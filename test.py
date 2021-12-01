from os import path
from fastai.basic_train import load_learner
from fastai.vision import *
from fastai import * 
from fastai.vision import * 


learn = load_learner(path="")
classes = ['10 Rupees', '100 Rupees', '1000 Rupees', '20 Rupees', '5 Rupees', '50 Rupees', '500 Rupees', 'Sorry No Money Detected']
img = open_image('./image.jpg')

pred_class, pred_idx, outputs = learn.predict(img)
print(pred_class)
print(type(img))