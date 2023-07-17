from pytube import *
from tkinter.filedialog import *
from tqdm import tqdm


def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
    process_bar.update(len(data_chunk))


try:
    URL = "https://www.youtube.com/watch?v=8eAOTpfMoik&ab_channel=%E4%B8%89%E7%AB%8B%E8%8F%AF%E5%8A%87SETDrama"
    path_save = askdirectory()
    if path_save is None:
        exit()

    proxy_handler = {
        "http": "http://10.11.12.6:10801",
        'https': "http://10.11.12.6:10801"
    }
    ob = YouTube(URL, on_progress_callback=progress_callback, proxies=proxy_handler)
    stream = ob.streams.filter(file_extension='mp4').get_by_itag(137)  # 22表示720p,137为1080p
    file_size = stream.filesize
    video_name = stream.title + '.mp4'
    process_bar = tqdm(total=stream.filesize, unit="bytes")
    stream.download(path_save, video_name)

except Exception as e:
    print(e)
    print("出现错误!!")
