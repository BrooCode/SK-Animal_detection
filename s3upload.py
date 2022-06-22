import boto3 
import cv2
import io
import calendar
import datetime
import uuid
import os


def upload(img):
    success, encoded_image = cv2.imencode('.png', img)
    processed = encoded_image.tobytes()
    ACCESS_KEY = '*'
    SECRET_KEY = '*'
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    bucket = s3.Bucket(name="infyu-animal-detector")

    date = datetime.datetime.utcnow()
    utc_time = calendar.timegm(date.utctimetuple())
    filename = "developement/" + str(utc_time) + ".png"
    bucket.upload_fileobj(io.BytesIO(processed), filename,ExtraArgs={'ACL': 'public-read',"ContentType":"image/png"})
    fileLink="https://infyu-animal-detector.s3.ap-south-1.amazonaws.com/"+filename
    return fileLink

# for file in os.listdir("warehouse_result\\03-26-22"):
#     t = "warehouse_result\\03-26-22\\"+file
#     print(t)
#     im = cv2.imread(t)
#     upload(im)
#     break
