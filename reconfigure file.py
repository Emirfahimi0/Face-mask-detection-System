import torch
import os

torch.cuda.empty_cache()

source = 'C:/Users/emirh/OneDrive/Desktop/Project/FYP SYSTEM/Program/yolov5-master/datasets/file Configure/valid\labels'
for root, dirs, filenames in os.walk(source):
    for f in filenames:
        this_file = open(os.path.join(source, f), "r")
        this_files_data = this_file.readlines()
        this_file.close()
        # opens all txt file in directory
        this_file = open(os.path.join(source, f), "w")
        for line in this_files_data:
            s = line[0]
            if s == '0':
                this_file.write(line.replace(s, '2', 1))

        this_file.close()
