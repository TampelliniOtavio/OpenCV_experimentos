from Coord import Coordinate
from utils import check_for_hangloose, draw_hands
from mediapipe.python.solutions import drawing_styles
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
drawing_styles = mp.solutions.drawing_styles

with mp_hands.Hands(min_detection_confidence=0.75,
                    min_tracking_confidence=0.75, max_num_hands=1) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_height, image_width, _ = image.shape
        image_copy = image.copy()

        x0 = 1 * image_width
        y0 = 1 * image_height
        x = 0
        y = 0
        dedao: Coordinate
        indicador: Coordinate
        meio: Coordinate
        anelar: Coordinate
        mindinho: Coordinate
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                dedao = Coordinate(hand_landmarks.landmark[4].x,
                    hand_landmarks.landmark[4].y)
                indicador = Coordinate(hand_landmarks.landmark[8].x,
                    hand_landmarks.landmark[8].y)
                meio = Coordinate(hand_landmarks.landmark[12].x,
                    hand_landmarks.landmark[12].y)
                anelar = Coordinate(hand_landmarks.landmark[16].x,
                    hand_landmarks.landmark[16].y)
                mindinho = Coordinate(hand_landmarks.landmark[20].x,
                    hand_landmarks.landmark[20].y)
                for finger_points in hand_landmarks.landmark:
                    if finger_points.x * image_width < x0:
                        x0 = round(finger_points.x * image_width)
                    if finger_points.y * image_height < y0:
                        y0 = round(finger_points.y * image_height)
                    if finger_points.x * image_width > x:
                        x = round(finger_points.x * image_width)
                    if finger_points.y * image_height > y:
                        y = round(finger_points.y * image_height)
                
                draw_hands(image, hand_landmarks, (208, 224, 64))

        if x0 == 1 * image_width and y0 == 1 * image_height and x == 0 and y == 0:
            retangulo = image
        else:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, 'Hand', (x0, y0-5), font,
                        1, (0, 0, 255), 1, cv2.LINE_AA)
            retangulo = cv2.rectangle(
                image, (x0, y0), (x, y), (0, 0, 255), 3)
        cv2.imshow('Frame', retangulo)
        if cv2.waitKey(1) == ord('r'):
            check_for_hangloose(dedao,indicador, meio, anelar, mindinho)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
