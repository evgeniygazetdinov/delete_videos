import os

from lib.search_videos import find_videos
from lib.file_size import find_size
from lib.delete_handler import find_free_space
from lib.older_by import find_older
from lib.delete_handler import
_PATH = os.getcwd()
ratio = 1000000





def main():
    #each func must me for single and call with map)
    #return list
    videos = find_videos(_PATH)
    #return list
    files_by_hour = map(find_size,videos)
    #return value
    total_by_hour = sum(files_by_hour)
    limit_for_delete = total_by_hour*3
    #return value
    free_space = find_free_space()
    older_files = map(find_older,videos)
    print(older_files)


if __name__ == "__main__":
    main()
