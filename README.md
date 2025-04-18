# Firewall IA Móvil

Proyecto de ciberseguridad avanzado que combina Bash y Python para crear un firewall inteligente, funcional desde Termux en dispositivos Android, sin necesidad de acceso root.

## Características

- **Detección en tiempo real** de conexiones activas.
- **Análisis inteligente** con aprendizaje automático (IA).
- **Bloqueo automático** de procesos maliciosos.
- **Geolocalización básica de IPs.**
- **Alertas activas** mediante vibración y notificaciones en Termux.
- **Sistema autoentrenable** que mejora con el tiempo.

## Tecnologías

- **Bash** para el monitoreo del sistema.
- **Python** con `scikit-learn`, `pandas` y `numpy` para análisis IA.
- **Termux API** para vibración, sonido y notificaciones.

## Instalación

```bash
pkg install git python net-tools termux-api
pip install pandas scikit-learn numpy
git clone https://github.com/dego905/firewall-IA-mobile.git
cd firewall-IA-mobile
chmod +x monitor.sh
