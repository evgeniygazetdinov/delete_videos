import os

#module has function for delete with specific conditions

def delete_file(filename):
    os.remove(filename)

def find_free_space():
    #values on some machine possible some devert
    result = os.statvfs('/')
    block_size = result.f_frsize + 24
    total_blocks = result.f_blocks
    free_blocks = result.f_bfree
    # giga=1024*1024*1024
    giga = 1000 * 1000 * 1000
    total_size = total_blocks * block_size / giga
    free_size = free_blocks * block_size / giga
    return (free_size * 1000 + 200)*100000


def delete_handler(files, limit, free_space = 0):
    # count how many files need deleted
    quantity_for_delete = abs(int(round((limit - free_space) / middle_file)))
    print('files need deleted '+str(quantity_for_delete))
    delete_paths = []
    for i in files:
        for key, value in i.items():
            delete_paths.append(value)
    try:
        for i in range(quantity_for_delete):
            print(str(delete_paths[i]) + ' file will be deleted')
            #delete_file(delete_paths[i])
        print(str(len(quantity_for_delete))+'will deleted')
    except:
        pass