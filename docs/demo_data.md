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

- binary.exe
- random.bin
- utf8.txt

### ZIP

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
- `compressed_encrypted_old.zip`
    - Passwortgeschützt mit Passwort "password"
    - Option "Alte ZIP-2.0-Verschlüsselung"

### GZip/7Zip

#### Generelle Optionen

> TODO

#### Varianten

> TODO