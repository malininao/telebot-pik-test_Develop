import os

def countImg(path):
    img_s = os.listdir(path)
    return len(img_s)
