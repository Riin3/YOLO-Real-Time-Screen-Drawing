# YOLO-Real-Time-Screen-Drawing
基于Yolo的实时屏幕测绘脚本

提供一个更方便的模型测试手段

模型来源：https://github.com/Sempre0721/YOLO-Real-time-screen-detection-of-human-shapes

1.获取屏幕截图：使用 mss 库获取当前屏幕的图像。

2.目标检测：将获取的图像传入预训练的 YOLO 模型，进行目标检测，返回检测框。

3.绘制检测框：使用 PyQt5 创建一个透明的窗口，实时在屏幕上绘制检测到的目标框。

![EXAMPLE](https://raw.githubusercontent.com/Yoelns/YOLO-Real-time-Screen-Drawing/refs/heads/main/example.png)

仅供交流学习
