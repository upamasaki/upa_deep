
import cv2
import numpy as np
import glob
import os
files = glob.glob("image/**bmp")

path_list = ["css", "style.css"]
css_path = os.path.join(*path_list)
print(css_path)

for file in files:

    current_dir = os.path.dirname(os.path.abspath(__file__))
    print([current_dir,file])
    tmp = [current_dir,file]
    #print(tmp.type())
    print(current_dir)
    file_full_path = os.path.join(*tmp)

    print(file_full_path)
