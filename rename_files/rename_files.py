import os
import string

def rename_files():
    #(1) returns a list of file names
    file_list = os.listdir("/Users/klaus.fuchs/Dropbox (Personal)/GitHub/Udacity-FullStackDeveloper/rename_files/prank")
    print(file_list)
    #(2) for each file, rename it
    os.chdir("/Users/klaus.fuchs/Dropbox (Personal)/GitHub/Udacity-FullStackDeveloper/rename_files/prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate({ord(k): None for k in string.digits}))
    print(file_list)
rename_files()



