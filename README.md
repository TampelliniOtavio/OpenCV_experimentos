# Instalar Dependências

Feito com [Python 3.9.6](https://www.python.org/downloads/) (Não testado com versões anteriores)

Necessita do [pip](https://github.com/pypa/get-pip)

```bash
pip install -r requirements.txt
```

# Utilizando

Para mostrar a mão:
```bash
python3 cam/track_hands.py
```

Para fazer um quadrado em volta da mão:
```bash
python3 cam/square_from_hand_landmarks.py
```

Para mostrar apenas dois triângulos, que os vértices são os dedos:

```bash
python3 cam/blue_and_red_mask.py
```

# Documentação

[OpenCV Python](https://docs.opencv.org/4.5.3/d6/d00/tutorial_py_root.html)

[MediaPipe](https://google.github.io/mediapipe/solutions/solutions.html)
