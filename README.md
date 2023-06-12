# CFV Demo

Demos zur Studienarbeit mit dem Thema "Informationsgewinnung aus verschlüsselten Archiv-Dateien und deren Auswertung im
Bezug auf die forensische Untersuchung"

## Benutzung

### Docker-Compose

1) Start der Applikation
   ```shell
   docker-compose up -d
   ```

2) Aufruf der Web-App über http://localhost:8080

### Manuell

1) Installation von Abhängigkeiten:
    ```shell
    pip install -r requirements.txt
    ```
2) Start der Applikation:
    ```shell
    python -m cfv_demo
    ```
3) Aufruf der Web-App über http://localhost:8080

## [Demo Daten](./docs/demo_data.md)

## [Demos der Präsentation](docs/presentation/presentation_demos.md)
