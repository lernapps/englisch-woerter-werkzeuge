---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: explore
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Plan: englisch-woerter-werkzeuge, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-24. Explore, Plan, Code, Commit.*

## Goal

Die Lernenden bauen sich einen Werkzeugkoffer für Wörter: Sie umschreiben ein fehlendes Wort, erschließen ein unbekanntes über seine Wortfamilie, verstehen phrasal verbs, erkennen false friends und vergleichen Englisch mit Deutsch (Issue lernapps/apps#485).

## Key decisions

- Archetype `explainer`: Seiten mit Lesestück, Erklärung und Übungen, Sprachaufgaben (`language-task`). Kein Spiel, keine Zeitmessung nötig.
- Strang-App `englisch/wortschatz`, Format 2, Sprache der Seiten Deutsch, Beispiele britisches Englisch.
- Kein Audio: das Issue verlangt keines (Konventionen 5).
- Kapitel 2 (Stufe 9-10): realistischer Fall mit Quellen statt erfundener Kinder; Sophie nur als Name der Nutzerin im Fall (guess, im Checkpoint gefragt).

## Notes

- Strang `englisch/wortschatz`, Karte `https://lernapps.net/apps/map/englisch.json` (geöffnet).
- Kapitel 1 · Wenn mir ein Wort fehlt (7-8): `umschreiben` (requires `relativsaetze`), `wortfamilien` (requires `grammatik-fachbegriffe`). Beide ohne Übung in einer App (Lücke).
- Kapitel 2 · Englisch und Deutsch vergleichen (9-10): `phrasal-verbs` (requires `praepositionen-ort`), `false-friends`, `sprachvergleich` (requires `phrasal-verbs`, `false-friends`).
- Wiederholung: Kapitel 1 Sammel-Wiederholung `relativsaetze` (englisch-saetze-verbinden) und `grammatik-fachbegriffe` (hello-millbrook); Kapitel 2 Wiederholung `praepositionen-ort` (englisch-dinge-mengen-orte).
- Didaktik: Der Werkzeugkoffer wächst. Jede Seite stellt ein Werkzeug als Karte „Was tun, wenn …?“ mit kurzem Vorgehen vor; Lesestück (Chat, Stufe 7-8; Sachfall, Stufe 9-10), Übungen an echten Stolpersteinen.
- Umfang: 2 Kapitel, 5 Seiten Inhalt plus 2 Wiederholungsseiten, je Seite höchstens etwa 25 Items. Ausgeschlossen: Wortfelder (Situations-Explainer), Lautschrift (#482), Fachbegriffe noun und verb (#470).
- Quellen (nur Fakten, geöffnet am 2026-11-24): en.wikipedia.org „False friend“ (Definition, gift/Gift, Herkunft des Begriffs), „English phrasal verbs“ (Verb plus Teilchen, Sinn nicht aus den Teilen ableitbar, Stellung des Pronomens), „Affix“ (Vor- und Nachsilben). Keine Sätze übernommen. Nicht geprüft: Häufigkeit einzelner phrasal verbs.
- Wie sie dorthin kommen (Fehlbild, das die Rückmeldung fängt):
  - `umschreiben`: Sie leiten aus einer Beschreibung (a person who …) das Wort ab und bauen selbst einen Relativsatz; Fehlbild: das Wort nennen statt es zu umschreiben, who/which vertauschen.
  - `wortfamilien`: Sie trennen Wörter in Stamm und Silben und bilden Wörter mit -ful/-less/un-/-er; Fehlbild: Stamm nicht erkannt, Bedeutung der Silbe vertauscht (helpful ≠ helpless).
  - `phrasal-verbs`: Sie ordnen Verb plus Teilchen einem Sinn zu und setzen das Pronomen an die richtige Stelle; Fehlbild: wörtliche Übersetzung des Verbs, Teilchen weggelassen, pick up it.
  - `false-friends`: Sie entscheiden am Warnschild, welche Bedeutung gilt, und wählen das richtige englische Wort; Fehlbild: become = bekommen, chef = Chef.
  - `sprachvergleich`: Sie sammeln aus Beispielen eigene Vergleichsregeln (Wortbildung, Wortstellung, Ausdruck) und prüfen sie; Fehlbild: Regel aus dem Deutschen übertragen.
- Umfang und Daten: Beispiele nur mit Wörtern aus A1/A2 oder auf der Seite erklärt; Sprachen de (Seiten) und en (Beispiele). Keine Auslassung ohne Nennung: Verben mit Teilchen nur die häufigsten (give up, look after, find out, turn on/off, pick up, put on); false friends: become, gift, chef, sensible, actual, eventually, art.
- Seiten und Kapitel (Dateien `<kapitel>/<seite>`):
  - Kapitel `wenn-ein-wort-fehlt` (7-8): `das-brauchst-du` (recap: `relativsaetze`, `grammatik-fachbegriffe`) · `umschreiben` (`umschreiben`) · `wortfamilien` (`wortfamilien`). Nicht geübt in der App: relativsaetze (englisch-saetze-verbinden), grammatik-fachbegriffe (hello-millbrook).
  - Kapitel `englisch-und-deutsch` (9-10): `das-brauchst-du` (recap: `praepositionen-ort`) · `phrasal-verbs` · `false-friends` · `sprachvergleich`. Nicht geübt in der App: praepositionen-ort (englisch-dinge-mengen-orte).
- Rückfrage an die Orchestrator-Session: (1) Darf Sophie (15 bis 16) in Kapitel 2 als Nutzerin des Falls vorkommen, oder ganz sachlich ohne Figur? (2) Reicht „Kein Audio“?
- Wörter: Grundwortschatz A1/A2 der Karte; Wörter darüber werden auf der Seite erklärt und im Inhaltsführer gelistet.

## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [ ] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

Die Antworten stehen im Auftrag (Issue lernapps/apps#485) und in der Startnachricht der Orchestrator-Session (in der Rolle der Ersteller:in); keine eigene Rückfrage nötig.

- Goal: Ich weiß, was ich tun kann, wenn mir ein Wort fehlt oder ich eines nicht kenne, und wo Englisch und Deutsch sich ähnlich oder täuschend verschieden sind (Issue, Leitidee).
- Learners: Englisch, Stufe 7-8 (Kapitel 1) und 9-10 (Kapitel 2); Sophie ist die Hauptfigur.
- Model and focus: die fertigen Vorgänger englisch-pronomen, englisch-klang-schrift, englisch-adjektive-adverbien; Schwerpunkt Lesestück und Werkzeugkarten.
- Hurdles: Wörter wörtlich übersetzen (false friends), Teilchen weglassen oder falsch deuten (phrasal verbs), Silben nicht abtrennen (Issue: Stolpersteine aus Texten).
- Content: von mir aus Fakten mit geöffneten Quellen, keine fremden Sätze.
- Amount: ganzer Explainer, beide Kapitel, 5 Bausteine; klein, kein Auffüllen.
- Languages: Deutsch (Erklärung), britisches Englisch (Beispiele).
- Look and feel: fixed by the archetype (ruhig wie ein Arbeitsblatt, Dunkelmodus folgt dem Gerät).
- Terms: Werkzeugkoffer, Werkzeugkarte „Was tun, wenn …?“, Teilchen (phrasal verbs), Warnschild (false friends), Wortfamilie, Stamm.
- Finding the app: Wortschatz Englisch, Wörter umschreiben, phrasal verbs, false friends.

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [ ] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [ ] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [ ] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [ ] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [ ] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [ ] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [ ] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [ ] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [ ] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [ ] Load skill `lernapps-explainer`.
- [ ] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [ ] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
<!-- tasks: pattern: the one page or screen that is the pattern for the others -->
- [ ] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
<!-- tasks: pages: the other pages or screens, after the pattern -->
- [ ] Update the content guide so that it describes the app as built (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
