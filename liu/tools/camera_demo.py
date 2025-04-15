import imageio
import cv2

reader = imageio.get_reader("<video3>")  # 默认会自动找第一个摄像头

for frame in reader:
    # imageio 输出是 RGB，而 OpenCV 用 BGR，所以需要转换
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("OBS 虚拟摄像机（via imageio）", frame_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

reader.close()
cv2.destroyAllWindows()




import cv2

# 用名字打开 OBS 虚拟摄像头
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("无法打开 OBS 虚拟摄像头")
    exit()

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("无法读取 OBS 画面")
        break

    cv2.imshow("OBS 虚拟摄像头", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
