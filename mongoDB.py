from flask import Flask, render_template, request, jsonify
import json
import Channel_Logger
import pymongo

class mongoDB:
    def __init__(self):
        self.logger = Channel_Logger.Channel_Logger()

    def connection(self):
        """To build connection"""
        try:
            client = pymongo.MongoClient("mongodb+srv://kalyan:Kalyan123@cluster1.itvkeub.mongodb.net/?retryWrites=true&w=majority")
            self.logger.log("Mongo DB Connected Successfully ")
        except Exception as e:
            self.logger.log(str(e))
        return client

    def insert_data(self,video_data):
        """To insert data into the db"""
        client = self.connection()
        db = client["youtube_data"]
        coll = db["videos_data"]
        try:
            coll.insert_one(video_data)
            self.logger.log(" Data inserted into Mongo DB Successfully ")
        except Exception as e:
            self.logger.log(str(e))
        