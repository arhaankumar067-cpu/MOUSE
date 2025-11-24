import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,max_num_hands=2,min_detection_confidence=0.5,min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
video_capture = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
prev_x, prev_y = 0, 0
smoothing = 2
print("Press 'q' to quit the video stream.")
while True:
   
    success, image = video_capture.read()
    if not success:
        print("Ignoring empty camera frame.")
      
        continue
    image = cv2.flip(image, 1)
  
    frame_height, frame_width, _ = image.shape

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image_rgb.flags.writeable = False

    results = hands.process(image_rgb)

    image.flags.writeable = True

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
           
            mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())

          
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            
            
            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_height)

            
            current_x = prev_x + (x - prev_x) / smoothing
            current_y = prev_y + (y - prev_y) / smoothing

          
            pyautogui.moveTo(screen_width * (current_x / frame_width), screen_height * (current_y / frame_height))

           
            distance = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)
            if distance < 0.05: 
                pyautogui.click()
            
            
            prev_x, prev_y = current_x, current_y
    cv2.imshow('Hand Detection and Air Mouse', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
