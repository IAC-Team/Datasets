import numpy as np
import tifffile as tiff
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
from numpy import *
from tqdm import tqdm
import cv2


#file path
FILE_2015 = './IAC_data/preliminary/quickbird2015.tif'
FILE_2017 = './IAC_data/preliminary/quickbird2017.tif'
FILE_cadastral2015 = './IAC_data/20170907_hint/cadastral2015.tif'
FILE_tinysample = './IAC_data/20170907_hint/tinysample.tif'
# 0: g  1: r 2: b 3: ir
w_size = 160
skip_size = 16

im = plt.imread(FILE_cadastral2015)

h = 0
l = 0
raw = 0
column = 0
image_name = "cadastral2015_subset_"
savepath = "./IAC_data/dataset/tag_nmirror/"
savepath90 = "./IAC_data/dataset/tag_nmirror90/"
savepath270 = "./IAC_data/dataset/tag_nmirror270/"
savepath180 = "./IAC_data/dataset/tag_nmirror180/"
while raw < np.shape(im)[0] - w_size -skip_size:
    column = 0
    l = 0
    while column <np.shape(im)[1] - w_size -skip_size:
        tmp = im[raw:raw+w_size, column:column+w_size]
        num = str(raw) + '_' + str(column) + '_'
        image_n = "tag_" + image_name + num + ".png"
        cv2.imwrite(savepath + image_n,tmp)
        imgr = Image.open(savepath + image_n)
        imgr_90 = imgr.rotate(90)
        imgr_90 = np.array(imgr_90)
        cv2.imwrite(savepath90 + "r90_" + image_n, imgr_90)
        imgr_180 = imgr.rotate(180)
        imgr_180 = np.array(imgr_180)
        cv2.imwrite(savepath180 + "r180_" + image_n, imgr_180)
        imgr_270 = imgr.rotate(270)
        imgr_270 = np.array(imgr_270)
        cv2.imwrite(savepath270 + "r270_" + image_n, imgr_270)
        column = column + skip_size
        l = l + 1
    raw = raw + skip_size
    h = h + 1
    print("total: ", (np.shape(im)[0] - w_size - skip_size) / skip_size, "\tfinished: ", raw / skip_size,"\ntotal picture number:", l * h)

print("Dataset create successfully!")


