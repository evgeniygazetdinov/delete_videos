import os
import datetime

#module has function for delete with specific conditions

def delete_file(filename):
    os.remove(filename)

def find_free_space(path):
    #values on some machine possible some devert
    #free size in bites
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    return free


def delete_handler(files, limit,middle_file,ratio,free_space = 1,path):
    # count how many files need deleted
    counter = 0
    free_space = find_free_space(path)
    delete_paths = []
    for i in files:
        for key, value in i.items():
            delete_paths.append(value)
    print(str(len(files))+' files for delete')
    free_space = find_free_space(path)
    try:
       while free_space< limit:
            if free_space>= limit:
                print("you have enough space "+ str(free_space/ratio)+'gb',flush = True)
                print(datetime.datetime.now(),flush =True)
            free_space = find_free_space(path)
            delete_file(delete_paths[counter])
            counter+=1
            print(delete_paths[counter])
    except:
        print('*'*50)
        print('files'+str(counter)+'deleted')
        pass
