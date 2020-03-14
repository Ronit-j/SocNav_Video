import cv2
import argparse
import os
import time
parser = argparse.ArgumentParser()
args = parser.parse_args()

directory = "./"
directory_names = [ "frames_trajectory_1","frames_trajectory_2","frames_3","frames_5","frames_7"]
Image_width,Image_Height = 1280, 680
frame_rate = 18
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('./outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), frame_rate, (Image_width,Image_Height))
for index,directory in enumerate(directory_names):
	x,y = None,None
	color = (0,0,255)
	thickness = 1
	print(index)
	if index == 0:
		print("inside Index 0")
		slide_image = cv2.imread("./slide.png")
		slide_image = cv2.resize(slide_image,(Image_width,Image_Height))
		time_for_slide = 2 # Seconds
		for _ in range(frame_rate*time_for_slide):
			out.write(slide_image)					
			
	for image_path in sorted(os.listdir(directory)):
		print("./"+directory+"/"+image_path)
		image = cv2.imread("./"+directory+"/"+image_path)
		# print(image)
		if index in [2,3]:
			for _ in range(17):
				image = cv2.resize(image,(Image_width,Image_Height))
				out.write(image)
		image = cv2.resize(image,(Image_width,Image_Height))
		out.write(image)
# When everything done, release the video capture and video write objects
out.release()