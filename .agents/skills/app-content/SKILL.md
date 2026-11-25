---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Werkzeuge für Wörter“: Explainer (Strang-App `englisch/wortschatz`, Format 2, Sprache Deutsch, englische Beispiele, britisches Englisch). Auftrag: Issue lernapps/apps#485 (Epic lernapps/apps#489, Konventionen dort). Gebaut sind beide Kapitel: Kapitel 1 (Stufe 7-8) und Kapitel 2 (Stufe 9-10).

## Curriculum

Englisch als erste Fremdsprache, Stufe 7-8 (Kapitel 1) und 9-10 (Kapitel 2). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`, Strang `wortschatz`). Nicht hier: Wortfelder (Situations-Explainer), die Fachbegriffe noun und verb (#470), Lautschrift (#482).

## Competencies

Alle fünf sind Lücken der Karte. Eine Seite je Baustein, Ordnung nach `requires`.

1. Kapitel `wenn-ein-wort-fehlt` („Wenn mir ein Wort fehlt“, Stufe 7-8)
   - Wiederholung `recap: [englisch/relativsaetze, englisch/grammatik-fachbegriffe]` → `das-brauchst-du` (ohne Übung, ohne `competencies`)
   - `umschreiben` → `umschreiben` (Musterseite): „Ich kann ein Wort, das mir fehlt, mit anderen Wörtern, Synonymen oder Gegenteilen umschreiben.“
   - `wortfamilien` → `wortfamilien`: „Ich kann Wörter einer Wortfamilie erkennen und mit Vor- und Nachsilben neue Wörter erschließen (help, helpful, helpless).“
2. Kapitel `englisch-und-deutsch` („Englisch und Deutsch vergleichen“, Stufe 9-10)
   - Wiederholung `recap: englisch/praepositionen-ort` → `das-brauchst-du`
   - `phrasal-verbs` → `phrasal-verbs`: „Ich kann häufige phrasal verbs wie give up, look after und find out verstehen und verwenden.“
   - `false-friends` → `false-friends`: „Ich kann typische false friends wie become, chef und sensible richtig verwenden.“
   - `sprachvergleich` → `sprachvergleich`: „Ich kann Englisch und Deutsch vergleichen und typische Unterschiede in Wortbildung, Wortstellung und Ausdruck erklären.“

Die „Ich kann“-Sätze stehen wie in der Karte (nicht umformulieren). Übungs-IDs: Präfix = Seite (`umschreiben-relativsatz`).

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Gebaut: Kapitel 1: `das-brauchst-du`, `umschreiben` (Musterseite), `wortfamilien`; Kapitel 2: `das-brauchst-du`, `phrasal-verbs`, `false-friends`, `sprachvergleich`. Je Kapitel eine Selbsteinschätzung (3 Übungen je Seite, in `chapter.yaml`). Je Seite 6 bis 8 Übungen, 12 bis 18 Items.
- Rahmen: Der Werkzeugkoffer. Jede Seite stellt ein Werkzeug als Karte „Was tun, wenn …?“ vor (Tabelle „Klassenzimmer-Poster · Werkzeugkarte …“, drei kurze Schritte) mit Merke-Kasten.
- Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Lesestück, erste leichte Aufgabe, „Das kannst du danach“), `werkzeug` (Karte, Merke, Wörter im Vokabelblock), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`open-task`), `weiter` (nächster Schritt; am Kapitelende ein Rückblick). Titel sagen, was der Abschnitt tut. Wiederholungsseite: nur Text und Tabelle.
- Lesestück: Kapitel 1 ein Chat (Text, Randglossar), etwa 150 bis 300 Wörter, höchstens eins je Seite; Kapitel 2 ein sachlicher Fall mit Daten und Quelle, keine erfundenen Kinder, Sophie nur als Name der Nutzerin. Die Lesestücke zählen nicht zu den 350 Wörtern Erklärtext.
- Länge: höchstens 350 Wörter Erklärtext, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken, höchstens etwa 25 Items und 10 Übungen je Seite.
- Lesestücke: `umschreiben` und `wortfamilien` ein Chat (Sophie, Ellie, Amir, Mr Hill, Mrs Parker nur genannt); `phrasal-verbs` ein Infoblatt für Gastschüler; `false-friends` eine Café-Mail mit Programm-Übersetzung (deutsches Original, englische Übersetzung, eine Zeile stimmt); `sprachvergleich` ein kurzer Sachtext mit Quellen. Alle Texte sind eigene, nach Fakten (siehe Sources).
- Keine Figuren-Einführung im Seitentext: keine Altersangaben, keine Familie, kein Datum; die Startseite nennt nur Namen und Rollen (Sophie, Ellie, Amir, Mr Hill, Mrs Parker, Peter).
- Anrede „du“.

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, sentence.
- Immer gleich: **Werkzeugkoffer**, **Werkzeugkarte** („Was tun, wenn …?“), **Umschreiben**, **Wortfamilie**, **Stamm**, **Vorsilbe** (prefix), **Nachsilbe** (suffix), **Teilchen** (bei phrasal verbs), **Warnschild** (false friends), **Vergleichsregel**.
- Britisches Englisch. Englische Aufgaben enthalten kein deutsches Wort; die deutsche Vorgabe steht in `source`. Neue englische Wörter mit deutscher Bedeutung im Vokabelblock.
- Aussprache: keine Lautschrift (gehört zu #482); kein Audio in dieser App.

## Exercise patterns

Aufbau leicht → schwer: wählen/zuordnen → Lücke → schreiben mit Cue → übersetzen/frei. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten mit `(a|b)`.

- Umschreiben ableiten: `language-task` mode `choice` (Beschreibung → Wort) und `write` (Relativsatz bilden).
- Zerlegen und bilden: mode `table` (Stamm, Silbe, Bedeutung), `gap`, `matching` Silbe ↔ Bedeutung.
- Teilchen zuordnen: mode `choice`, `ordering`, `write`.
- Warnschild: `single-choice` mit Fall, mode `write` in beide Richtungen.
- Regel ableiten: `single-choice` mit Begründung, `open-task` für die eigene Vergleichsregel.
- Distraktoren nur echte Lernerfehler, je Fehler eine eigene Meldung.
- Keine Komponente (`prefer-built-in-block`); keine Datendateien: jede Tatsache steht einmal in ihrer Seite.

## Figures

- Eigene Zeichnungen, `CC-BY-4.0`, Quelle „eigene Zeichnung“, `src/images/`, erzeugt vom Skript `.agents/skills/app-content/scripts/make_images.py` (nie die SVG von Hand ändern): `werkzeugkoffer-1` bis `werkzeugkoffer-5` (der Koffer füllt sich von Seite zu Seite: umschreiben 1, phrasal-verbs 3, false-friends 4, sprachvergleich 5; `wortfamilien` hat stattdessen `wortfamilie.svg`: Stamm help grün, Silben ful und less orange). `alt` sagt, was das Bild zeigt, nie die Lösung. Schrift mindestens 16 im 480er viewBox.
- Poster sind `table`-Blöcke: „Klassenzimmer-Poster · Werkzeugkarte …“. Wörter stehen im Vokabelblock der Seite, nicht in einer Tabelle.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2). Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA), geöffnet am 2026-11-24: `False friend` (Definition, gift/Gift), `English phrasal verbs` (Verb plus Teilchen, Sinn nicht aus den Teilen ableitbar, Pronomen steht vor dem Teilchen: hand it in), `Affix` (Vor- und Nachsilben, Stamm), `V2 word order` (Deutsch: Verb an zweiter Stelle im Hauptsatz, am Ende im Nebensatz; Englisch überwiegend Subjekt-Verb-Objekt), `Compound (linguistics)` (Zusammensetzungen). Nicht geprüft und weggelassen: Häufigkeit einzelner phrasal verbs. Wörter außerhalb von A1/A2 stehen unten, wenn die Seiten gebaut sind. Beispielsätze sind eigene. Material der Ersteller:in: keines.

### Wörter außerhalb des Grundwortschatzes

Jedes steht auf der Seite mit Bedeutung (Vokabelblock, Merke oder Rückmeldung der Übung):
- `umschreiben`: rubber (Radiergummi, britisch), caretaker (Hausmeister), pencil (A2).
- `wortfamilien`: careless (Vokabelblock), hopeless, homeless, hopeful (abgeleitet aus Stamm und Silbe, in den Rückmeldungen erklärt), colourful, helpful, useful, useless (A2 der Liste).
- `phrasal-verbs`: host family, fill in, hand in, set off (Vokabelblock); die Verben give up, look after, find out, take off, pick up, turn off, put on, stand up, grow up, sit down, put away (Karte, Zuordnung und Rückmeldungen).
- `false-friends`: become, chef, sensible, eventually, actual, gift (Vokabelblock „Warnschilder“), current, poison, sensitive, boss (Warnschild-Spalte), eventual (nur als Distraktor mit Meldung).
- `sprachvergleich`: main clause, subordinate clause, compound (Vokabelblock), closed compound, Germanic (im Sachtext), homework, school bus (Übung), thirsty (A1).

## Adding a chapter or round

1. Baustein auf der Karte wählen; Voraussetzungen auf früheren Seiten oder auf einer Wiederholungsseite.
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `werkzeug`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` eintragen, Competency-ID setzen.
3. Werkzeugkarte als Poster-Tabelle, Übungen aus den Mustern, je mit `mistakes` und `hint`; 1 bis 3 ihrer Übungen in `selfAssessment` aufnehmen, wie Skill `lernapps-explainer-self-assessment` sagt.
4. Wörter gegen den Grundwortschatz prüfen und hier listen; Hörsätze gibt es nicht.
5. `npx --no -- lernapps check`; committen.

## Rules learned from mistakes

Aus dem Lerner-Check der Musterseite `umschreiben`:
- Eine Karte, die mehrere Wege kennt, nennt sie „Weg A“ und „Weg B“, nicht „Schritt 1, 2, 3“ (Schritte sind eine Reihenfolge).
- Auswahlaufgaben: die richtige Antwort steht nicht immer an erster Stelle und ist nicht immer die längste.
- Englisch im Chat mit Kurzformen (don't), kein Wort außerhalb von A1/A2 ohne Erklärung; vor der ersten Aufgabe steht „Das kannst du danach“.
- Übungen vom Leichten zum Schweren: Ordnen vor Übersetzen; bei `write` gleichwertige Antworten als `(a|b)` und `(you use to cut|cuts)` zulassen.
- Das Koffer-Bild lässt unter dem Koffer Platz, damit die Lizenzplakette kein Fach verdeckt.

Aus der Reihe (Konventionen lernapps/apps#489, Abschnitte 7 und 8):
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen; eine Tabelle, die eine Übung beantwortet, steht nicht direkt darüber.
- Poster, Merke, Einstieg und Bild nennen andere Beispiele als die Übungen darunter (keine Lösung im Text darüber).
- Als Auswahl nur echte Lernerfehler, keine Unwörter; jeder Distraktor und jedes typische Fehlerbild eine eigene Meldung; ein Einstiegs-`single-choice` hat mindestens drei Optionen.
- Mit `(a|b)` gleichwertige richtige Antworten zulassen.
- Menschen sind keine „Dinge“; Beziehungen haben keinen „Besitzer“.
- Keine Figuren-Einführung im Seitentext; Aussagen ohne geöffnete Quelle weglassen.
