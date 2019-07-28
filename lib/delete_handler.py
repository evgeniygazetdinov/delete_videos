import os

#module has function for delete with specific conditions

def delete_file(filename):
    os.remove(filename)

def find_free_space():
    #values on some machine possible some devert
    #free size in bites
    st = os.statvfs('/')
    free = st.f_bavail * st.f_frsize
    return free


def delete_handler(files, limit,middle_file,ratio,free_space = 0,):
    # count how many files need deleted
    quantity_for_delete = abs(int(round((limit* ratio - free_space) / middle_file)))
    print('lim is '+str(limit))
    print(free_space)
    print(middle_file)
    print('files need deleted '+str(quantity_for_delete))
    delete_paths = []
    try:
        for i in range(quantity_for_delete):
            print(str(files[i]) + ' file will be deleted')
            #delete_file(delete_paths[i])
        print(str(len(quantity_for_delete))+'will deleted')
    except:
        pass
