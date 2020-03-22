import cv2
import numpy as np
import os
import sys

segments = [
	("images/slide.png", 70, ''),
	("images/scn2.png", 35, ''),
	("images/scn3.png", 35, ''),
	("images/scn4.png", 35, ''),
	("images/view1.png", 75, ''),
	("frames_trajectory_1/", 1, 'scale1_extend'),
	("images/view2.png", 60, ''),
	("frames_trajectory_2/", 1, 'scale1_extend'),
	("images/people.png", 60, ''),
	("frames_3/", 25, 'scale2_extend'),
	("images/rotation.png", 65, ''),
	("frames_5/", 6, 'scale2_extend'),
	("images/distance.png", 65, ''),
	("frames_7/", 2, 'scale2_extend'),
	("images/slide.png", 6, ''),
]

frame_rate = 20
image_width, image_height = 1280, 680
image_size = (image_width, image_height)
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('./socnav_video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), frame_rate, image_size)

x, y = None, None
color = (0, 0, 255)
thickness = 1


def myread(path):
	ret = cv2.imread(path, cv2.IMREAD_UNCHANGED)
	if ret.shape[2] == 4:
		bg = np.array([255, 255, 255])
		alpha = (ret[:, :, 3] / 255).reshape(ret.shape[:2] + (1,))
		ret = ((bg * (1 - alpha)) + (ret[:, :, :3] * alpha)).astype(np.uint8)
	if ret is None:
		print('Couldn\'t read', path)
	return ret[:, :, :3]


def scale1_extend(image):
	scale = myread('images/scale.png')
	return scale_extend(image, scale)


def scale2_extend(image):
	scale = myread('images/scale2.png')
	return scale_extend(image, scale)


def scale_extend(image, scale):
	image = np.concatenate((scale, image, scale), axis=0)
	difference = int((image_width - image.shape[1])/2)
	left = difference
	right = image_width-image.shape[1]-left
	border_type = cv2.BORDER_CONSTANT
	color = [0, 0, 0]
	image = cv2.copyMakeBorder(image, 0, 0, left, right, border_type, value=color)
	return image


images = []
for segment_source, reps, action in segments:
	print(segment_source)
	# We are dealing with a regular image (png)
	if segment_source.endswith('.png'):
		images.append((cv2.resize(myread(segment_source), image_size), reps, action, segment_source))
	# We are dealing with a sequence of images (directory)
	elif segment_source.endswith('/'):
		for image_path in sorted(os.listdir(segment_source)):
			path = segment_source + "/" + image_path
			if not path.endswith('.png'):
				continue
			image = myread(path)
			if image is None:
				print("ERRORRRRRRRRRRRRR", path)
				sys.exit(1)
			images.append((image, reps, action, segment_source))
	# Error
	else:
		print('Every segment source must end with "\\" (for directories or ".png" for regular images')
		sys.exit(1)

for image, reps, action, segment_source in images:
	if action == 'scale1_extend':
		image = scale1_extend(image)
	elif action == 'scale2_extend':
		image = scale2_extend(image)
	elif action != '':
		print('Unknown action', action)
		sys.exit(1)
	for _ in range(reps):
		print(segment_source, image.shape)
		out.write(image)


# When everything done, release the video capture and video write objects
out.release()
