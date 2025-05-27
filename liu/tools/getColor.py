import cv2
import numpy as np

def nothing(x):
    pass

def show_color_info(event, x, y, flags, param):
    img, window_name = param
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        hsv = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]
        print(f"Position: ({x}, {y}) - BGR: ({b}, {g}, {r}) - HSV: ({hsv[0]}, {hsv[1]}, {hsv[2]})")

def color_picker(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Failed to load image!")
        return

    window_name = 'Color Picker'
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, show_color_info, param=(img, window_name))

    print("Click on the image to get BGR and HSV values (printed in terminal). Press ESC to exit.")

    while True:
        cv2.imshow(window_name, img)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break

    cv2.destroyAllWindows()

# 使用示例
color_picker(r"C:\Users\liuji\Pictures\Screenshots\Screenshot 2025-05-27 203847.png")
