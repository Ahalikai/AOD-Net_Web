import cv2
import math
import numpy as np

from PIL import Image


def make_regalur_image(img, size=(64, 64)):
    gray_image = img.resize(size).convert('RGB')
    return gray_image


# 计算直方图
def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    hist = sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)
    return hist


# 计算相似度
def calc_similar(li, ri):
    calc_sim = hist_similar(li.histogram(), ri.histogram())
    return calc_sim


def similar(image_path1, image_path2):
    image1 = Image.open(image_path1)
    image1 = make_regalur_image(image1)
    image2 = Image.open(image_path2)
    image2 = make_regalur_image(image2)
    print("图片间的相似度为", calc_similar(image1, image2))
    # 图像分块
    src = cv2.imread(image_path1, -1)
    cnt = 1
    num = 1
    sub_images = []
    sub_image_num = 3
    src_height, src_width = src.shape[0], src.shape[1]
    sub_height = src_height // sub_image_num
    sub_width = src_width // sub_image_num
    for j in range(sub_image_num):
        for i in range(sub_image_num):
            if j < sub_image_num - 1 and i < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width: (i + 1) * sub_width, :]
            elif j < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width:, :]
            elif i < sub_image_num - 1:
                image_roi = src[j * sub_height:, i * sub_width: (i + 1) * sub_width, :]
            else:
                image_roi = src[j * sub_height:, i * sub_width:, :]
            sub_images.append(image_roi)
    for i, img in enumerate(sub_images):
        cv2.imwrite('pic\\dehaze\\dehaze_f' + str(i) + '.jpg', img)

    src = cv2.imread(image_path2, -1)
    cnt = 1
    num = 1
    sub_images = []
    sub_image_num = 3
    src_height, src_width = src.shape[0], src.shape[1]
    sub_height = src_height // sub_image_num
    sub_width = src_width // sub_image_num
    for j in range(sub_image_num):
        for i in range(sub_image_num):
            if j < sub_image_num - 1 and i < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width: (i + 1) * sub_width, :]
            elif j < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width:, :]
            elif i < sub_image_num - 1:
                image_roi = src[j * sub_height:, i * sub_width: (i + 1) * sub_width, :]
            else:
                image_roi = src[j * sub_height:, i * sub_width:, :]
            sub_images.append(image_roi)
    for i, img in enumerate(sub_images):
        cv2.imwrite('pic\\demo\\demo_f' + str(i) + '.jpg', img)

    pic_similar = []
    for i in range(3 * 3):
        image1 = Image.open('pic\\demo\\demo_f' + str(i) + '.jpg')
        image1 = make_regalur_image(image1)
        image2 = Image.open('pic\\dehaze\\dehaze_f' + str(i) + '.jpg')
        image2 = make_regalur_image(image2)
        pic_similar.append(calc_similar(image1, image2))
        print("图片间的相似度为", pic_similar[i])
    pic_similar_std = np.std(pic_similar, ddof=1)
    print("标准差为:%f" % pic_similar_std)
    return pic_similar_std
