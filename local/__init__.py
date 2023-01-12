#!/usr/bin/env python3
# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (__init__.py)
# File Modified : 09/01/2023


import os
import imghdr
import joblib
import cv2
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import keras



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
