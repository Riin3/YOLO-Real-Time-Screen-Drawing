import cv2
import numpy as np
import mss
from ultralytics import YOLO
from PIL import Image
import sys
import numpy as np
import mss
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QPixmap
from PyQt5.QtCore import Qt, QRect
from ultralytics import YOLO

class ScreenOverlay(QMainWindow):
    def __init__(self, boxes):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, 1920, 1080)
        self.boxes = boxes

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        for box in self.boxes:
            painter.drawRect(QRect(box[0], box[1], box[2] - box[0], box[3] - box[1]))

def get_screen_image():
    sct = mss.mss()
    monitor = sct.monitors[1]
    screenshot = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    return frame

def detect_objects(frame, model):
    results = model(frame)
    boxes = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            boxes.append((int(x1), int(y1), int(x2), int(y2)))
    return boxes

def main():
    app = QApplication(sys.argv)
    model = YOLO('yolov8n-pose.pt')
    while True:
        frame = get_screen_image()
        boxes = detect_objects(frame, model)
        overlay = ScreenOverlay(boxes)
        overlay.show()
        app.processEvents()

if __name__ == '__main__':
    main()

model = YOLO('yolov8n-pose.pt')

sct = mss.mss()
monitor = sct.monitors[1]
sct = mss.mss()
monitor = sct.monitors[1]

while True:
    screenshot = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    results = model(frame)

    for result in results:
        im_array = result.plot()
        im = Image.fromarray(im_array[..., ::-1])
        im.show()

    cv2.imshow('Screen Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()