#Instalar librerias
#pip install mediapipe==0.10.1
#pip install pyserial==3.5
#pip install opencv-python==4.7.0.72
 
#Librerias
import cv2
import mediapipe as mp
import serial 
import time

#Crea un objeto de detección de manos
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configura el modelo "lite" de MediaPipe para la detección de manos
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

#Comunicacion serial
puerto = 'COM13'
baud_rate = 9600

# Inicializar la conexión serial
ser = serial.Serial(port=puerto, baudrate=baud_rate, timeout=1)# Asegúrate de ajustar el puerto COM adecuadamente
#Esperar 1 seg
time.sleep(1)
# Verificar si la conexión serial está abierta
if ser.is_open:
    print(f'Conexión serial establecida en el puerto {puerto} a {baud_rate} bps.')
else:
    print('Error al abrir la conexión serial.')

#Inicializa la captura de video desde la cámara y comienza a procesar los fotogramas
cap = cv2.VideoCapture(0)

while True:
    # Leer el fotograma de la cámara
    ret, frame = cap.read()

    # Convertir la imagen a RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar manos en el fotograma
    results = hands.process(frame_rgb)
    
    # Contador para contar los dedos levantados
    total_dedos = 0
    # Dibujar marcas y conexiones en las manos detectadas
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Determinar si el dedo índice está levantado
            if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y:
                total_dedos += 1
            # Determinar si el dedo medio está levantado
            if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y:
                total_dedos += 1
            # Determinar si el dedo anular está levantado
            if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y:
                total_dedos += 1
            # Determinar si el dedo meñique está levantado
            if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y:
                 total_dedos += 1
            # Determinar si el pulgar está levantado
            if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
                total_dedos += 1

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Enviar los datos a través de la conexión serial
    datos = str(total_dedos)
    ser.write(datos.encode())
    time.sleep(0.1)  # Espera 0.1 segundo
    print(datos.encode())

    # Mostrar el fotograma con las manos detectadas
    cv2.putText(frame, f"Dedos levantados: {total_dedos}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Hand Detection', frame)
     
    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
# Liberar los recursos
cap.release()
cv2.destroyAllWindows()