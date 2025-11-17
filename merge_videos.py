from moviepy import VideoFileClip, concatenate_videoclips
import os
from datetime import datetime

def get_file_creation_time(file_path):
    """获取文件的创建时间"""
    if os.name == 'nt':  # Windows
        return os.path.getctime(file_path)
    else:  # Unix
        return os.path.getmtime(file_path)

def list_mp4_files(folder_path):
    """列出文件夹中所有的MP4文件，并按创建时间排序"""
    mp4_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.mp4'):
                full_path = os.path.join(root, file)
                creation_time = get_file_creation_time(full_path)
                mp4_files.append((full_path, creation_time))
    
    # 按创建时间排序
    mp4_files.sort(key=lambda x: x[1])
    return [file_info[0] for file_info in mp4_files]

def print_video_list(video_files):
    """打印视频列表（包含创建时间）"""
    print("\n可用的视频文件：")
    for i, file in enumerate(video_files):
        creation_time = datetime.fromtimestamp(get_file_creation_time(file))
        file_name = os.path.basename(file)
        print(f"{i}: {file_name} (创建时间: {creation_time.strftime('%Y-%m-%d %H:%M:%S')})")

def select_videos(video_files):
    """让用户选择要合并的视频"""
    selected_indices = []
    while True:
        try:
            print("\n请输入要合并的视频序号（用逗号分隔），输入'done'完成选择：")
            user_input = input().strip()
            
            if user_input.lower() == 'done':
                break
                
            indices = [int(x.strip()) for x in user_input.split(',')]
            for idx in indices:
                if 0 <= idx < len(video_files) and idx not in selected_indices:
                    selected_indices.append(idx)
                else:
                    print(f"警告：序号 {idx} 无效或重复，已忽略")
                    
        except ValueError:
            print("输入格式错误，请重试")
    
    return [video_files[i] for i in selected_indices]

def merge_videos(selected_videos, output_path):
    """合并选中的视频"""
    try:
        print("\n开始合并视频...")
        clips = [VideoFileClip(video) for video in selected_videos]
        final_clip = concatenate_videoclips(clips)
        
        print("正在导出合并后的视频...")
        final_clip.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac'
        )
        
        # 清理资源
        final_clip.close()
        for clip in clips:
            clip.close()
            
        print(f"\n视频合并完成！已保存至：{output_path}")
        
    except Exception as e:
        print(f"合并过程中出错：{str(e)}")
        # 确保清理资源
        try:
            final_clip.close()
            for clip in clips:
                clip.close()
        except:
            pass

def main():
    # 设置文件夹路径
    folder_path = r"E:\Projects\manimProj\BinarySplit\media\videos\1440p60\partial_movie_files\BinarySearchAnimation"

    if not os.path.exists(folder_path):
        print("文件夹不存在！")
        return
    
    # 获取所有MP4文件
    video_files = list_mp4_files(folder_path)
    if not video_files:
        print("未找到MP4文件！")
        return
    
    # 定义要合并的视频组
    merge_groups = {
        "merge1.mp4": (0, 4),    # 0-4
        "merge2.mp4": (5, 9),    # 5-9
        "merge3.mp4": (10, 15),  # 10-15
        "merge4.mp4": (16, 18),  # 16-18
        "merge5.mp4": (19, 24),  # 19-24
        "merge6.mp4": (25, 27),  # 25-27
        "merge7.mp4": (28, 33),  # 28-33
        "merge8.mp4": (34, 36),  # 34-36
    }
    
    # 处理每组视频
    for output_path, (start_idx, end_idx) in merge_groups.items():
        print(f"\n处理 {output_path} (索引 {start_idx}-{end_idx})...")
        selected_videos = video_files[start_idx:end_idx + 1]
        merge_videos(selected_videos, output_path)

if __name__ == "__main__":
    main()
