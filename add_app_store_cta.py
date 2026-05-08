#!/usr/bin/env python3
"""
Fügt App Store CTA-Box zu allen Klaro Blogposts hinzu und korrigiert bestehende Links.
"""

import os
import re
from pathlib import Path

# Konfiguration
BLOG_DIR = Path(__file__).parent / "Fertige Blog Posts."
APP_STORE_URL = "https://apps.apple.com/ch/app/klaro/id6748945706"
APP_NAME = "Klaro"

# CTA Box HTML
CTA_BOX = f'''
      <aside class="app-download-cta">
        <h2>Jetzt {APP_NAME} kostenlos testen</h2>
        <p>Die Schweizer Lern-App für Mathematik in der Primarschule. Über 50 Aktivitäten, adaptives Lernen, ohne Werbung.</p>
        <a href="{APP_STORE_URL}" class="btn-appstore">
          Kostenlos im App Store laden
        </a>
      </aside>
'''

def fix_post(filepath):
    """Korrigiert einen einzelnen Blogpost."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Ersetze alle unvollständigen/falschen App Store Links
    # Alte Patterns: https://apps.apple.com/ch/app/klaro (ohne ID)
    content = re.sub(
        r'https://apps\.apple\.com/ch/app/klaro(?!/id)',
        APP_STORE_URL,
        content
    )

    # 2. Prüfe ob CTA Box bereits existiert
    if 'class="app-download-cta"' not in content:
        # Füge CTA Box vor dem Fazit ein
        if '<section id="fazit">' in content:
            content = content.replace(
                '<section id="fazit">',
                CTA_BOX + '\n      <section id="fazit">'
            )
        # Oder am Ende des main-Tags
        elif '</main>' in content:
            content = content.replace(
                '</main>',
                CTA_BOX + '\n    </main>'
            )

    # 3. Stelle sicher, dass der App-Name im TLDR verlinkt ist
    # Suche nach "Klaro" ohne Link im tldr
    tldr_pattern = r'(<p class="tldr">.*?)(Klaro)(.*?</p>)'

    def add_link_to_tldr(match):
        before = match.group(1)
        app_name = match.group(2)
        after = match.group(3)

        # Prüfe ob bereits ein Link vorhanden
        if f'href="{APP_STORE_URL}"' in before or f'href="{APP_STORE_URL}"' in after:
            return match.group(0)

        # Prüfe ob irgendein Link um Klaro ist
        if '<a href=' in before[-50:] and '</a>' in after[:20]:
            return match.group(0)

        # Füge Link hinzu
        return f'{before}<a href="{APP_STORE_URL}">{app_name}</a>{after}'

    content = re.sub(tldr_pattern, add_link_to_tldr, content, flags=re.DOTALL)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 50)
    print(f"{APP_NAME} App Store CTA Updater")
    print("=" * 50)

    if not BLOG_DIR.exists():
        print(f"Fehler: Verzeichnis nicht gefunden: {BLOG_DIR}")
        return

    html_files = sorted(BLOG_DIR.glob("*.html"))
    print(f"Gefundene Posts: {len(html_files)}")
    print()

    updated = 0
    for filepath in html_files:
        print(f"Verarbeite: {filepath.name}", end="")
        if fix_post(filepath):
            print(" -> Aktualisiert")
            updated += 1
        else:
            print(" -> Keine Änderung")

    print()
    print("=" * 50)
    print(f"Fertig! {updated} Posts aktualisiert.")
    print("=" * 50)

if __name__ == "__main__":
    main()
