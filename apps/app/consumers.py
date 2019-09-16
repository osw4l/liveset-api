from channels import Group
import json


def connect_videos_streaming(message):
    message.reply_channel.send({'accept': True})
    Group("videos").add(message.reply_channel)


def receive_videos_streaming(message):
    Group("videos").send({
        'text': message.content['text']
    })


def disconnect_videos_streaming(message):
    Group("videos").discard(message.reply_channel)

