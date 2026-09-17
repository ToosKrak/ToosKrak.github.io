# import OS module
import os
# Get the list of all files and directories
path = "./Media/Plaatjes/1Popprijs"
dir_list = os.listdir(path)


first_item = dir_list[0]


file_type = '0'
length = 1

while file_type[0] != '.':
    file_type = first_item[-length:]
    length += 1





for count, filename in enumerate(os.listdir(path)):
    if filename != "TMP":
        # rename all the files

        if filename[1] == '.':
            os.rename(path + "/" + filename,  path + "/0" + filename)


