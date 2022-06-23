import pyrebase


firebaseConfig = {
  'apiKey': "*",
  'authDomain': "*",
  'databaseURL': "*",
  'projectId': "*",
  'storageBucket': "*",
  'messagingSenderId': "*",
  'appId': "*",
  'measurementId': "*"
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

