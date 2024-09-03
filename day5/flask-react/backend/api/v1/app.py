#!/usr/bin/env python3
'''
Flask App to handle the resolution of YouTube Video Urls and return a json response
'''
from flask import abort, Flask, jsonify, request, redirect
from pytube import YouTube
from flask_cors import CORS
import os


app = Flask(__name__)


@app.route('/api/v1/', methods=['GET'], strict_slashes=False)
def index() -> str:
    '''
    return a JSON payload
    '''
    return jsonify({'message': 'use /download/ endpoint'})


@app.route('/api/v1/download/', methods=['POST'], strict_slashes=False)
def download_video_post():
    try:
        data = request.json
        url = data['url']
        yt = YouTube(url)
        


@app.route('/api/v1/download/<video_id>', methods=['GET', 'POST'], strict_slashes=False)
def download_video(video_id) -> str:
    '''
    end-point to handle YouTube Video resolution and return a json response
    '''
    url = f'https://www.youtube.com/watch?v={video_id}'

    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4'.order_by('resolution').desc().first())
        audio =yt.streams.filter(audio_only=True)

        if not video and not audio:
            return jsonify({'error': 'No suitable video/audio streams'}), 404
        if not video and audio:
            return jsonify({'audio': 'audio streams available'})
        if video and not audio:
            return jsonify({'video': 'video streams available'})
    except:
        pass
