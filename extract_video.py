import cv2
import os
from datetime import timedelta

def extract_frames(video_path, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 读取视频
    video = cv2.VideoCapture(video_path)
    
    # 获取视频的基本信息
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    print(f"视频FPS: {fps}")
    print(f"总帧数: {total_frames}")
    print(f"视频时长: {timedelta(seconds=duration)}")
    
    frame_count = 0
    
    while True:
        # 读取一帧
        success, frame = video.read()
        
        if not success:
            break
            
        # 计算当前时间点
        time_point = frame_count / fps
        time_str = str(timedelta(seconds=time_point)).replace(":", "-")
        
        # 保存图片，文件名格式：frame_001_00-00-00.jpg
        output_path = os.path.join(
            output_folder, 
            f"frame_{frame_count:03d}_{time_str}.jpg"
        )
        cv2.imwrite(output_path, frame)
        
        frame_count += 1
        
        # 打印进度
        if frame_count % 100 == 0:
            print(f"已处理 {frame_count}/{total_frames} 帧")
    
    video.release()
    print("完成！所有帧已保存。")

# 使用示例
video_path = r"E:\Projects\manimProj\BinarySplit\media\videos\1440p60\BinarySearchAnimation.mp4"  # 替换为你的视频文件路径
output_folder = r"E:\Projects\manimProj\BinarySplit\media\images"  # 替换为你想保存图片的文件夹路径

extract_frames(video_path, output_folder)