import utils
import mediapipe as mp
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

            if results.multi_hand_landmarks:
                utils.draw_hands_from_multi_hand_landmarks(image,results.multi_hand_landmarks)

            cv2.imshow('Frame', image)
            if cv2.waitKey(5) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
