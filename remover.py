import os

from lib.search_videos import find_videos
from lib.file_size import find_size
from lib.older_by import find_older
from lib.delete_handler import delete_handler,find_free_space
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
    #return value
    limit_for_delete = total_by_hour*3
    #return list
    older_files = map(find_older,videos)
    free_space = find_free_space()
    #default free_space is 0 for delete all
    #func take inside list with files
    delete_handler(older_files,limit_for_delete)

if __name__ == "__main__":
    main()
