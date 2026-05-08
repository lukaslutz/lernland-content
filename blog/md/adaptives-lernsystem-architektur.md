---
title: "Wie adaptives Lernen funktioniert: Die Technologie hinter intelligenten Mathe-Apps"
description: "Technischer Deep-Dive: So funktioniert adaptives Lernen in modernen Lern-Apps. Voraussetzungs-Mapping, Schwierigkeitsanpassung und KI-Algorithmen erklärt."
source_html: "adaptives-lernsystem-architektur.html"
license: CC-BY-4.0
author: Lukas Lutz
publication: Lernland
url: "https://lukaslutz.github.io/lernland-content/blog/adaptives-lernsystem-architektur.html"
---

# Wie adaptives Lernen funktioniert: Die Technologie hinter intelligenten Mathe-Apps

**Kernaussage:** Adaptive Lernsysteme analysieren das Antwortverhalten in Echtzeit und passen Schwierigkeit sowie Aufgabenauswahl automatisch an. Lernland implementiert dieses Prinzip durch ein Voraussetzungs-Mapping basierend auf dem [Lehrplan 21 App](</blog/mathe-app-lehrplan-21>) und erreicht damit eine optimale Erfolgsrate von 70-80% für jedes Kind.

## Das Problem statischer Lerninhalte

Traditionelle Lernmaterialien haben einen fundamentalen Fehler. Sie präsentieren allen Kindern dieselben Aufgaben in derselben Reihenfolge. Das führt zu zwei Problemen: Kinder mit Lücken werden überfordert und scheitern. Kinder ohne Lücken langweilen sich und verlieren Motivation.

Adaptive Systeme lösen dieses Dilemma durch kontinuierliche Anpassung. Die Software beobachtet, analysiert und reagiert – in Echtzeit, bei jeder einzelnen Antwort.

## Die drei Säulen adaptiven Lernens

### 1\. Erfolgsraten-Tracking

Lernland erfasst für jede Aktivität zwei Kernmetriken: korrekte Antworten und inkorrekte Antworten. Aus diesem Verhältnis berechnet das System die aktuelle Erfolgsrate. Liegt diese unter 70%, reduziert der Algorithmus die Schwierigkeit. Liegt sie über 80%, erhöht er sie.

Diese Zielzone von 70-80% ist nicht willkürlich gewählt. Lernpsychologische Forschung zeigt, dass in diesem Bereich die optimale Kombination aus Herausforderung und Erfolgserlebnis liegt. Zu leicht demotiviert. Zu schwer frustriert.

### 2\. Voraussetzungs-Mapping

Mathematische Kompetenzen bauen aufeinander auf. Wer den [Zehnerübergang üben](</blog/zehneruebergang-app>) nicht beherrscht, scheitert bei der Addition bis 100. Wer keine Mengen erfassen kann, hat Schwierigkeiten mit dem Zahlbegriff.

Lernland modelliert diese Abhängigkeiten explizit. Ein Auszug aus dem Mapping:

  * **Plus im 20er Raum (Zehnerübergang)** setzt voraus: Plus im 10er Raum, Immer 10, Strukturiert 20
  * **Minuten ablesen** setzt voraus: Viertelstundentakt
  * **Zahlenstreifen bis 10** setzt voraus: Strukturiert 10, Zahlenstreifen bis 5

Wenn ein Kind bei einer Aktivität wiederholt scheitert, prüft das System die Voraussetzungen. Fehlt eine Basis-Kompetenz, wird automatisch diese zuerst trainiert.

### 3\. Dynamische Schwellen

Nicht alle Kinder lernen gleich schnell. Lernland passt die Freischaltungs-Schwellen für neue Aktivitäten dynamisch an:

Genauigkeit | Benötigte korrekte Antworten  
---|---  
≥ 90% | 10  
≥ 75% | 15  
< 75% | 25  
  
Ein Kind mit hoher Trefferquote schreitet schneller voran. Ein Kind, das noch unsicher ist, erhält mehr Übung auf dem aktuellen Niveau.

## Cold-Start-Problem und Lösung

Neue Benutzer stellen adaptive Systeme vor ein Dilemma: Es existieren keine Daten, um das Niveau einzuschätzen. Lernland löst dieses Cold-Start-Problem durch zwei Mechanismen.

Erstens: Die initiale Klassenstufe. Lehrpersonen oder Eltern geben an, in welcher Klasse das Kind ist. Das System startet mit altersgerechten Aktivitäten statt bei Kindergarten-Übungen für einen Drittklässler.

Zweitens: Fundament-Aktivitäten. Bestimmte Aktivitäten haben keine Voraussetzungen – sie dienen als Einstiegspunkt und liefern erste Datenpunkte für die Kalibrierung.

## Technische Implementierung

Lernland verwendet eine Schwierigkeitsskala von 0.0 bis 1.0. Jede Aktivität generiert Aufgaben basierend auf diesem Wert. Bei 0.2 sind die Aufgaben einfach. Bei 0.8 anspruchsvoll.

Die Anpassungslogik folgt klaren Regeln:

  * 5 korrekte Antworten in Folge → Schwierigkeit erhöhen
  * 3 inkorrekte Antworten in Folge → Schwierigkeit reduzieren
  * Erfolgsrate dauerhaft unter 70% → Voraussetzungs-Aktivität vorschlagen

Diese Logik läuft vollständig auf dem Gerät. Keine Serveranfrage, keine Latenz. Das Kind merkt die Anpassung nicht – es erlebt nur, dass die Aufgaben "irgendwie passend" sind.

## Offline-First-Architektur

Schulen haben oft instabile Internetverbindungen. Deshalb speichert Lernland alle Daten lokal. Die Lernalgorithmen funktionieren ohne Server. Bei verfügbarer Verbindung synchronisiert das System automatisch mit Firebase.

Diese Architektur hat einen Nebeneffekt: Geschwindigkeit. Die Anpassung erfolgt instantan, weil keine Netzwerklatenz existiert.

## Vergleich: Adaptiv vs. Nicht-adaptiv

Aspekt | Statische App | Adaptive App (Lernland)  
---|---|---  
Schwierigkeit | Fest vorgegeben | Passt sich in Echtzeit an  
Aufgabenauswahl | Lineare Reihenfolge | Basierend auf Kompetenzstand  
Lücken | Werden übersprungen | Werden erkannt und gefüllt  
Frustration | Bei Überforderung hoch | Durch Anpassung minimiert  
  
## Implikationen für Förderbedarf

Kinder mit besonderem Förderbedarf profitieren überproportional von adaptiven Systemen. Ihre Lernkurven sind oft nicht linear. Sie haben punktuelle Stärken und Lücken an unerwarteten Stellen.

Lernland wurde explizit für diese Zielgruppe entwickelt. Das Voraussetzungs-Mapping bildet den [Lehrplan 21 App](</blog/mathe-app-lehrplan-21>) ab und erkennt, wenn fundamentale Kompetenzen fehlen – selbst wenn das Kind bereits in der dritten Klasse ist.

## Zusammenfassung

Adaptives Lernen ist keine Marketing-Phrase. Es bezeichnet ein konkretes technisches System: Erfolgsraten-Tracking, Voraussetzungs-Mapping und dynamische Schwellen arbeiten zusammen, um jedem Kind das optimale Lernniveau zu bieten.

Lernland implementiert diese Prinzipien vollständig, offline-fähig und optimiert für Kinder mit besonderem Förderbedarf.

**App herunterladen:** [Lernland im App Store](<https://apps.apple.com/ch/app/lernland/id6748945706>)