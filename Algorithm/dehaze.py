import torch
import torch.nn as nn
import torchvision
import torch.backends.cudnn as cudnn
import torch.optim
import os
import sys
import argparse
import time
import dataloader
import net
import numpy as np
from torchvision import transforms
from PIL import Image
import glob

class dehaze(object):
	def dehaze_image(image_path):

		data_hazy = Image.open(image_path)
		data_hazy = (np.asarray(data_hazy)/255.0)

		data_hazy = torch.from_numpy(data_hazy).float()
		data_hazy = data_hazy.permute(2,0,1)
		data_hazy = data_hazy.cuda().unsqueeze(0)

		dehaze_net = net.dehaze_net().cuda()
		dehaze_net.load_state_dict(torch.load('D:/pycharm/AOD-Net-Dehaze/Algorithm/snapshots/dehazer.pth'))

		clean_image = dehaze_net(data_hazy)
		filename = 'Algorithm/results/' + os.path.split(image_path)[-1]

		torchvision.utils.save_image(clean_image, 'D:/pycharm/AOD-Net-Dehaze/Algorithm/results/' + os.path.split(image_path)[-1])#image_path.split("/")[-1]
		print(filename)


		return filename

	if __name__ == '__main__':
		dehaze_image("D:/pycharm/AOD-Net-Dehaze/Algorithm/test_images/AM_Google_228.png")
	'''	
		test_list = glob.glob("test_images/*")
	
		for image in test_list:
	
			dehaze_image(image)
			print(image, "done!")
	'''
