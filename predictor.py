# _*_ utf-8 _*_
# @uthor : Aman Raj
# Filename : local (predictor.py)
# File Modified : 09/01/2023

import local
import os


DIRECTORY = "<DIRECTORY PATH>"
MODEL_FILENAME = "<MODEL FILENAME>"
IMAGE_FILENAME = "<IMAGE FILENAME>"
CLASS_FILENAME = "<CLASS FILENAME>"

PREDICTION = local.img_decoder(
    model_path=os.path.join(DIRECTORY, MODEL_FILENAME),
    img_path=os.path.join(DIRECTORY, IMAGE_FILENAME),
    classes=os.path.join(DIRECTORY, CLASS_FILENAME)
    )

print("Prediction is :", PREDICTION)
