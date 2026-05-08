#!/usr/bin/env python3
"""
Fügt interne Links zu den Klaro Blogposts hinzu.
"""

import os
import re
from pathlib import Path

POSTS_DIR = Path("/Users/lukas/Documents/Projekte/: SEO/Klaro/Fertige Blog Posts.")

# Link-Regeln basierend auf Keywords (Keyword -> (slug, anchor_text))
LINK_RULES = {
    # Grundlagen
    "rechnen lernen": ("beste-mathe-app-kinder", "Mathe-App für Kinder"),
    "Rechenschwäche": ("rechenschwaeche-app-ueben", "Rechenschwäche mit Apps üben"),
    "Dyskalkulie": ("rechenschwaeche-app-ueben", "Dyskalkulie-Förderung"),
    "Mathe-Angst": ("mathe-angst-bei-kindern", "Mathe-Angst überwinden"),

    # Lehrplan
    "Lehrplan 21": ("mathe-app-lehrplan-21", "Lehrplan 21 App"),
    "Primarschule": ("lernapp-schweiz-primarschule", "Lern-App für Primarschule"),
    "Schweiz": ("lernapp-schweiz-primarschule", "Schweizer Lern-App"),

    # Konkrete Themen
    "Uhr lesen": ("uhr-lesen-lernen-app", "Uhr lesen lernen"),
    "Einmaleins": ("einmaleins-lernen-app", "Einmaleins üben"),
    "Kopfrechnen": ("kopfrechnen-app", "Kopfrechnen trainieren"),
    "Zehnerübergang": ("zehneruebergang-app", "Zehnerübergang üben"),

    # Features
    "offline": ("lernapp-ohne-internet", "offline nutzbar"),
    "Gamification": ("lernapp-mit-belohnungen-gamification", "Gamification-Features"),
    "Belohnungen": ("lernapp-mit-belohnungen-gamification", "Belohnungssystem"),
    "mehrere Kinder": ("lernapp-mehrere-kinder", "mehrere Kinder-Profile"),

    # Pädagogik
    "Heilpädagogik": ("app-heilpaedagogik-if-unterricht", "Heilpädagogik-Einsatz"),
    "Förderunterricht": ("app-heilpaedagogik-if-unterricht", "IF-Unterricht"),
    "Differenzierung": ("app-differenzierung-mathe", "differenzierter Unterricht"),

    # Alternativen
    "Anton": ("anton-app-alternative", "Anton Alternative"),

    # Eltern
    "Eltern": ("mein-kind-kann-nicht-rechnen", "Tipps für Eltern"),
    "Hausaufgaben": ("schlechte-mathe-note-hausaufgaben-nicht-die-loesung", "Hausaufgaben-Tipps"),

    # Ferien
    "Ferien": ("mathe-lernen-ferien", "Mathe in den Ferien"),
    "Sommerferien": ("sommerferien-lernrueckstand-aufholen", "Sommerferien-Lernen"),
}

def add_links_to_post(filepath):
    """Fügt Links zu einem Post hinzu"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    links_added = 0

    for keyword, (slug, anchor_text) in LINK_RULES.items():
        if links_added >= 3:
            break

        # Nicht in eigenen Post verlinken
        if slug in filepath.name:
            continue

        # Prüfe ob Link schon existiert
        if f'href="/blog/{slug}"' in content:
            continue

        # Suche das Keyword
        pattern = rf'\b({re.escape(keyword)})\b'

        if re.search(pattern, content, re.IGNORECASE):
            link = f'<a href="/blog/{slug}">{anchor_text}</a>'

            # Ersetze nur in Paragraphen
            def replace_in_paragraph(match):
                nonlocal links_added
                if links_added >= 3:
                    return match.group(0)

                para = match.group(0)

                if f'href="/blog/{slug}"' in para:
                    return para

                if '<h' in para[:10]:
                    return para

                if re.search(pattern, para, re.IGNORECASE):
                    links_added += 1
                    return re.sub(pattern, link, para, count=1, flags=re.IGNORECASE)

                return para

            content = re.sub(r'<p>.*?</p>', replace_in_paragraph, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return links_added

def main():
    print("=" * 50)
    print("Klaro: Interne Links hinzufügen")
    print("=" * 50)
    print()

    total_links = 0
    files = sorted(POSTS_DIR.glob("*.html"))

    for i, filepath in enumerate(files):
        links = add_links_to_post(filepath)
        total_links += links
        if (i + 1) % 50 == 0:
            print(f"  Verarbeitet: {i + 1}/{len(files)} ({total_links} Links)")

    print()
    print(f"Total: {len(files)} Posts, {total_links} Links hinzugefügt")
    print()
    print("=" * 50)
    print("Fertig!")
    print("=" * 50)

if __name__ == "__main__":
    main()
