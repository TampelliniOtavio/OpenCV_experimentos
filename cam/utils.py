import numpy as np
from Coord import Coordinate
import mediapipe as mp
import cv2


def round_coord(coord, pixels):
    return round(coord * pixels)

def get_area_from_multi_hands_landmarks(multi_hand_landmarks, image_width, image_height):
    x0 = 1 * image_width
    y0 = 1 * image_height
    x = 0
    y = 0

    for hand_landmarks in multi_hand_landmarks:
        for finger_points in hand_landmarks.landmark:
            if finger_points.x * image_width < x0:
                x0 = round_coord(finger_points.x, image_width)
            if finger_points.y * image_height < y0:
                y0 = round_coord(finger_points.y, image_height)
            if finger_points.x * image_width > x:
                x = round_coord(finger_points.x, image_width)
            if finger_points.y * image_height > y:
                y = round_coord(finger_points.y, image_height)
    return [x0, y0, x, y]

def get_coordenates_from_multi_hands_landmarks(multi_hand_landmarks, image_width, image_height):
    retorno: Coordinate = []
    for hand_landmarks in multi_hand_landmarks:
        for fingers in hand_landmarks.landmark:
            finger_mark = Coordinate(round_coord(fingers.x, image_width),
                round_coord(fingers.y, image_height))
            retorno.append(finger_mark)
    return retorno
    
def return_y_from_a_b_x(a, b, x):
    y = ((a*x) + b)
    roun = round(y)
    limite = 0.01
    if roun > y:
        if roun - y < limite:
            return roun
        else:
            return y
    else:
        if y - roun < limite:
            return roun
        else:
            return y


def draw_polygon(image, points: list[Coordinate], is_closed: bool = True, color=(0, 0, 255), thickness=5):
    pts = []
    for coord in points:
        pts.append(coord.get_coords())
    array = np.array(pts, np.int32)
    array = array.reshape((-1, 1, 2))
    return cv2.polylines(image, array, is_closed, color=color, thickness=thickness, lineType=cv2.LINE_8)


def draw_text(image, text: str, coord: Coordinate, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 0, 255), thickness=1, line_type=cv2.LINE_AA):
    x0, y0 = coord.get_coords()
    return cv2.putText(image, text, (x0, y0), font, font_scale, color, thickness, line_type)


def draw_rectangle(image, ponto_inicial: Coordinate, ponto_final: Coordinate, color=(0, 0, 255), thickness=3):
    x0, y0 = ponto_inicial.get_coords()
    x, y = ponto_final.get_coords()
    return cv2.rectangle(image, (x0, y0), (x, y), color=color, thickness=thickness)


def draw_line(image, ponto1: Coordinate, ponto2: Coordinate, color=(0, 0, 255), thickness=5):
    ponto1_x, ponto1_y = ponto1.get_coords()
    ponto2_x, ponto2_y = ponto2.get_coords()
    return cv2.line(image, (ponto1_x, ponto1_y), (ponto2_x, ponto2_y), color=color, thickness=thickness)


def draw_triangle(image, point1: Coordinate, point2: Coordinate, point3: Coordinate, color=(0, 0, 255), thickness=5):
    draw_line(image, point1, point2, color=color, thickness=thickness)
    draw_line(image, point2, point3, color=color, thickness=thickness)
    draw_line(image, point3, point1, color=color, thickness=thickness)


def draw_hands_from_multi_hand_landmarks(image, multi_hand_landmarks, dots_color=(223, 0, 142), connection_color=()):
    for hand_landmarks in multi_hand_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS,
                                                mp.solutions.drawing_utils.DrawingSpec(
                                                    dots_color, thickness=mp.solutions.drawing_styles._THICKNESS_DOT, circle_radius=mp.solutions.drawing_styles._RADIUS),
                                                mp.solutions.drawing_styles.get_default_hand_connection_style())

if __name__ == '__main__':
    print("ops")
