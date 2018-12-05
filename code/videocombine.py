#Code来自：https://www.jianshu.com/p/98a0c091c4bf

import imageio
import ssl

#下面这一句不是必须的, 但是某些情况下访问 https 会报SSL证书不受信任, 加上这一句可以允许通过
ssl._create_default_https_context = ssl._create_unverified_context

#下载 ffmpeg 组件。Download ffmpeg.
imageio.plugins.ffmpeg.download()

#import
from moviepy.editor import *
import os
from natsort import natsorted

#定义一个数组
L = []

# 访问 video 文件夹 (假设视频都放在这里面)
for root, dirs, files in os.walk("./prevue/1"):
    # 按文件名排序
    files = natsorted(files)#This code will sort the file on natural number. 1,2,3,4.....
    #files.sort()#If use this one, the file will go 1,1x,1xx...then 2,2x,2xx...
    # 遍历所有文件。Traverse all the files.
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            # 载入视频
            video = VideoFileClip(filePath)
            # 添加到数组
            L.append(video)

# 拼接视频
final_clip = concatenate_videoclips(L)

# 生成目标视频文件
final_clip.to_videofile("./prevue/1/target.mp4", fps=24, remove_temp=False)

#But there was a problem. The combined video went snowy after the first section.
#合并之后的视频会出现雪花，不知道什么原因。
