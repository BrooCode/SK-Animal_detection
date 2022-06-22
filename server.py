
# from imutils import build_montages
from datetime import datetime
from fileinput import filename
from cv2 import copyTo
import imagezmq
import requests
import imutils
import cv2
import run_tf_detector as detect
import winsound
import os
import s3upload as upload
import sendpush as send_notify

import run_tf_detector_instance as detect2
import numpy as np
from PIL import Image
import time


imageHub = imagezmq.ImageHub()


def send_notification(res,croped):
	#send notification to server
	result = []
	im_pil = Image.fromarray(res)
	imageHeight, imageWidth, channels = res.shape
	try:
		for i in range(1,len(croped)):
			x1, y1,w_box, h_box = croped[i]
			ymin,xmin,ymax, xmax = y1, x1, y1 + h_box, x1 + w_box
			area = (xmin * imageWidth, ymin * imageHeight, xmax * imageWidth,
					ymax * imageHeight)
			out = im_pil.crop(area)
			img = np.array(out)
			res,flag = detect2.load_and_run_detector(img)
			result.append(flag)
		print("errorr")
	except:
		print("not process crop")
		pass
	print(result)
	if 1 in result:  #animal detected
			now = datetime.now()
			time = now.strftime("%H-%M-%S")
			date = now.strftime("%m-%d-%y")
			mk = os.path.join("warehouse_result",date)
			send_notify.notify()
			try:
				os.makedirs(mk)
			except:
				print("exit")    
			filename = time + ".png"
			path = os.path.join(mk,filename)
			cv2.imwrite(path,res)
			return 1
	return 0		



count = 0 
while True:
	(rpiName, frame) = imageHub.recv_image()
	imageHub.send_reply(b'OK')

	frame = imutils.resize(frame, width=600)
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (150, 150)),
		0.007843, (300, 300), 127.5)


	cv2.putText(frame, rpiName, (10, 25),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

	result_img = frame
	croped = [[]]
	try:
		res,flag,box = detect.load_and_run_detector(frame)
		croped = box
		print("visulized")
	except:
		res = result_img
		flag=2
		print("Can't visualized!!!!!!")	
	print(flag)
	if flag == 1 :
		uploadd = send_notification(res,croped)
		if uploadd == 1:
			fileLink = upload.upload(frame)
		# time.sleep(1800)
	result_img = res
		
	cv2.imshow("animal_detection",result_img)


	key = cv2.waitKey(1) & 0xFF


	if key == ord("q"):
		break
	if count==100:
		count=0

# do a bit of cleanup
cv2.destroyAllWindows()