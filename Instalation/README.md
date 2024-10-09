# Componentes necesarios para instalar Raspberry Pi OS (Raspbian)🫐

## 1. Hardware 🖥️

### Raspberry Pi 🥧

- **Modelo de Raspberry Pi**: Puede ser cualquier modelo compatible como Raspberry Pi 4, Raspberry Pi 3, Raspberry Pi Zero, etc.

### Tarjeta microSD (o SD) 💾

- **Capacidad mínima**: 8 GB (Recomendado 16 GB o más)
- **Clase**: Clase 10 o superior para mejor rendimiento
- **Compatibilidad**: Asegúrate de que la tarjeta sea compatible con el modelo de Raspberry Pi

### Fuente de alimentación 🔌

- **Voltaje y amperaje**:
  - Raspberry Pi 4: 5V 3A
  - Raspberry Pi 3 y anteriores: 5V 2.5A
- **Conector**: USB-C para Raspberry Pi 4, Micro-USB para modelos anteriores

### Monitor 🖥️

- **Interfaz**: HDMI o microHDMI (dependiendo del modelo de Raspberry Pi)

### Cable HDMI 📺

- **Tipo de cable**: HDMI a HDMI, o microHDMI a HDMI (para Pi 4)

### Teclado y ratón ⌨️🖱️

- **Conexión**: USB o Bluetooth (si tienes un dongle USB)

### Opcional: Carcasa 🛡️

- Para proteger tu Raspberry Pi de daños físicos.

### Opcional: Disipadores de calor ❄️

- Para mejorar el enfriamiento en uso prolongado.

---

## 2. Software 💻

### Raspberry Pi Imager (O cualquier otra herramienta para grabar imágenes en tarjetas SD) 🛠️

- Disponible en: [Descargar Raspberry Pi Imager](https://www.raspberrypi.org/software/)
- Sistemas operativos compatibles: Windows, macOS, Linux

### Imagen del sistema operativo (Raspberry Pi OS) 🖥️

- Descarga la última versión desde: [Página oficial de Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/)
- Opciones:
  - **Raspberry Pi OS (32-bit)**: Versión recomendada para la mayoría de usuarios
  - **Raspberry Pi OS Lite**: Versión sin entorno gráfico, ideal para servidores
  - **Raspberry Pi OS con Desktop y software recomendado**: Versión completa con todas las aplicaciones incluidas

### VNC Viewer para acceso remoto 🔗

- **Instalar el servidor VNC** en la Raspberry Pi:
  - Ya viene preinstalado en **Raspberry Pi OS con Desktop**, solo hay que habilitarlo.
  - Ir a **Configuración** > **Interfaz** y habilitar **VNC**.
- **Instalar VNC Viewer** en tu computadora:
  - Descarga desde: [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)
  - Sigue las instrucciones para conectarte a la dirección IP de tu Raspberry Pi.

## 3. Red 🌐

### Conexión a Internet 📶

- **Wi-Fi** o **Ethernet** (depende de si tu Raspberry Pi tiene puerto Ethernet)
- Para descarga de software adicional y actualizaciones

---

## 4. Otros componentes (opcionales) ⚙️

### Adaptador USB a SD (si tu PC no tiene ranura SD) 🔄

- Para transferir la imagen del sistema operativo a la tarjeta microSD desde tu computadora.

### Dispositivo de almacenamiento USB (opcional) 💽

- Para transferir archivos desde/hacia la Raspberry Pi

---

Con todos estos componentes listos, podrás proceder a grabar el sistema operativo en la tarjeta microSD, insertar la tarjeta en la Raspberry Pi y configurarla. 🚀
