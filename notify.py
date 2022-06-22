from datetime import datetime    
import os
import cv2
import requests
import s3upload as upload
import sendpush as notify
def send(res):
    fileLink = upload.upload(res)
    notify.notify()
    now = datetime.now()
    time = now.strftime("%H-%M-%S")
    date = now.strftime("%m-%d-%y")
    mk = os.path.join("warehouse_result",date)
    try:
        os.makedirs(mk)
    except:
        print("exit")
    filename = time + ".png"
    path = os.path.join(mk,filename)
    cv2.imwrite(path,res)
    try:
        response = requests.post(
                'http://3.108.178.47:5050/detector',
                json={'Time': now,'fileLink' : fileLink}
            )
        result = response.json()
        print(result["result"]['fileLink'])
    except:
        print("Server not connected!!")
    time.sleep(900)