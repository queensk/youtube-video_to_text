#!/usr/bin/env python3
"""
youtube transcriber
"""
from youtube_transcript_api import YouTubeTranscriptApi
import sys


def get_video_id(url):
    """
    assuming the url is in the format https://www.youtube.com/watch?v=video_id
    """
    return url.split('=')[-1]


url = sys.argv[1]
video_id = get_video_id(url)
transcript = YouTubeTranscriptApi.get_transcript(video_id)
text = ""
for item in transcript:
    text += item['text'] + " "

with open("output.txt", "w") as f:
    f.write(text)
