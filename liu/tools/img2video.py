import os
import re
import cv2


def natural_sort_key(s):
    """
    自然排序辅助函数，用于正确排序含数字的文件名
    """
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', s)]


def create_video_from_images(input_folder, output_path, fps=24):
    """
    将指定文件夹中的JPG图像合并为MP4视频

    参数:
    input_folder: 包含JPG文件的输入文件夹路径
    output_path: 输出视频文件路径（应以.mp4结尾）
    fps: 输出视频帧率（默认24）
    """

    # 获取所有JPG文件并自然排序
    files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    files.sort(key=natural_sort_key)

    if not files:
        raise ValueError("输入文件夹中没有找到JPG文件")

    # 获取第一个图像的尺寸
    first_image = cv2.imread(os.path.join(input_folder, files[0]))
    if first_image is None:
        raise ValueError(f"无法读取图像文件：{files[0]}")
    height, width = first_image.shape[:2]

    # 初始化视频编码器（尝试多种常见FourCC编码）
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 大多数系统的默认MP4编码器
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    if not video.isOpened():
        # 如果默认编码器失败，尝试其他常见编码器
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        if not video.isOpened():
            raise RuntimeError("无法创建视频文件，请检查编码器支持")

    try:
        for filename in files:
            file_path = os.path.join(input_folder, filename)
            img = cv2.imread(file_path)
            if img is None:
                print(f"警告：无法读取文件 {filename}，已跳过")
                continue
            video.write(img)
    finally:
        video.release()

    print(f"视频已成功生成：{output_path}")


if __name__ == "__main__":
    # 使用示例
    # input_folder = r"C:\Users\liuji\Downloads\VisDrone2019-MOT-val\sequences\uav0000117_02622_v"  # 替换为你的图片文件夹路径
    # input_folder = r"C:\Users\liuji\Downloads\VisDrone2019-MOT-val\sequences\uav0000137_00458_v"  # 替换为你的图片文件夹路径
    # input_folder = r"C:\Users\liuji\Downloads\VisDrone2020-CC\sequences\00081"  # 替换为你的图片文件夹路径
    input_folder = r"C:\xiangmu\PaddleDetection\demo\seadronesee"  # 替换为你的图片文件夹路径
    output_video = "./SeeDroneSee.mp4"  # 输出视频路径

    create_video_from_images(
        input_folder=input_folder,
        output_path=output_video,
        fps=2  # 可调整帧率
    )