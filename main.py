import cv2
import pathlib
import shutil


path = pathlib.Path(r"C:\Users\Video tech\Desktop\photos\8-Techtalk")
for file in path.iterdir():
    img=cv2.imread(f"{path}\{file.name}",cv2.IMREAD_COLOR)
    height,width=img.shape[0],img.shape[1]

    pathP=pathlib.Path(r"C:\Users\Video tech\Desktop\portraits")
    pathL=pathlib.Path(r"C:\Users\Video tech\Desktop\landscapes")

    if height>width:
        shutil.copy(f"{path}\{file.name}",pathP)
    else:
        shutil.copy(f"{path}\{file.name}", pathL)