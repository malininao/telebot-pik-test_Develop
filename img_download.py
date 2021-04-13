import os

def countImg(path):
    img_s = os.listdir(path=path)
    return len(img_s)
