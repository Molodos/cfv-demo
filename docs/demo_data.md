# Demo Daten

Im Folgenden wird erläutert, wie die Demo-Daten aufgebaut sind und warum die entsprechenden Konstellationen sinnvoll
sind

## Basis-Daten

Die folgenden Basis-Daten wurde ausgewählt, um daraus einige Test-Datensätze zu erstellen

### /demo_data/example_data/exiftool.exe

Es wurde ein Binary ausgewählt, da bei diesen hohe Entropieschwankungen innerhalb der Datei auftreten, und es interesant ist, ob diese Schwankungen noch nach der Komprimierung sichtbar sind.

### /demo_data/example_data/garden.dng

Es wurden ein Bild im RAW Format ausgewählt, da diese im Gegensatz zu Bildern im PNG oder JPG Format einen höheren Anteil an Metadaten und damit ein anderes Verhältnis von Text zu Pixelinformationen enthalten. Des Weiteren
werden häufig Bilder verschickt, sodass eine Betrachtung des Formats in diesem Kontext sinnvoll ist.

### /demo_data/example_data/random_data.bin

Es wurden zufällige Binärdaten ausgewählt, da diese eine sehr hohe Entropie aufweisen und damit die Frage beantwortet werden kann, wie sich diese aus eine Komprimierung auswirkt.

### /demo_data/example_data/rfc_793_4.txt

Es wurden ASCII Textdaten ausgewählt, da diese eine geringe Entropie aufweisen und sich dadurch gut komprimieren lassen. Des Weiteren wird viel Text verschickt, sodass diese Datenart in der Praxis sehr relevant ist.
Um ein realistisches Datenset zu bekommen, wurde die RFC Spezifikation von TCP verwendet und, um die Datengröße zu erhöhen, vier mal in das Dokument kopiert. Durch die Wiederholung wird die Entropie weiter verringert,
was aber für unsere Betrachtung vernachlässigt werden kann.

## Demo-Daten

Die folgenden Demo-Daten wurden mit 7-Zip aus den oben erläuterten Basis-Daten zusammengesetzt. Als Kompressionsverfahren wurde dabei Deflate mit den Standard Parametern für die Wortgröße (32), die Wörterbuchgröße (32KB) 
sowie die Kompressionstärke (Stufe 5 - normal) verwendet, außer es ist, wie bei Datensatz 4, anders spezifiziert. 

### Übersicht über die Demo Datensätze

| ID | Quellbetriebsbsystem | Verschlüsselung & Passwort| Filetypes | sonstige Parameter |
| -- | -- | -- | -- | -- |
| 1 | Ubuntu | ZipCrypto - '1sfaches pw' | RAW, ASCII | kompletter Pfad |
| 2 | Windows | AES256 - 'sicheres Passwort' | EXE, ASCII | Änderungs- und Erstellungszeitstempel |
| 3 | Windows | ZipCrypto - 'pwt\#123!' | BIN, ASCII | -/- |
| 4 | Windows | ZipCrypto - '123\#pwd!' | ASCII | Stufe 0 - speichern
| 5 | Windows | AES256 - 'pwt\#123!' | EXE | -/- |
| 6 | Ubuntu | AES256 - 's3cure pwd' | BIN | -/- |
