# Programm zum erzeugen von lustigen Namen
# aus zwei Listen mit Vornamen und Nachnamen,
# die zufällig miteinander kombiniert werden.

# Erste Aufgabe aus dem Buch
# "Impractical Python Projects"

import sys, random

wort1 = ['innige', 'mannhafte', 'freudige', 'abendländische', 'machtvolle', 'diese unsere', 'fanatische', 'unerschütterliche', 'erhabene', 'tiefe', 'funktionale', 'integrierte', 'kreative', 'permanente', 'echte', 'konstruktive', 'emanzipatorische', 'ambivalente', 'qualifizierte', 'systematisierte']

wort2 = ['Zukunfts', 'Schicksals', 'Vergangenheits', 'Geistes', 'Gewissens', 'Bildungs', 'Kultur', 'Erinnerungs', 'Seins', 'Wesens', 'Aktions', 'Identifikations', 'Kommunikations', 'Interpretations', 'Organisations', 'Fluktuations', 'Beziehungs', 'Innovations', 'Koalitions', 'Motivations']

wort3 = ['Bewältigung', 'Ergriffenheit', 'Gläubigkeit', 'Verstrickung', 'Gewissheit', 'Verpflichtung', 'Erhellung', 'Aussage', 'Besinnung', 'Verantwortung', 'Potenz', 'Flexibilität', 'Akzeleration', 'Problematik', 'Tendenz', 'Konzeption', 'Präferenz', 'Struktur', 'Relevanz', 'Phase']

for i in range(1,11):
    auswahl_wort1 = random.choice(wort1)
    auswahl_wort2 = random.choice(wort2)
    auswahl_wort3 = random.choice(wort3)

    print(str(i) + ". " + auswahl_wort1 + " " + auswahl_wort2 + "-" + auswahl_wort3 + "\n")


