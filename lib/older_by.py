import os
import datetime
from file_size import return_name,create_name_path,find_files_older


def day_limit():
    today = datetime.datetime.now()
    hour = datetime.timedelta(days=1)
    limit = today - hour
    delay = limit.replace(second = 0,microsecond=0)
    return delay





def find_older(video_file):
    delay = day_limit()
    name = return_name(video_file)
    name_path = create_name_path(name,video_file)
    older_video = find_files_older(name_path,delay)
    return older_video
