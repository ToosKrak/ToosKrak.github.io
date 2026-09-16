# import OS module
import os
# Get the list of all files and directories
path = "./Media/Plaatjes/14Mixtream"
dir_list = os.listdir(path)

try:
    os.mkdir(path + "/TMP")
except:
    dir_list.remove("TMP")


first_item = dir_list[0]


file_type = '0'
length = 1

while file_type[0] != '.':
    file_type = first_item[-length:]
    length += 1





for count, filename in enumerate(os.listdir(path)):
    if filename != "TMP":
        # rename all the files

        dst = str(count+1) + file_type
        if count < 9:
            dst = "0" + dst


        os.rename(path + "/" + filename,  path + "/TMP/" + dst)


for count, filename in enumerate(os.listdir(path + "/TMP")):
    os.rename(path + "/TMP/" + filename, path + "/" + filename)