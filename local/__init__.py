# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (__init__.py)
# File Modified : 09/01/2023


import os
import imghdr
import joblib
import cv2
import numpy as np
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import time
import math
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import keras


def class_loader(path:str):
    return joblib.load(str(path))

def img_decoder(model_path:str, img_path:str, classes:any, resize:tuple[int, int]=(256, 256),
                channel:int=3):

    model = keras.models.load_model(str(model_path))

    ext = joblib.load(os.path.join("local", "extensions.pkl"))
    if imghdr.what(img_path) not in ext:
        raise Exception("File Extension Isn't Supported...")
    else:
        img_path = img_path
    classes = joblib.load(classes)
    img = cv2.imread(img_path)
    img = cv2.resize(img, resize)
    img = img.reshape(tuple([1] + list(resize) + [int(channel)]))
    img = img / 255
    prediction = model.predict(img, verbose=0)
    prediction = np.argmax(prediction)
    prediction = classes[prediction]
    return np.array(prediction)

def img_cleaner(img_path):
    ext = joblib.load(os.path.join("local", "extensions.pkl"))
    try:
        what = imghdr.what(img_path)
        if what not in ext:
            os.remove(img_path)
            return f'Image Path {img_path} Removed'
    except Exception:
        return f'An Issued Found !!'

def download(url,  no:int=5, save_format:str='jpeg', save_prefix:str='image', save_dir:str='image'):
    URL = str(url)
    USER_AGENT = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
    }
    IMG_NUMBER = int(no)

    if os.path.isdir(save_dir):
        SAVE_DIR = save_dir
    else:
        os.mkdir(save_dir)
        SAVE_DIR = save_dir

    FORMAT = save_format
    PREFIX = save_prefix

    response = requests.get(URL, headers=USER_AGENT)
    soup = BeautifulSoup(response.text, 'html.parser')
    count = 0
    links = []
    for i in soup.findAll('img', {'class': 'rg_i Q4LuWd'}):
        try:
            key = i['data-src']
            links.append(key)
            count += 1
            if count >= IMG_NUMBER:
                break
        except KeyError:
            continue

    starting_time = int( time.strftime( "%S" ) )
    print("\033[92mDownloading is Started...")
    img_count = 0
    for img in links:
        img_count += 1
        urlretrieve(img, os.path.join(f"{SAVE_DIR}", f"{PREFIX}({img_count}).{FORMAT}"))

    print("\033[91mImages is Downloaded")
    final_time = int(int(time.strftime('%S'))-starting_time)
    print(f"\033[1;33mTotal Time Taken : \033[1;36m{math.gcd(final_time)}")
