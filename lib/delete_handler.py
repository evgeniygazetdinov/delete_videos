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


def delete_handler(files, limit,middle_file,ratio,free_space = 1,):
    # count how many files need deleted

    quantity_for_delete = abs(int(round((limit* ratio - free_space) / middle_file)))
    print('lim is '+str(limit/ratio)+' mb')
    print('files need deleted '+str(quantity_for_delete))
    try:
        for i in range(quantity_for_delete):
            print(str(files[i]) + ' file will be deleted')
            free_space = find_free_space()
            #delete_file(files[i])
            if free_space >= limit:
                print("You have free_space")
                break
            else:
                continue
    except:
        print(str(quantity_for_delete)+'will deleted')
        pass
