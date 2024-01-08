import os
import json
import boto3
from boto3.dynamodb.conditions import Key
from linebot import LineBotApi
from linebot.models import TextSendMessage
import sys

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def reply(ev): 
    reply_token = ev["replyToken"]
    message = ev["message"]["text"]
    LINE_BOT_API.reply_message(
        reply_token, 
        TextSendMessage(text=message)
    )

def save_storage():
    return

def create_sig_url():
    return

def lambda_handler(event, context):
    print("hello")
    return {}