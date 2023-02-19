import requests
from flask import Flask, send_file, request, render_template, make_response
import json
import channel_data
import mongoDB
import Channel_Logger

application = Flask(__name__)
app = application
logger = Channel_Logger.Channel_Logger()

channel_data = channel_data.channel_data()
mongo_db = mongoDB.mongoDB()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/channel", methods=["POST"])
def get_channel_info():
    if request.method == 'POST':
        url = request.form['url']
    api_key = "AIzaSyDbVke3REsYIKgozMWQGD3yNDonX7fJk90"
    try:
        video_id = url.split("=")[1]
    except Exception as e:
        self.logger.log(str(e))
    video_info_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    video_comments = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
    video_info_response = requests.get(video_info_url)
    video_info_data = video_info_response.json()
    video_comment_response = requests.get(video_comments)
    comment_data = video_comment_response.json()
    video_data = channel_data.get_channel_data(video_info_data,comment_data)
    mongo_db.insert_data(video_data)
    return render_template('result.html', video_data=video_data)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)

