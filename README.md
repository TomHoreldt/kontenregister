# Projektplan: Kontenregister

**Projekt:** Neugestaltung eines minimalen Staates 
**Team:** Kontenregister

---

## 1. Projektziel und Scope

Das Team baut das zentrale **Kontenregister** des Staates. Es verwaltet Konten und Transaktionen aller Akteure und ist die finanzielle Schnittstelle zu den drei anderen Registern.

**(Entwurf):**
- Kontoverwaltung (Eröffnen, Ändern, Schließen, Abfragen) für Bürger, Unternehmen und Staat
- Buchungen und Überweisungen zwischen Konten, Kontostand und Kontoauszug
- Einkommenszahlung (Unternehmen an Bürger) und Steuereinzug (Bürger/Unternehmen an Staat)
- Zahlungen des Staates an Unternehmen (Infrastruktur)
- Schnittstellen zu Personen-, Gewerbe- und Infrastrukturregister
- Protokollierung (Nachvollziehbarkeit für Kontrollorgane)

---

## 2. Work Packages, Tasks, Deliverables

| WP | Task | Beschreibung | Deliverable | Start | Ende |
|---|---|---|---|---|---|
| **WP1** | **Projektmanagement** | | | 26.10. | 29.01. |
| | 1.1 | Kick-off, Rollen, Kommunikationswege | Rollenübersicht | 23.10. | 23.10. |
| | 1.2 | Projektplan erstellen, GitHub-Repo aufsetzen | Dieser Plan, Repo | 23.10. | 23.10. |
| | 1.3 | Wöchentliche Team-Syncs, Plan pflegen | Protokolle, Plan-Updates | 02.11. | 29.01. |
| **WP2** | **Anforderungen & Abstimmung** | | | 28.10. | 13.11. |
| | 2.1 | Schnittstellen-Workshop mit den anderen Registern | Schnittstellenliste | 28.10. | 06.11. |
| | 2.2 | Klärung der offenen Fragen (Steuern, Maut, Gerichte, Gesetze) | Entscheidungsprotokoll | 28.10. | 13.11. |
| | 2.3 | Anforderungskatalog (funktional/nicht-funktional) | Anforderungskatalog | 02.11. | 13.11. |
| **WP3** | **Fachkonzept & Design** | | | 16.11. | 04.12. |
| | 3.1 | Datenmodell (Konto, Transaktion, Kontotyp, Steuerregel, Protokoll) | ER-Diagramm | 16.11. | 27.11. |
| | 3.2 | Prozessmodelle (Kontoeröffnung, Überweisung, Einkommen + Steuer, Staatszahlung, Sanktion) | Prozessdiagramme | 16.11. | 27.11. |
| | 3.3 | Architektur und API-Spezifikation | Architekturskizze, OpenAPI-Spec | 23.11. | 04.12. |
| **WP4** | **Implementierung** | | | 23.11. | 15.01. |
| | 4.1 | Tech-Stack festlegen, Entwicklungsumgebung, Datenbank, CI | Lauffähiges Grundgerüst | 23.11. | 04.12. |
| | 4.2 | Kontoverwaltung | Funktionierende Konto-API | 07.12. | 18.12. |
| | 4.3 | Transaktionen (Buchung, Überweisung, Saldo, Auszug) | Funktionierende Transaktions-API | 07.12. | 23.12. |
| | 4.4 | Staatsfunktionen (Steuereinzug, Zahlungen an Unternehmen, Sanktionen) | Steuer-/Staatsmodul | 14.12. | 08.01. |
| | 4.5 | Anbindung Personen-, Gewerbe-, Infrastrukturregister | Funktionierende Schnittstellen | 04.01. | 15.01. |
| **WP5** | **Test & Integration** | | | 07.12. | 22.01. |
| | 5.1 | Komponententests (begleitend zur Entwicklung) | Testfälle, Testbericht | 07.12. | 15.01. |
| | 5.2 | Integrationstest mit allen Registern | Integrationstestbericht | 11.01. | 22.01. |
| | 5.3 | Fehlerbehebung | Stabiler Release | 18.01. | 26.01. |
| **WP6** | **Dokumentation & Abschluss** | | | 02.11. | 29.01. |
| | 6.1 | Laufende Dokumentation (README, API-Doku, Entscheidungen) | Doku im Repo | 02.11. | 22.01. |
| | 6.2 | Abschlussdokumentation und Präsentation | Abschlussbericht, Präsentation | 18.01. | 29.01. |

---

## 3. Meilensteine

| ID | Meilenstein | Datum | Kriterium |
|---|---|---|---|
| M0 | Projektplan veröffentlicht | 23.10.2026 | Plan und Repo auf GitHub |
| M1 | Anforderungen freigegeben | 06.11.2026 | Anforderungskatalog und Schnittstellenliste mit allen Teams abgestimmt |
| M2 | Design freigegeben | 20.11.2026 | Datenmodell, Prozesse und API-Spezifikation abgenommen |
| M3 | MVP lauffähig | 08.01.2027 | Konten, Transaktionen und Steuerlogik funktionieren isoliert |
| M4 | Integration abgeschlossen | 22.01.2027 | Zusammenspiel mit allen Registern getestet |
| M5 | Abgabe / Präsentation | 29.01.2027 | Code, Dokumentation und Präsentation fertig |

---

## 4. Abhängigkeiten

- **WP3 → WP4:** Implementierung startet erst nach freigegebenem Datenmodell und API-Spezifikation (Ausnahme: Grundgerüst 4.1).
- **Kontenregister ← Personen-/Gewerberegister:** Konten benötigen eindeutige IDs von Bürgern und Unternehmen.
- **Kontenregister ← Infrastrukturregister:** Zahlungsempfänger und Zahlungsanlässe (Bauaufträge, ggf. Maut).
- **Steuerlogik ← Entscheidung zur Besteuerung** (siehe Abschnitt 2); bis M1 klären.

---

## 5. Rollen 

| Rolle | Verantwortlich |
|---|---|
| Product Owner | Jan_Diedrich |
| Scrum Master | Tom_Horeldt|
| Developers | Tobias_Berndt & Emirhan_Gülec |
