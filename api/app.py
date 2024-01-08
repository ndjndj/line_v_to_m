import os
import json
import boto3
from boto3.dynamodb.conditions import Key
from linebot import LineBotApi
from linebot.models import TextSendMessage
import sys

IS_TEST = os.environ("IS_TEST")

voxpics = boto3.resource("dynamodb").Table("voxpics")
USER_PREFIX = "U_#"
INFORMATION = "information"

if IS_TEST == 1:
    LINE_CHANNEL_ACCESS_TOKEN = ""
    LINE_BOT_API = ""
else:
    LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
    LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def received_message(ev):
    return ev[""]

def create_user(ev):
    user_id = ev["source"]["userId"]
    voxpics.put_item(
        Item={
            "pk": f"{USER_PREFIX}{user_id}",
            "sk": INFORMATION,
            "line-id": user_id
        }
    )

def reply(ev): 
    reply_token = ev["replyToken"]
    message = ev["message"]["text"]

#    LINE_BOT_API.reply_message(
#        reply_token, 
#        TextSendMessage(text=message)
#    )
#
#def save_storage():
#    return
#
#def create_sig_url():
#    return

def lambda_handler(event, context):
    print("hello")
    return {"ret": "hello"}