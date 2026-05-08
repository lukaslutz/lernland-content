---
title: "Datenschutz Lernapp Schweiz: Sichere Apps für Schulen und Familien"
description: "Wie sicher ist Lernland? Die Schweizer Lernapp ist DSGVO/DSG-konform, werbefrei, ohne Tracking. Daten werden in der EU gespeichert. Ideal für Schulen."
source_html: "datenschutz-lernapp-schweiz.html"
license: CC-BY-4.0
author: Lukas Lutz
publication: Lernland
---

1. [Start](</>)
  2. [Blog](</blog>)
  3. Datenschutz Lernapp Schweiz

# Datenschutz Lernapp Schweiz: Sichere Apps für Schulen und Familien

26\. März 2026 Lesezeit: 7 Min.

**Kurz gesagt:** **[Lernland](<https://apps.apple.com/ch/app/lernland/id6748945706>)** nimmt Datenschutz ernst. Die App ist **DSGVO/DSG-konform** , speichert Daten in der EU (Frankfurt), ist komplett **werbefrei** und verwendet **kein externes Tracking**. Für Kinder werden nur minimale Daten erfasst (Vorname, Lernfortschritt). Ideal für Schweizer Schulen mit hohen Datenschutz-Anforderungen.

## Warum Datenschutz bei Lernapps wichtig ist

Lernapps für Kinder verarbeiten sensible Daten:

  * Namen und Alter von Minderjährigen
  * Lernfortschritt und Leistungsdaten
  * Potentiell Standortdaten und Nutzungsverhalten

Viele kostenlose Apps finanzieren sich durch Werbung und Datenverkauf. Das ist bei Kinder-Apps besonders problematisch. **Lernland** geht einen anderen Weg.

## Lernland und Datenschutz: Die wichtigsten Punkte

### DSGVO/DSG-Konformität

Lernland erfüllt sowohl die europäische DSGVO als auch das Schweizer Datenschutzgesetz (DSG):

  * Rechtmässige Datenverarbeitung
  * Zweckbindung (nur für Lernzwecke)
  * Datenminimierung (nur das Nötigste)
  * Speicherbegrenzung
  * Integrität und Vertraulichkeit

### Server-Standort: EU (Frankfurt)

Alle Daten werden auf Firebase-Servern in **Frankfurt (europe-west3)** gespeichert:

  * Innerhalb der EU – DSGVO-konform
  * Kein Datentransfer in die USA oder andere Drittländer
  * Für Schweizer Schulen geeignet (Äquivalenz-Anerkennung EU)

### Keine Werbung

Lernland ist **komplett werbefrei** :

  * Keine Banner, keine Videos, keine Pop-ups
  * Keine Werbe-SDKs integriert
  * Keine Datenweitergabe an Werbenetzwerke

### Kein externes Tracking

Lernland verwendet **keine externen Analyse-Tools** :

  * Kein Google Analytics
  * Kein Facebook Pixel
  * Keine Third-Party-Tracker

Intern wird nur erfasst, was für die App-Funktion nötig ist (Lernfortschritt).

## Welche Daten werden gespeichert?

### Für Kinder (Schülerprofile)

Daten | Gespeichert? | Zweck  
---|---|---  
Vorname | Ja | Identifikation im Profil  
Nachname | Nein | –  
E-Mail | Nein | –  
Geburtsdatum | Nein | –  
Foto | Nein | –  
PIN | Ja | Login  
Lernfortschritt | Ja | Kern-Funktionalität  
Münzen/Levels | Ja | Gamification  
  
### Für Erwachsene (Lehrpersonen, Eltern)

Daten | Gespeichert? | Zweck  
---|---|---  
E-Mail | Ja | Login via Firebase Auth  
Name | Optional | Anzeige  
Profilbild | Optional | Von OAuth-Provider (Google/Apple)  
  
## Datensicherheit

### Verschlüsselung

  * **Transport:** TLS/HTTPS für alle Verbindungen
  * **Speicherung:** Firebase-Standardverschlüsselung

### Authentifizierung

  * **Kinder:** Klassencode + Name + PIN (kein Firebase Auth)
  * **Erwachsene:** Firebase Authentication (Google, Apple, E-Mail)

### Zugriffskontrolle

  * Lehrpersonen sehen nur ihre eigenen Klassen
  * Fachpersonen sehen nur ihnen zugewiesene Kinder
  * Eltern sehen nur ihre eigenen Kinder

## Für Schulen: Datenschutz-Checkliste

Wenn Sie Lernland an Ihrer Schule einführen möchten, hier die wichtigsten Punkte:

Anforderung | Lernland  
---|---  
DSGVO-konform? | ✅ Ja  
DSG (Schweiz) konform? | ✅ Ja  
Server in EU/CH? | ✅ Frankfurt (EU)  
Werbefrei? | ✅ Ja  
Ohne externes Tracking? | ✅ Ja  
Minimale Kinderdaten? | ✅ Nur Vorname + Lernfortschritt  
Keine E-Mail für Kinder? | ✅ Korrekt  
Daten löschbar? | ✅ Profile können gelöscht werden  
AVV verfügbar? | ✅ Auf Anfrage  
  
**AVV:** Auftragsverarbeitungsvertrag – für Schulen oft erforderlich. Kontaktieren Sie uns für Details.

## Häufige Bedenken

### "Ist Firebase sicher?"

Firebase ist ein Google-Dienst, aber:

  * Server-Standort ist wählbar (wir nutzen EU)
  * Keine Datenweitergabe an Google für andere Zwecke
  * Firebase ist weit verbreitet und wird regelmässig auditiert

### "Was passiert mit den Daten, wenn wir Lernland nicht mehr nutzen?"

  * Profile können jederzeit gelöscht werden
  * Bei Klassen-Löschung werden alle Schülerdaten entfernt
  * Auf Anfrage: Komplette Datenlöschung

### "Können Kinder mit anderen Kindern kommunizieren?"

Nein, Lernland hat **keine Chat- oder Kommunikationsfunktion**. Kinder können sich nicht gegenseitig kontaktieren.

## Transparenz

Lernland informiert offen:

  * **Datenschutzerklärung:** In der App und auf der Website
  * **AGB:** Klar formuliert
  * **Kontakt:** Datenschutzanfragen werden beantwortet

## Jetzt Lernland kostenlos testen

Die Schweizer Lern-App für Mathematik in der Primarschule. Über 50 Aktivitäten, adaptives Lernen, ohne Werbung.

[ Kostenlos im App Store laden ](<https://apps.apple.com/ch/app/lernland/id6748945706>)

## Fazit: Lernland nimmt Datenschutz ernst

Eine **sichere Lernapp für die Schweiz** muss hohe Standards erfüllen. **Lernland** bietet:

  * DSGVO/DSG-Konformität
  * Server in der EU (Frankfurt)
  * Komplett werbefrei
  * Kein externes Tracking
  * Minimale Kinderdaten (nur Vorname)
  * Keine Kommunikationsfunktionen
  * Daten löschbar

**Für Schulen:** AVV auf Anfrage verfügbar.

**Jetzt testen:** [Lernland im App Store herunterladen](<https://apps.apple.com/ch/app/lernland/id6748945706>)

## Häufige Fragen

Ist Lernland DSGVO-konform?

Ja, vollständig. Daten werden in der EU (Frankfurt) gespeichert, kein externes Tracking, keine Werbung.

Welche Daten speichert Lernland von meinem Kind?

Nur das Minimum: Vorname, Lernfortschritt, Münzen, Levels. Keine E-Mail, kein Geburtsdatum, keine Fotos.

Wo werden die Daten gespeichert?

Firebase-Server in Frankfurt (europe-west3), innerhalb der EU.

Gibt es Werbung oder Tracking?

Nein, Lernland ist komplett werbefrei und verwendet keine externen Analyse-Tools.

## Weiterlesen

  * [Lernapp Schweiz Primarschule](</blog/lernapp-schweiz-primarschule>)
  * [Lernapp mit Lehrerbereich](</blog/lernapp-mit-lehrerbereich-statistiken>)
  * [Lernapp ohne Internet](</blog/lernapp-ohne-internet>)

## Das könnte Sie auch interessieren

  * [Mathe App Kindergarten: Spielerisch Zahlen lernen ab 4 Jahren](</blog/mathe-app-kindergarten>)
  * [Mathe App für Erstklässler: Rechnen lernen in der 1. Klasse](</blog/mathe-app-erstklassler>)
  * [Anton App Alternative: Warum Lernland die bessere Wahl für die Schweiz ist](</blog/anton-app-alternative>)
  * [Plus und Minus üben App: Addition und Subtraktion für Kinder](</blog/plus-und-minus-ueben-app>)
  * [Lernapp mit Lehrerbereich: Statistiken und Klassenverwaltung](</blog/lernapp-mit-lehrerbereich-statistiken>)

## Das könnte Sie auch interessieren

  * [Mathe App Kindergarten: Spielerisch Zahlen lernen ab 4 Jahren](</blog/mathe-app-kindergarten>)
  * [Mathe App für Erstklässler: Rechnen lernen in der 1. Klasse](</blog/mathe-app-erstklassler>)
  * [Anton App Alternative: Warum Lernland die bessere Wahl für die Schweiz ist](</blog/anton-app-alternative>)
  * [Plus und Minus üben App: Addition und Subtraktion für Kinder](</blog/plus-und-minus-ueben-app>)
  * [Lernapp mit Lehrerbereich: Statistiken und Klassenverwaltung](</blog/lernapp-mit-lehrerbereich-statistiken>)

## Das könnte Sie auch interessieren

  * [Mathe App Kindergarten: Spielerisch Zahlen lernen ab 4 Jahren](</blog/mathe-app-kindergarten>)
  * [Mathe App für Erstklässler: Rechnen lernen in der 1. Klasse](</blog/mathe-app-erstklassler>)
  * [Anton App Alternative: Warum Lernland die bessere Wahl für die Schweiz ist](</blog/anton-app-alternative>)
  * [Plus und Minus üben App: Addition und Subtraktion für Kinder](</blog/plus-und-minus-ueben-app>)
  * [Lernapp mit Lehrerbereich: Statistiken und Klassenverwaltung](</blog/lernapp-mit-lehrerbereich-statistiken>)

## Das könnte Sie auch interessieren

  * [Mathe App Kindergarten: Spielerisch Zahlen lernen ab 4 Jahren](</blog/mathe-app-kindergarten>)
  * [Mathe App für Erstklässler: Rechnen lernen in der 1. Klasse](</blog/mathe-app-erstklassler>)
  * [Anton App Alternative: Warum Lernland die bessere Wahl für die Schweiz ist](</blog/anton-app-alternative>)
  * [Plus und Minus üben App: Addition und Subtraktion für Kinder](</blog/plus-und-minus-ueben-app>)
  * [Lernapp mit Lehrerbereich: Statistiken und Klassenverwaltung](</blog/lernapp-mit-lehrerbereich-statistiken>)

## Das könnte Sie auch interessieren

  * [Mathe App Kindergarten: Spielerisch Zahlen lernen ab 4 Jahren](</blog/mathe-app-kindergarten>)
  * [Mathe App für Erstklässler: Rechnen lernen in der 1. Klasse](</blog/mathe-app-erstklassler>)
  * [Anton App Alternative: Warum Lernland die bessere Wahl für die Schweiz ist](</blog/anton-app-alternative>)
  * [Plus und Minus üben App: Addition und Subtraktion für Kinder](</blog/plus-und-minus-ueben-app>)
  * [Lernapp mit Lehrerbereich: Statistiken und Klassenverwaltung](</blog/lernapp-mit-lehrerbereich-statistiken>)

(C) 2026 Lernland. Alle Rechte vorbehalten.