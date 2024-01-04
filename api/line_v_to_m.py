import os
import json
import boto3
from boto3.dynamodb.conditions import Key
from linebot import LineBotApi
from linebot.models import TextSendMessage
import sys

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
