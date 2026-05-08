---
title: "Lernland auf dem iPad-Wagen | App für geteilte Schulgeräte"
description: "Lernland auf dem iPad-Wagen: Schneller Schüler-Wechsel, Offline-Fähigkeit, Multi-Profil-Support. Die perfekte App für geteilte Schulgeräte."
source_html: "ipad-wagen-mathe-app.html"
license: CC-BY-4.0
author: Lukas Lutz
publication: Lernland
url: "https://lukaslutz.github.io/lernland-content/blog/ipad-wagen-mathe-app.html"
---

# Lernland auf dem iPad-Wagen: Perfekt für geteilte Schulgeräte

Multi-Profil-Support, schneller Wechsel, Offline-Fähigkeit - so funktioniert Lernland im Schulalltag

## Inhalt

  * Die Realität: Geteilte Geräte
  * Was eine App können muss
  * Wie Lernland diese Anforderungen erfüllt
  * iPad-Wagen einrichten
  * Workflow im Unterricht

## Die Realität: Nicht jedes Kind hat ein iPad

Die wenigsten Schulen haben 1:1-Ausstattung. Stattdessen:

  * **iPad-Wagen:** 16-20 Geräte, die sich Klassen teilen
  * **iPad-Koffer:** Mobile Einheit für verschiedene Räume
  * **Klassensatz:** Ein Set pro Schulhaus, reservierbar

### Herausforderungen

  * Jedes Kind braucht Zugang zu seinen Daten
  * Profile müssen auf jedem Gerät verfügbar sein
  * Schneller Wechsel zwischen Klassen nötig
  * Offline-Fähigkeit wegen instabilem WLAN
  * IT-Administration muss einfach sein

## Was eine App für geteilte Geräte können muss

### 1\. Mehrere Profile pro Gerät

Nicht jedes Kind bekommt immer dasselbe iPad. Profile müssen auf allen Geräten zugänglich sein.

### 2\. Schnelles An- und Abmelden

Keine langen Wartezeiten beim Klassenwechsel. In 30 Sekunden muss das nächste Kind arbeiten können.

### 3\. Offline-Funktionalität

20 iPads gleichzeitig im WLAN = oft Probleme. Die App muss ohne Internet funktionieren.

### 4\. Cloud-Sync

Fortschritt muss auf allen Geräten verfügbar sein - wenn Kind A heute auf iPad 3 arbeitet und morgen auf iPad 7.

### 5\. Automatisches Logout

Kind vergisst Abmelden? Das nächste Kind sollte nicht fremde Profile sehen.

## Wie Lernland diese Anforderungen erfüllt

### Multi-Profil-Support

  * Unbegrenzt viele Profile pro Gerät
  * Jedes Kind meldet sich mit Klassencode + Name + PIN an
  * Profile werden lokal gespeichert für schnellen Zugriff

### Schneller Login

  1. Klassencode eingeben (oder aus Liste wählen)
  2. Namen auswählen
  3. PIN eingeben
  4. Fertig - unter 30 Sekunden

### Vollständige Offline-Funktionalität

  * Alle Lernaktivitäten funktionieren ohne Internet
  * Fortschritt wird lokal gespeichert
  * Bei Verbindung: Automatischer Sync

### Cloud-Synchronisation

  * Arbeitet Kind auf iPad A, ist der Fortschritt auch auf iPad B
  * Firebase-Backend mit atomaren Updates
  * Konfliktauflösung: Server gewinnt

### Automatisches Logout

  * Nach 2 Minuten im Hintergrund: Automatische Abmeldung
  * Nur aktiv, wenn mehrere Profile auf dem Gerät
  * Verhindert versehentlichen Zugriff auf fremde Profile

### Geräte-Import-Code

Spezielle Funktion für iPad-Wagen:

  * Ein Code für die ganze Klasse
  * Alle Geräte gleichzeitig einrichten
  * Unterscheidet sich vom Schüler-Klassencode

## iPad-Wagen für Lernland einrichten

### Einmalige Vorbereitung

  1. **Lernland auf allen Geräten installieren**
     * Via MDM (Jamf, Mosyle, etc.) oder manuell
     * Apple School Manager Integration möglich
  2. **Geräte-Import-Code nutzen**
     * Lehrperson generiert Import-Code im Cockpit
     * Code auf allen Geräten eingeben
     * Alle Profile sind sofort verfügbar

### Für jede Klasse

  1. Lehrperson erstellt Klasse in Lernland
  2. Schülerprofile hinzufügen
  3. Import-Code an IT oder Stellvertretung weitergeben
  4. Code auf allen iPad-Wagen-Geräten eingeben

### MDM-Kompatibilität

Lernland funktioniert mit allen gängigen MDM-Lösungen:

  * Jamf Pro / Jamf School
  * Mosyle
  * Microsoft Intune
  * Apple Business Manager / School Manager

## Workflow im Unterricht

### Klasse 3a kommt dran (9:00)

  1. iPad-Wagen ins Zimmer rollen
  2. Jedes Kind nimmt ein iPad
  3. Kinder melden sich mit ihrer Karte an
  4. Arbeiten beginnt

### Klasse 3b kommt dran (10:00)

  1. Klasse 3a meldet sich ab (oder automatisches Logout)
  2. iPads zurück in den Wagen
  3. Wagen zu Klasse 3b
  4. Klasse 3b meldet sich an
  5. Jeder hat seinen eigenen Fortschritt

### Tipps für reibungslosen Ablauf

  * Login-Karten laminieren und griffbereit haben
  * Feste "iPad-Nummern" vermeiden - jedes Kind kann jedes iPad nehmen
  * Am Ende der Stunde: "Alle abmelden" als Ritual
  * iPads im Wagen laden lassen

## Perfekt für Ihren iPad-Wagen

Lernland wurde für genau diese Situation entwickelt: Viele Kinder, wenige Geräte, maximale Flexibilität.

[Lernland testen](<https://apps.apple.com/app/lernland>)

## Häufig gestellte Fragen

### Was passiert, wenn das WLAN ausfällt?

Kinder können weiterarbeiten. Alle Aktivitäten funktionieren offline. Der Fortschritt wird lokal gespeichert und synchronisiert, sobald wieder Verbindung besteht.

### Kann ein Kind das Profil eines anderen öffnen?

Nur mit dem korrekten PIN. Ohne PIN ist kein Zugriff möglich. Das automatische Logout nach 2 Minuten verhindert zudem, dass ein vergessenes Login offen bleibt.

### Wie viele Profile passen auf ein iPad?

Praktisch unbegrenzt. Lernland speichert Profile effizient. Ein iPad kann problemlos Hunderte von Profilen aus verschiedenen Klassen verwalten.

### Brauche ich IT-Kenntnisse für die Einrichtung?

Nein. Die Grundinstallation (App herunterladen) ist einfach. Der Geräte-Import-Code ermöglicht schnelles Einrichten ohne IT-Support.

## Das könnte Sie auch interessieren

  * [Klassenübergabe bei Lehrerwechsel](</blog/klassenuebergabe-lehrerwechsel>)
  * [Zugang für Fachpersonen](</blog/fachpersonen-zugang-logopaedie>)
  * [Lernland für Wochenplan-Arbeit](</blog/wochenplan-arbeit-mathe>)
  * [Das Kronen-System: Meisterschaft feiern](</blog/kronen-system-meisterschaft>)
  * [Login-Karten für Schüler erstellen](</blog/login-karten-schueler>)

## Das könnte Sie auch interessieren

  * [Klassenübergabe bei Lehrerwechsel](</blog/klassenuebergabe-lehrerwechsel>)
  * [Zugang für Fachpersonen](</blog/fachpersonen-zugang-logopaedie>)
  * [Lernland für Wochenplan-Arbeit](</blog/wochenplan-arbeit-mathe>)
  * [Das Kronen-System: Meisterschaft feiern](</blog/kronen-system-meisterschaft>)
  * [Login-Karten für Schüler erstellen](</blog/login-karten-schueler>)

## Das könnte Sie auch interessieren

  * [Klassenübergabe bei Lehrerwechsel](</blog/klassenuebergabe-lehrerwechsel>)
  * [Zugang für Fachpersonen](</blog/fachpersonen-zugang-logopaedie>)
  * [Lernland für Wochenplan-Arbeit](</blog/wochenplan-arbeit-mathe>)
  * [Das Kronen-System: Meisterschaft feiern](</blog/kronen-system-meisterschaft>)
  * [Login-Karten für Schüler erstellen](</blog/login-karten-schueler>)

## Das könnte Sie auch interessieren

  * [Klassenübergabe bei Lehrerwechsel](</blog/klassenuebergabe-lehrerwechsel>)
  * [Zugang für Fachpersonen](</blog/fachpersonen-zugang-logopaedie>)
  * [Lernland für Wochenplan-Arbeit](</blog/wochenplan-arbeit-mathe>)
  * [Das Kronen-System: Meisterschaft feiern](</blog/kronen-system-meisterschaft>)
  * [Login-Karten für Schüler erstellen](</blog/login-karten-schueler>)

## Das könnte Sie auch interessieren

  * [Klassenübergabe bei Lehrerwechsel](</blog/klassenuebergabe-lehrerwechsel>)
  * [Zugang für Fachpersonen](</blog/fachpersonen-zugang-logopaedie>)
  * [Lernland für Wochenplan-Arbeit](</blog/wochenplan-arbeit-mathe>)
  * [Das Kronen-System: Meisterschaft feiern](</blog/kronen-system-meisterschaft>)
  * [Login-Karten für Schüler erstellen](</blog/login-karten-schueler>)