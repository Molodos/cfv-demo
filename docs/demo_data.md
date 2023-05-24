# Demo Daten

## Basis-Daten

### Zufälligen binären Daten

#### Generierung

```shell
head -c 1M /dev/urandom > random.bin
```

### UTF-8-Text

#### Generierung

Nutzung von [CyberChef](https://gchq.github.io/CyberChef/#recipe=Generate_Lorem_Ipsum(1048576,'Bytes')) (lädt kurz, bis
sich Output befüllt) und Download des Ergebnisses als Datei

### Ausführbare Datei

Nutzung der Sysinternals Process Explorer exe (Version 16.43)

## Komprimierte Dateien

### Inhalt

> In dieser Reihenfolge.\
> Kann unter Linux mit `binwalk <datei>` überprüft werden (liefert auch Start-Bytes der einzelnen Dateien)

- binary.exe
- random.bin
- utf8.txt

### ZIP-Daten

> Dateinamen können im Gegensatz zu z.B. RAR nicht verschlüsselt werden

#### Generelle Optionen

- Verwendung von WinRAR
- Komprimierungsmethode: Normal (default)
- Wörterbuchgröße: 32kB (default)

#### Varianten

- `compressed.zip`
    - Kein Passwort
- `compressed_encrypted.zip`
    - Passwortgeschützt mit Passwort "password"
