from Coord import Coordinate
import utils
import mediapipe as mp
import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
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
            dedao: Coordinate
            indicador: Coordinate
            meio: Coordinate
            anelar: Coordinate
            mindinho: Coordinate
            if results.multi_hand_landmarks:
                mao_inteira = utils.get_coordenates_from_multi_hands_landmarks(results.multi_hand_landmarks,
                    image_width, image_height)
                punho = mao_inteira[mp_hands.HandLandmark.WRIST]
                dedao = mao_inteira[mp_hands.HandLandmark.THUMB_TIP]
                indicador = mao_inteira[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                meio = mao_inteira[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                anelar = mao_inteira[mp_hands.HandLandmark.RING_FINGER_TIP]
                mindinho = mao_inteira[mp_hands.HandLandmark.PINKY_TIP]

                utils.draw_triangle(image,punho, dedao,mindinho)
                utils.draw_triangle(image,indicador,meio, anelar, color=(255,0,0))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            lower_blue = np.array([110, 255, 255])
            upper_blue = np.array([130, 255, 255])
            mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
            res_blue = cv2.bitwise_and(image, image, mask=mask_blue)

            lower_red = np.array([0, 255, 255])
            upper_red = np.array([0, 255, 255])
            mask_red = cv2.inRange(hsv, lower_red, upper_red)
            res_red = cv2.bitwise_and(image, image, mask=mask_red)

            result = cv2.addWeighted(res_blue, 1, res_red,1,0)

            cv2.imshow('Dedos', result)

            if cv2.waitKey(5) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()