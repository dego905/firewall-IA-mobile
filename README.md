# Firewall IA Móvil - Sin Nombre Security AI

Un firewall inteligente desarrollado en Bash y Python, con interfaz web profesional, capaz de detectar amenazas en tiempo real en dispositivos Android sin necesidad de root.

## Características

- Detección de amenazas con IA (Machine Learning)
- Análisis de conexiones en tiempo real (netstat + ps)
- Dashboard web con logs, métricas y reentrenamiento
- Funciona en Termux sin privilegios de superusuario
- Visualización profesional de tráfico y amenazas

## Estructura del Proyecto

- `monitor.sh` - Script principal del firewall
- `ai_detect.py` - Motor de inteligencia artificial
- `conn_raw.csv` - Base de datos dinámica de conexiones
- `decision.log` - Registro de acciones del firewall
- `app.py` - Servidor web Flask
- `templates/dashboard.html` - Interfaz web

## Requisitos

- Python 3
- Termux (para Android)
- Flask, pandas, scikit-learn
- Git (para clonar y subir)

## Uso

```bash
chmod +x monitor.sh
./monitor.sh &
python app.py
