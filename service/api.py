import os
import sys
import uvicorn

from fastapi import FastAPI, HTTPException, File
from pydantic import BaseModel

path_this = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(path_this, ".."))
src_path = os.path.join(root_path, "src")
sys.path.append(src_path)

from inference import Inference

app = FastAPI(title="Text Correction and Segmentation API", 
              description="Indonesian Text Correction and Segmentation for Preprocessing NLP", 
              version="1.0.0")
inf = Inference()

class Text(BaseModel):
    text:str

@app.post("/segment")
async def segment(item: Text, status_code=200):
    txt = item.text
    try:
        result = inf.segment(txt)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    return {"result": result}

@app.post("/correct")
async def correct(item: Text, status_code=200):
    txt = item.text
    try:
        result = inf.correct(txt)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    return {"result": result}


if __name__ == "__main__":

    uvicorn.run("api:app", port=6969, log_level="info", reload=False)