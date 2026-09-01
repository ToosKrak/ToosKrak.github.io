# import OS module
import os
# Get the list of all files and directories
path = "./Media/Plaatjes/13Bpop"
dir_list = os.listdir(path)
first_item = dir_list[0]

print(first_item[-4:])

file_type = '0'
length = 1

while file_type[0] != '.':
    file_type = first_item[-length:]
    length += 1



for count, filename in enumerate(os.listdir(path)):
    dst = str(count) + ".jpg"

    # rename all the files
    os.rename(os.path.join(path, filename),  os.path.join(path, dst))

