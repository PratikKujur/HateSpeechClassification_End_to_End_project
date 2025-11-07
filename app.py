# from hate.pipeline.train_pipeline import TrainPipeline
from fastapi import FastAPI
import uvicorn
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from hate.pipeline.prediction_pipeline import PredictionPipeline
from hate.exception import CustomException
# from hate.constants import *
import streamlit as st


# text:str = "What is machine learing?"

# app = FastAPI()

# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")


# @app.get("/train")
# async def training():
#     try:
#         train_pipeline = TrainPipeline()

#         train_pipeline.run_pipeline()

#         return Response("Training successful !!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")


# @app.post("/predict")
# async def predict_route(text):
#     try:

#         obj = PredictionPipeline()
#         text = obj.run_pipeline(text)
#         return text
#     except Exception as e:
#         raise CustomException(e, sys) from e


# if __name__=="__main__":
#     uvicorn.run(app, host=APP_HOST, port=APP_PORT)

st.title("\U0001F620 Hate Speech Detection")
st.write("Enter text to analyze for hate speech:")
user_input = st.text_area("Text Input", height=200)
if st.button("Analyze"):
    try:
        obj = PredictionPipeline()
        result = obj.run_pipeline(user_input)
        st.write("Analysis Result:")
        st.write(result)
    except Exception as e:
        st.error(f"Error Occurred! {e}")