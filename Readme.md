#### Programas

- Python
- Arduino IDE.


#### Lista de archivos

- manos.py (Código que detecta una mano y envia el numero de dedos levantados por protocolo de comunicación serial).
- arduino_maestro (Se encarga de recibir el dato por puerto serial y genera un numero de opciones según el caso para encender el led correspondiente al numero de 0 a 5)
- gitignore.io (Omite información no relevante al proyecto de windows y python)

#### Instrucciones instalación Windows

- Python

1. git clone
2. cd nombre_carpeta
3. python -m venv env
4. env\Scripts\activate.bat
5. pip install -r requirements.txt
6. python manos.py
7. Para detener presione la tecla q

- Arduino

1. Cargar archivo arduino_maestro.ino
2. Asegurarte del puerto COM#, por defecto esta el COM13, de ser necesario cambiarlo al que te asigne cuando reconozca la placa, modificar tambien en el código de python.
3. Verificar que el led numero 13 de tu tarjeta este encendido, indicador de protocolo de comunicación serial iniciado.
4. Ejecutar archivo  manos.py
5. Validar funcionamiento según el número de dedos levantados