import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyDEOKvIMA_jCkhrsOqhrDeTprMWcGT0L0E",
  'authDomain': "infyulabs-4adc0.firebaseapp.com",
  'databaseURL': "https://infyulabs-4adc0-default-rtdb.firebaseio.com",
  'projectId': "infyulabs-4adc0",
  'storageBucket': "infyulabs-4adc0.appspot.com",
  'messagingSenderId': "1009466381176",
  'appId': "1:1009466381176:web:e3889591c7ddd9c15c2e8d",
  'measurementId': "G-BYT7Y1YTEK"
};  


firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#Login function

def login(email,password):
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        return 1
    except:
        print("Invalid email or password")
    return 0

