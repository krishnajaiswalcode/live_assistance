import asyncio
import base64
from google import genai
import traceback
import cv2
import os
from dotenv import load_dotenv
from google.genai import types
import mss
import argparse
import pyaudio


import pyaudio

load_dotenv()

FORMAT =  pyaudio.paInt16
MODEL = "models/gemini-2.5-flash-lite"
CHANNEL = 1
SEND_SAMPLE_RATE = 12000
RECEIVE_SAMPLE_RATE = 250000
CHUNK_SIZE = 1024
# SIMPLE_WIDTH =
MODE = "camera"

client = genai.Client(http_options={"api_key": "v1alpha"},api_key=os.getenv("GENAI_API_KEY"))

tools= [
    types.Tool(google_search=types.Tool.GoogleSearch())
]


CONFIG = types.LiveConnectConfig(
    response_modalities=[
    types.ResponseModality.AUDIO,],
    speech_config=types.SpeechConfig(
       voice_config=types.VoiceConfig(
           prebuilt_voice_config=types.PrebuiltVoiceConfig(voice="leda")
           
       )
),
tools=types.ToolListUnion(tools),
)




