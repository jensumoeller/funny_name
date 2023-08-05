# Programm zum erzeugen von lustigen Phrasen
# aus drei Wortlisten
# die zufällig miteinander kombiniert werden.

# Python-Umsetzung der "Phrasen-Dreschmaschine"
# aus der Straelener Manuskripte Verlags-GmbH

import sys, random, time

wort1 = ['innige', 'mannhafte', 'freudige', 'abendländische', 'machtvolle', 'diese unsere', 'fanatische', 'unerschütterliche', 'erhabene', 'tiefe', 'funktionale', 'integrierte', 'kreative', 'permanente', 'echte', 'konstruktive', 'emanzipatorische', 'ambivalente', 'qualifizierte', 'systematisierte']

wort2 = ['Zukunfts', 'Schicksals', 'Vergangenheits', 'Geistes', 'Gewissens', 'Bildungs', 'Kultur', 'Erinnerungs', 'Seins', 'Wesens', 'Aktions', 'Identifikations', 'Kommunikations', 'Interpretations', 'Organisations', 'Fluktuations', 'Beziehungs', 'Innovations', 'Koalitions', 'Motivations']

wort3 = ['Bewältigung', 'Ergriffenheit', 'Gläubigkeit', 'Verstrickung', 'Gewissheit', 'Verpflichtung', 'Erhellung', 'Aussage', 'Besinnung', 'Verantwortung', 'Potenz', 'Flexibilität', 'Akzeleration', 'Problematik', 'Tendenz', 'Konzeption', 'Präferenz', 'Struktur', 'Relevanz', 'Phase']

auswahl_1 = random.sample(wort1, k=10)
auswahl_2 = random.sample(wort2, k=10)
auswahl_3 = random.sample(wort3, k=10)


for i in range(10):

    print(str(i+1) + ". " + auswahl_1[i] + " " + auswahl_2[i] + "-" + auswahl_3[i] + "\n")

