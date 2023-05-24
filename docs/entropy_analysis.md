# Entropie Analysen

## Berechnung der Entropie

1) Analyse der Datei (oder von Blöcken dieser) Byte für Byte
2) Zählen der Vorkommnisse aller möglichen Bytes
3) [Berechnung der Entropie](https://welt-der-bwl.de/Entropie) für gesamte Datei oder Bereiche der Datei (Wertebereich
   0-1)
4) Bei Blöcken: Größe von mindestens 4096 Bytes (aussagekräftig)

> Ideen
> - Häufigkeitsanalyse von Nibbles oder Byte-Tupeln statt einzelnen Bytes
> - Anpassung der Block-Größe für detaillierte Dateianalysen

## Häufigkeiten der Bytes (gesamte Datei)

### Zufällige Binärdaten

![Entropie Zufallsdaten](entropy_graphs_overall/random.png)

- Sehr hohe Entropie

### UTF-8-Text

![Entropie UTF-8](entropy_graphs_overall/utf8.png)

- Viele 0x20 Bytes (Space)
- Viele Buchstaben-Bytes (ASCII)

### Ausführbare Datei

![Entropie Sysinternals Process Explorer](entropy_graphs_overall/binary.png)

- Viele 0x00 Bytes

### ZIP

![Entropie ZIP](entropy_graphs_overall/zip_compressed.png)

- Sehr hohe Entropie

### Verschlüsseltes ZIP

![Entropie verschlüsseltes ZIP](entropy_graphs_overall/zip_compressed_encrypted.png)

- Sehr hohe Entropie

## Entropie von Dateibereichen (Blöcke von 4096 Bytes)

### Zufällige Binärdaten

![Entropie Zufallsdaten](entropy_graphs_blocks/random.png)

- Keine Entropie-Schwankungen
- Durchgehend sehr hohe Entropie

### UTF-8-Text

![Entropie UTF-8](entropy_graphs_blocks/utf8.png)

- Keine Entropie-Schwankungen
- Durchgehend geringe Entropie

### Ausführbare Datei

![Entropie Sysinternals Process Explorer](entropy_graphs_blocks/binary.png)

- Starke Entropie-Schwankungen innerhalb der Datei
- Verschiedene Bereiche einer Executable haben unterschiedliche Entropie

### ZIP

![Entropie ZIP](entropy_graphs_blocks/zip_compressed.png)

- Kaum Entropies-Schwankungen (woher kommen kleine Schwankungen?)
- Durchgehend sehr hohe Entropie

### Verschlüsseltes ZIP

![Entropie verschlüsseltes ZIP](entropy_graphs_blocks/zip_compressed_encrypted.png)

- Keine Entropies-Schwankungen
- Durchgehend sehr hohe Entropie
