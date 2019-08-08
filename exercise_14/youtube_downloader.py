"""
 当我们获得了youtube上一个视频的url，例如：https://www.youtube.com/watch?v=hSjyCBsR_Qk，
 我们无法通过wget等命令直接下载视频。github上的一个开源工具youtube-dl为我们提供了一个下载youtube视频的接口。
 项目地址：https://github.com/rg3/youtube-dl。

"""
"""
   首先我们用pip安装youtube-dl包：pip install --upgrade youtube-dl。我们可以用命令行的形式来下载youtube视频，
   也可以封装一个函数来完成：
"""
import os
def video_download_func(url_save_dir_tuple):
    """

    download video by url
    :param url:youtube视频url
    :param save_dir:保存视频的目录
    :param save_path:save_path = os.path.join(save_dir,'{}'.format(video_url.split('watch?v=')[1]))
    :return:
    """
       url, save_dir, save_path = url_save_dir_tuple
       try:
            ydl_opts = {'outtmpl': '{}/%(id)s'.format(save_dir)}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl :
                ydl.download([url])

            for video_format in ['.mp4', '_mkv', '.webm']:
                video_path = save_path + video_format
                if os.path.exists(video_path):
                    # do some thing
                    print('download video succeed:{}'.format(video_path))
                    return True
       except Exception as e:
           print('download failed:', url)
           traceback.print_exc()
           return False

       """
       其中save_path是save_dir和视频名称的连接，例如 https://www.youtube.com/watch?v=hSjyCBsR_Qk 会连接成 save_dir/hSjyCBsR_Qk，
       再加上后面判断视频是什么格式：’.mp4’, ‘.mkv’还是 ‘.webm’，最后得到save_dir/hSjyCBsR_Qk.mp4 这种形式。

       """
