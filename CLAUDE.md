# Lernland Blog - Projekt-Kontext

## GitHub Repository
- **Repository:** https://github.com/lukaslutz/lernland-blog
- **Lokaler Pfad:** `/Users/lukas/Documents/Projekte/: SEO/Lernland/Fertige Blog Posts.`

## App Store Link
- **Lernland:** https://apps.apple.com/ch/app/lernland/id6748945706

## Nach dem Erstellen neuer Blogposts

Wenn neue Blogposts erstellt wurden, führe automatisch diese Schritte aus:

1. **Skripte ausführen:**
   ```bash
   cd "/Users/lukas/Documents/Projekte/: SEO/Lernland"
   python3 fix_blogposts.py
   python3 add_app_store_cta.py
   ```

2. **Auf GitHub pushen:**
   ```bash
   cd "/Users/lukas/Documents/Projekte/: SEO/Lernland/Fertige Blog Posts."
   git add .
   git commit -m "Neue Blogposts hinzugefügt"
   git push
   ```

## Wichtige Regeln für Blogposts

- Jeder Post MUSS den App Store Link enthalten
- App Store Link: `https://apps.apple.com/ch/app/lernland/id6748945706`
- CTA-Box am Ende jedes Posts (wird durch `add_app_store_cta.py` hinzugefügt)
- Struktur gemäss `BLOG-KORPUS-BLUEPRINT-HUGO.md`

## Dateien im Projekt

| Datei | Zweck |
|-------|-------|
| `1. Beschreibung.md` | App-Dokumentation für Content-Erstellung |
| `2. Fragen.md` | SEO-Keywords und Suchfragen |
| `fix_blogposts.py` | Fügt Schema, BreadcrumbList, Related Posts hinzu |
| `add_app_store_cta.py` | Fügt App Store CTA-Box hinzu |
| `add_internal_links.py` | Fügt interne Links hinzu |
