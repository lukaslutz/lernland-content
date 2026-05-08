---
title: "Adaptives Lernen erklärt: Wie intelligente Lern-Apps sich dem Kind anpassen"
description: "Wie funktioniert adaptives Lernen in modernen Lern-Apps? Ein technischer Blick auf die Architektur hinter personalisiertem Mathe-Training für Kinder mit Förderbedarf."
source_html: "adaptives-lernen-ki-lernapp.html"
license: CC-BY-4.0
author: Lukas Lutz
publication: Lernland
url: "https://lukaslutz.github.io/lernland-content/blog/adaptives-lernen-ki-lernapp.html"
---

# Adaptives Lernen erklärt: Wie intelligente Lern-Apps sich dem Kind anpassen

**Ein technischer Deep-Dive in die Architektur moderner Lernsysteme**

## Das Problem mit statischen Lernprogrammen

Die meisten digitalen Lernmaterialien arbeiten nach einem starren Prinzip: Aufgabe für Aufgabe, Seite für Seite, unabhängig davon, ob das Kind die Inhalte bereits beherrscht oder noch Schwierigkeiten hat. Ein Erstklässler, der problemlos im Zahlenraum bis 10 rechnet, langweilt sich. Ein Kind mit Förderbedarf wird frustriert, weil die Aufgaben zu schnell schwieriger werden.

Adaptive Lernsysteme lösen dieses Problem durch kontinuierliche Analyse des Lernverhaltens. Sie passen Schwierigkeit, Aufgabentyp und Lernpfad individuell an.

## Wie funktioniert adaptive Schwierigkeitsanpassung?

Ein gut konzipiertes adaptives System verfolgt mehrere Metriken gleichzeitig:

### Erfolgsquote als Kernmetrik

Die optimale Erfolgsquote für nachhaltiges Lernen liegt zwischen 70 und 80 Prozent. Liegt ein Kind darunter, ist es überfordert. Liegt es darüber, fehlt die Herausforderung. Lernland verwendet diese Zielerfolgsrate als zentrale Steuerungsgrösse.

### Sequenzbasierte Analyse

Einzelne Fehler sind weniger aussagekräftig als Muster. Das Lernland-System wertet Antwortsequenzen aus: Fünf richtige Antworten in Folge signalisieren Unterforderung und erhöhen die Schwierigkeit. Drei Fehler nacheinander deuten auf Überforderung hin und senken das Niveau.

### Voraussetzungs-Mapping

Mathematische Kompetenzen bauen aufeinander auf. Wer den Zehnerübergang nicht versteht, wird bei der Addition bis 100 scheitern. Lernland implementiert ein Voraussetzungs-Mapping nach [Lehrplan 21 App](</blog/mathe-app-lehrplan-21>). Zeigt ein Kind Schwächen, werden automatisch grundlegendere Aktivitäten priorisiert.

## Die technische Architektur von Lernland

Das adaptive System von Lernland basiert auf drei Kernkomponenten:

### 1\. Schwierigkeitsparameter pro Aktivität

Jede der über 50 Lernaktivitäten speichert einen individuellen Schwierigkeitswert zwischen 0 und 1. Dieser Wert bestimmt Faktoren wie Zahlenraum, Zeitdruck oder Komplexität der Darstellung. Der Wert wird nach jeder Antwort neu berechnet.

### 2\. Dynamische Freischaltung

Neue Aktivitäten werden nicht pauschal freigeschaltet, sondern nach einem dynamischen Schwellenwert. Bei hoher Genauigkeit (über 90%) genügen 10 korrekte Antworten in der Vorläuferaktivität. Bei niedrigerer Genauigkeit werden bis zu 25 richtige Antworten benötigt. Dies verhindert, dass Kinder zu schnell zu schwierigen Themen übergehen.

### 3\. Cold-Start-Algorithmus

Neue Nutzer stellen eine besondere Herausforderung dar. Lernland löst das Cold-Start-Problem durch Klassenstufen-Priorisierung. Ein Drittklässler beginnt nicht bei Kindergarten-Aufgaben, sondern bei altersgerechten Einstiegsaktivitäten. Das System sammelt dann schnell genug Daten für die individuelle Anpassung.

## Trainingsmodus: Personalisiertes Mixed Practice

Der Trainingsmodus von Lernland kombiniert multiple Aktivitäten in einer Session. Das System wählt automatisch aus, welche Übungen präsentiert werden. Die Auswahl basiert auf:

  * Aktivitäten mit Verbesserungspotenzial (Erfolgsrate unter 80%)
  * Aktivitäten, die seit längerem nicht geübt wurden
  * Voraussetzungs-Aktivitäten bei identifizierten Lücken
  * Aktivitäten kurz vor der nächsten Freischaltung

Dieses Prinzip des _Mixed Practice_ oder _Interleaving_ ist wissenschaftlich belegt effektiver als das isolierte Üben einzelner Themen.

## Fehleranalyse statt blosser Statistik

Lernland speichert nicht nur, ob eine Antwort richtig oder falsch war. Das System protokolliert die konkreten Fehler: Welche Aufgabe wurde gestellt? Was hat das Kind geantwortet? Was wäre korrekt gewesen?

Diese Daten ermöglichen Lehrpersonen und Fachpersonen präzise Diagnostik. Typische Fehlermuster werden sichtbar: Verwechselt das Kind Plus und Minus? Hat es Probleme mit dem Zehnerübergang in eine bestimmte Richtung? Solche Erkenntnisse sind Gold wert für die [heilpädagogische Förderplanung](<app-heilpaedagogik-if-unterricht.html>).

## Warum nicht alle Apps adaptiv sind

Echte Adaptivität erfordert erheblichen Entwicklungsaufwand. Die meisten Lern-Apps beschränken sich auf simple Schwierigkeitsstufen, die der Nutzer manuell wählt. Das ist einfacher zu implementieren, verfehlt aber den Kern personalisierten Lernens.

Lernland wurde von Grund auf für adaptive Förderung konzipiert. Der [Lehrplan 21 App](</blog/mathe-app-lehrplan-21>) mit seinen klar definierten Kompetenzstufen bietet dafür eine ideale Grundlage. Jede Aktivität ist einem Kompetenzbereich zugeordnet und in das Voraussetzungs-Mapping integriert.

## Offline-Adaptivität

Eine besondere technische Herausforderung ist Adaptivität ohne Internetverbindung. Viele Schulen haben eingeschränktes WLAN, Tablets werden auch zuhause ohne Netz genutzt. Lernland arbeitet nach dem Local-First-Prinzip: Alle Berechnungen erfolgen auf dem Gerät. Fortschritte werden lokal gespeichert und bei Verbindung synchronisiert.

Das bedeutet: Die [Offline-Funktionalität](<lernapp-ohne-internet.html>) umfasst auch die vollständige adaptive Anpassung, nicht nur statische Übungen.

## Fazit: Adaptives Lernen als Standard

Kinder lernen unterschiedlich schnell, haben verschiedene Stärken und Schwächen. Eine Lern-App, die sich nicht anpasst, wird diesem Grundprinzip nicht gerecht. Adaptive Systeme wie Lernland nutzen Technologie, um individuelle Förderung zu ermöglichen, die in grossen Klassen oft nicht leistbar ist.

Lernland passt die Schwierigkeit automatisch an das Leistungsniveau des Kindes an. Das System analysiert Antwortmuster, priorisiert Voraussetzungs-Aktivitäten und hält die Erfolgsrate im optimalen Bereich. Für Kinder mit [[Rechenschwäche mit Apps üben](</blog/rechenschwaeche-app-ueben>)](<rechenschwaeche-app-ueben.html>) oder besonderem Förderbedarf ist diese Anpassung besonders wertvoll.

**Lernland** ist eine adaptive Lern-App für Schweizer Primarschüler vom Kindergarten bis zur 6. Klasse. Die App basiert auf dem Lehrplan 21 und wurde speziell für Kinder mit heilpädagogischem Förderbedarf entwickelt.