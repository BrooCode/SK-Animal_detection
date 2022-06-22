import uvicorn
from fastapi import FastAPI, Request,UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import firebase as auth
import awstop as file
import tokenn as token
from datetime import datetime
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/fileLink')
def get_form(request: Request):
    result = "Links..."
    return  result

# {
#     "key":"infyulabs-animal-detector"
# }

@app.post('/fileLink')
async def post_form(request: Request):
    req_info = await request.json()
    key = req_info['key']
    print(key)
    if key=="infyulabs-animal-detector":
        result = file.filelink()
    else:
        result = "Access Denied!!"
    print(result)
    return {"FileLinks" : result}


@app.get('/authentication')
def get_form(request: Request):
    result = "LogIn......"
    return  result

#  uid: str = None
# {
#     "email":"",
#     "password":"",
#     "token":""
# }
@app.post('/authentication')
async def post_form(request: Request):
        req_info = await request.json()
        now = datetime.now()
        end = now.strftime("%H-%M-%S")
        print("time : " + str(end) + "  :  " + req_info['token'])
        try:
            token.token_generate(req_info['token'])
            print("added")
        except:
            pass
            print("toje")
        flag = auth.login(req_info['email'],req_info['password'])
        if flag==1:
            result = "Logged In Successfully!!"
        else:
            result = "Wrong credentials"
        return {"result" : result}
