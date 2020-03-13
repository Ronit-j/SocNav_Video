import cv2
import argparse
import os
import time
parser = argparse.ArgumentParser()
args = parser.parse_args()

directory = "./"
filenames = [ "./sngnn.mpeg", "./video_2.webm", "./video_3.webm", "./video_4.webm", "./video_5.webm", "./project1.mpeg", "./project2.mpeg"]

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('./outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 18, (1280,680))
for index,video in enumerate(filenames):
	
	# Create a VideoCapture object
	cap = cv2.VideoCapture(video)# put the path of the video here
	write_flag = False
	text = None
	print(index)
	x,y = None,None
	color = (0,0,255)
	thickness = 1
	if index in [1,2,3,4,5,6]:
			if index == 1:
				frame = cv2.imread("video_"+str(index+1)+".png")
				frame = cv2.resize(frame, (1280,680))
				text = "The impact of walls"
				frame = cv2.putText(frame, text ,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1, color, thickness, cv2.LINE_AA, False)
				for i in range(48):
					out.write(frame)
			elif index == 2:
				frame = cv2.imread("video_"+str(index+1)+".png")
				frame = cv2.resize(frame, (1280,680))
				text = "Impact of incrementing the number of people in a room"
				frame = cv2.putText(frame, text ,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1, color, thickness, cv2.LINE_AA, False)
				for i in range(48):
					out.write(frame)
			elif index == 3:
				frame = cv2.imread("video_"+str(index+1)+".png")
				frame = cv2.resize(frame, (1280,680))
				text = "The impact of angle when approaching interacting people"
				frame = cv2.putText(frame, text ,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1, color, thickness, cv2.LINE_AA, False)
				for i in range(48):
					out.write(frame)
			elif index == 4:
				frame = cv2.imread("video_"+str(index+1)+".png")
				frame = cv2.resize(frame, (1280,680))
				text = "The impact of distance between two interacting people"
				frame = cv2.putText(frame, text ,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1, color, thickness, cv2.LINE_AA, False)
				for i in range(48):
					out.write(frame)
			elif index == 5:
				frame = cv2.imread("sample.jpg")
				frame = cv2.resize(frame, (1280,680))
				text = "The trajectories are decided depending upon the social acceptibilty score on the neighbouring area"
				frame = cv2.putText(frame, text ,(50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness, cv2.LINE_AA, False)
				for i in range(48):
					out.write(frame)
				

			
				
	while(True):

		ret, frame = cap.read()
		if ret is False:
			break

		# Cropping last two videos Their image size is (640,640)
		if index in [ 6,7]:
			ImageHeight = 640
			ImageWidth = 600
			frame = frame[0:0+ImageHeight,0:0+ImageWidth] 
		frame = cv2.resize(frame, (1280,680))
		img = frame
		cv2.imshow("Original_Video_Output",frame)
		
		#Key Event Handling
		key = cv2.waitKey(1) & 0xFF 
		
		if key == ord('q'):
			break

		elif key == ord("w"): # press W to write a caption and to stop displaying it on the future frame press S(Stop)
			text = str(input("Input the Caption:"))
			x,y = int(input("X:")),int(input("Y:"))
			pos = x ,y
			img = cv2.putText(img,text,(x,y),3,0.8,(0,0,255))
			write_flag = True

		elif key == ord("s"):
			write_flag = False
		
		if write_flag:
			print("Write_Flag is on")
			# print(text,x,y)
			img = cv2.putText(img,text,(x,y),3,0.8,(0,0,255))
		
		cv2.imshow("Video_Output",img)
		
		#Repeating frames to slow down the video
		if index in [2,3]:
			for i in range(10):
				out.write(img)
		out.write(img)
	cap.release()

# When everything done, release the video capture and video write objects
out.release()