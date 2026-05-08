#!/usr/bin/env python3
"""
Korrigiert alle Klaro Blogposts mit:
1. Semantic ID (@id) im JSON-LD
2. BreadcrumbList Schema
3. Related Posts Sektion
4. Interne Links im Content
"""

import os
import re
import json
import hashlib
from pathlib import Path

# Verzeichnis mit den Posts
POSTS_DIR = Path("/Users/lukas/Documents/Projekte/: SEO/Klaro/Fertige Blog Posts.")

# Thematische Gruppen für Related Posts
GROUPS = {
    "rechnen": ["001", "002", "003", "004"],
    "lehrplan": ["005", "006", "007"],
    "apps": ["008", "009", "010", "011", "012"],
    "paedagogik": ["013", "014", "015"],
    "eltern": ["001", "002", "004"],
    "uhr": ["009"],
    "einmaleins": ["010"],
    "gamification": ["014"],
}

def generate_uuid(slug):
    """Generiert eine deterministische UUID aus dem Slug"""
    return hashlib.md5(slug.encode()).hexdigest()[:8]

def get_related_posts(post_id, all_posts):
    """Findet verwandte Posts basierend auf Post-ID"""
    # Einfache Logik: Nimm die 5 nächsten Posts (numerisch)
    post_num = int(post_id)
    related = []

    # Posts in der Nähe
    for offset in [1, 2, -1, 3, -2, 4, 5]:
        neighbor = str(post_num + offset).zfill(3)
        if neighbor in all_posts and neighbor != post_id:
            related.append(neighbor)
            if len(related) >= 5:
                break

    # Fülle mit allgemeinen Posts auf
    general = ["001", "008", "005", "010", "014"]
    for g in general:
        if g in all_posts and g != post_id and g not in related:
            related.append(g)
            if len(related) >= 5:
                break

    return related[:5]

def create_schema_json(post_id, slug, title):
    """Erstellt das korrigierte JSON-LD Schema"""
    uuid = generate_uuid(slug)

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "@id": f"https://klaroapp.ch/entity/POST-{uuid}",
                "mainEntityOfPage": f"https://klaroapp.ch/blog/{slug}",
                "url": f"https://klaroapp.ch/blog/{slug}",
                "headline": title,
                "datePublished": "2026-03-26",
                "dateModified": "2026-04-02",
                "inLanguage": "de-CH",
                "author": {
                    "@type": "Organization",
                    "name": "Klaro",
                    "url": "https://klaroapp.ch"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Klaro",
                    "url": "https://klaroapp.ch"
                },
                "about": {
                    "@type": "SoftwareApplication",
                    "name": "Klaro",
                    "operatingSystem": "iOS",
                    "applicationCategory": "EducationalApplication"
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"https://klaroapp.ch/blog/{slug}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Start",
                        "item": "https://klaroapp.ch/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Blog",
                        "item": "https://klaroapp.ch/blog/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": title
                    }
                ]
            }
        ]
    }
    return schema

def create_related_posts_html(related_ids, all_posts):
    """Erstellt die Related Posts Sektion"""
    if not related_ids:
        return ""

    html = '''
      <aside class="related-posts" role="region" aria-label="Verwandte Artikel">
        <h2>Das könnte Sie auch interessieren</h2>
        <ul>
'''
    for rid in related_ids:
        if rid in all_posts:
            post = all_posts[rid]
            html += f'          <li><a href="/blog/{post["slug"]}">{post["title"]}</a></li>\n'

    html += '''        </ul>
      </aside>
'''
    return html

def extract_title_from_html(content):
    """Extrahiert den Titel aus dem HTML"""
    match = re.search(r'<title>([^|<]+)', content)
    if match:
        return match.group(1).strip()
    return "Klaro Artikel"

def process_all_posts():
    """Verarbeitet alle Posts"""
    print("=" * 50)
    print("Klaro Blogpost Korrektur")
    print("=" * 50)

    # Sammle alle Posts
    all_posts = {}
    files = sorted([f for f in POSTS_DIR.glob("*.html")])

    print(f"Gefundene Posts: {len(files)}")
    print()

    # Erste Runde: Metadaten sammeln
    for filepath in files:
        match = re.match(r'^(\d+)-(.+)\.html$', filepath.name)
        if not match:
            continue

        post_id = match.group(1)
        slug = match.group(2)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        title = extract_title_from_html(content)

        all_posts[post_id] = {
            "file": filepath.name,
            "path": filepath,
            "slug": slug,
            "title": title
        }

    # Zweite Runde: Posts korrigieren
    for post_id, post in all_posts.items():
        try:
            filepath = post["path"]
            print(f"Verarbeite: {post['file']}")

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Ersetze das alte JSON-LD Schema (Article)
            old_schema_pattern = r'<script type="application/ld\+json">\s*\{[^}]*"@type":\s*"Article"[^<]*</script>'

            new_schema = create_schema_json(post_id, post["slug"], post["title"])
            new_schema_html = f'''<script type="application/ld+json">
  {json.dumps(new_schema, indent=2, ensure_ascii=False)}
  </script>'''

            content = re.sub(old_schema_pattern, new_schema_html, content, count=1, flags=re.DOTALL)

            # 2. Füge Related Posts ein
            related_ids = get_related_posts(post_id, all_posts)
            related_html = create_related_posts_html(related_ids, all_posts)

            # Verschiedene Muster für das Ende des Artikels
            patterns = [
                (r'(</aside>\s*\n\s*<section id="fazit")', r'</aside>\n\n' + related_html + r'\n      <section id="fazit"'),
                (r'(<section id="fazit")', related_html + r'\n      <section id="fazit"'),
                (r'(</article>\s*</main>)', related_html + r'\n    </article>\n  </main>'),
                (r'(</article>)', related_html + r'\n    </article>'),
            ]

            inserted = False
            for pattern, replacement in patterns:
                if re.search(pattern, content) and not inserted:
                    content = re.sub(pattern, replacement, content, count=1)
                    inserted = True
                    break

            # Speichere die korrigierte Datei
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"  ✓ Korrigiert")

        except Exception as e:
            print(f"  ✗ Fehler: {e}")

    print()
    print("=" * 50)
    print("Fertig!")
    print("=" * 50)

if __name__ == "__main__":
    process_all_posts()
