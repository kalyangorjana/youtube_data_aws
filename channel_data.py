import requests
from flask import Flask, send_file, request, render_template, make_response
import json
import Channel_Logger
class channel_data():
    def __init__(self):
        self.logger = Channel_Logger.Channel_Logger()
    
    def get_channel_data(self,video_info_data,comment_data):
        try:
            video_data = {}
            video_data['title'] = video_info_data['items'][0]['snippet']['title']
            video_data['published_on'] = video_info_data['items'][0]['snippet']['publishedAt']
            video_data['channel_title'] = video_info_data['items'][0]['snippet']['channelTitle']
            video_data['description'] = video_info_data['items'][0]['snippet']['description']
            comment_list = []
            for i in comment_data["items"]:
                comment_dict = {}
                comment_dict['author_name']=i['snippet']['topLevelComment']['snippet']['authorDisplayName']
                comment_dict['comment']=i['snippet']['topLevelComment']['snippet']['textOriginal']
                comment_list.append(comment_dict)
            
            video_data['comment_data'] = comment_list
            self.logger.log("Extract the data successfully")
        except Exception as e:
            self.logger.log(str(e))
        return(video_data)