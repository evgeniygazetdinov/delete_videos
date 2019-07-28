import os

#module has function for delete with specific conditions


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
