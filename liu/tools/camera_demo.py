import imageio
import cv2

reader = imageio.get_reader("<video0>")  # 默认会自动找第一个摄像头

for frame in reader:
    # imageio 输出是 RGB，而 OpenCV 用 BGR，所以需要转换
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("OBS 虚拟摄像机（via imageio）", frame_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

reader.close()
cv2.destroyAllWindows()




# import cv2
# import time
#
# print("正在测试摄像头设备...")
#
# for i in range(6):
#     cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # 使用 DirectShow 后端（兼容性更好）
#
#     if cap.isOpened():
#         print(f"尝试打开摄像头 {i}...")
#         ret, frame = cap.read()
#         if ret and frame is not None:
#             print(f"✅ 摄像头 {i} 成功读取帧")
#             cv2.imshow(f"Camera {i}", frame)
#             cv2.waitKey(2000)
#             cv2.destroyWindow(f"Camera {i}")
#         else:
#             print(f"⚠️ 摄像头 {i} 打开但无法读取帧")
#         cap.release()
#     else:
#         print(f"❌ 摄像头 {i} 无法打开")
#
# cv2.destroyAllWindows()
