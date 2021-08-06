import numpy as np
import math
from Coord import Coordinate
import mediapipe as mp

def return_y_from_a_b_x(a,b,x):
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

def draw_hands(image, hand_landmarks, dots_color=(), connection_color=()):
    mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS,
        mp.solutions.drawing_utils.DrawingSpec(
        dots_color, thickness=mp.solutions.drawing_styles._THICKNESS_DOT, circle_radius=mp.solutions.drawing_styles._RADIUS),
        mp.solutions.drawing_styles.get_default_hand_connection_style())

def check_for_hangloose(dedao: Coordinate, indicador: Coordinate, meio: Coordinate, anelar: Coordinate, mindinho: Coordinate):
    x_dedao, y_dedao = dedao.get_coords()
    x_indicador, y_indicador = indicador.get_coords()
    x_meio, y_meio = meio.get_coords()
    x_anelar, y_anelar = anelar.get_coords()
    x_mindinho, y_mindinho = mindinho.get_coords()

    x = [x_dedao, x_mindinho]
    y = [y_dedao, y_mindinho]

    x2 = [(x_indicador + x_meio)/2, (x_anelar + x_meio)/2]
    y2 = [(y_indicador + y_meio)/2, (y_anelar + y_meio)/2]

    a, b = np.polyfit(x, y, 1)
    a2,b2 = np.polyfit(x2, y2, 1)
    print(f"Equacao da reta entre dedao e mindinho: y = {a:.2f}x + {b:.2f}")
    print(f"Equacao da reta entre os 3 dedos do meio: y = {a2:.2f}x + {b2:.2f}")
    # print(return_y_from_a_b_x(a,b,x_dedao))
    # angular_coeficient = 0.0
    # if x_dedao < x_mindinho:
    #     angular_coeficient = (y_mindinho - y_dedao) / (x_mindinho - x_dedao)
    # else:
    #     angular_coeficient = (y_dedao - y_mindinho) / (x_dedao - x_mindinho)

    
if __name__ == '__main__':
    dedao = Coordinate(1,3)
    indicador = Coordinate(111,222)
    meio = Coordinate(222,333)
    anelar = Coordinate(333,444)
    mindinho = Coordinate(3,5)

    check_for_hangloose(dedao, indicador, meio,anelar, mindinho)
