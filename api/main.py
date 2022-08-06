import uvicorn
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse

import time
from model import faceDetect

app = FastAPI()

data_file = "pred.jpeg"
target_file = "target.jpeg"
data_label = ["Default"]

@app.get("/")
def index():
    return {"Computer Vision":"Face Detect"}


@app.post("/upload/data_file")
async def upload(Source_Image: UploadFile = File(...), Name:str = Form(...)):
    
    data_label.append(Name)

    with open(data_file, "wb") as buffer:
        shutil.copyfileobj(Source_Image.file, buffer)

    return {"filename": Source_Image.filename}


@app.post("/upload/target_file")
async def Target_Image(Target_Image: UploadFile = File(...)):

    with open(target_file, "wb") as buffer:
        shutil.copyfileobj(Target_Image.file, buffer)

    return {"filename": Target_Image.filename}


@app.get("/result")
async def Prediction():
  model = faceDetect(data_file, data_label[-1])
  model.predict(target_file)
  time.sleep(10)
  result = FileResponse("target.jpeg")
  return result

if __name__=="__main__":
    uvicorn.run(app, port=8000)