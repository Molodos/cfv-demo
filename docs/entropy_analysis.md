# Entropie Analysen

## Berechnung der Entropie

1) Analyse der Datei (oder von Blöcken dieser) Byte für Byte
2) Zählen der Vorkommnisse aller möglichen Bytes
3) [Berechnung der Entropie](https://welt-der-bwl.de/Entropie) für gesamte Datei oder Bereiche der Datei (Wertebereich
   0-1)

> Ideen
> - Häufigkeitsanalyse von Nibbles oder Byte-Tupeln statt einzelnen Bytes
> - Anpassung der Block-Größe für detaillierte Dateianalysen

## Häufigkeiten der Bytes (gesamte Datei)

### Zufällige Binärdaten

![Entropie Zufallsdaten](entropy_graphs_overall/random.png)

### UTF-8-Text

![Entropie UTF-8](entropy_graphs_overall/utf8.png)

### Ausführbare Datei

![Entropie Sysinternals Process Explorer](entropy_graphs_overall/binary.png)

### ZIP

![Entropie ZIP](entropy_graphs_overall/zip_compressed.png)

### Verschlüsseltes ZIP

![Entropie verschlüsseltes ZIP](entropy_graphs_overall/zip_compressed_encrypted.png)

### Verschlüsseltes ZIP (Alt)

![Entropie verschlüsseltes ZIP (Alt)](entropy_graphs_overall/zip_compressed_encrypted_old.png)


## Entropie von Dateibereichen (Blöcke von 4096 Bytes)

> TODO
