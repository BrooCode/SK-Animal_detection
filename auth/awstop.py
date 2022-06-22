import boto3 

ACCESS_KEY = '*'
SECRET_KEY = '*'

session = boto3.Session( 
         aws_access_key_id=ACCESS_KEY, 
         aws_secret_access_key=SECRET_KEY)

#Then use the session to get the resource
s3 = session.resource('s3')

my_bucket = s3.Bucket('infyu-animal-detector')


def filelink():
    count=0
    fileLink="https://infyu-animal-detector.s3.ap-south-1.amazonaws.com/"
    res = []
    for objects in my_bucket.objects.all():
        if count==0:
            count+=1
            continue
        temp = fileLink+str(objects.key)
        # temp = str(objects.key)
        res.append(temp)
    res.reverse()
    return res[:5]