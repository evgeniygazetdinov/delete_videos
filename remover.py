import os

from lib.search_videos import find_videos
from lib.file_size import find_size

_PATH = os.getcwd()






def main():
    #each func must me for single and call with map)
    videos = find_videos(_PATH)
    files_by_hour = map(find_size,videos)
    total_by_hour = sum(files_by_hour)
    limit_for_delete = total_by_hour*3


if __name__ == "__main__":
    main()
