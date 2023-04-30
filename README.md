# youtube-video_to_text

This script extracts the transcript of a YouTube video and saves it to a text file.

## Requirements
- Python 3.x
- youtube_transcript_api

## Installation
Install the youtube_transcript_api package by running the following command:
```
pip install youtube_transcript_api
```
## Usage
1. Open a terminal window.
2. Navigate to the directory containing the youtube_transcript.py file.
3. Run the following command, replacing <youtube_video_url> with the URL of the YouTube video you want to extract the transcript from:

```
python youtube_transcript.py <youtube_video_url>
```
4. The script will extract the transcript of the video and save it to a text file called output.txt in the same directory as the script.
## Notes
The script assumes that the YouTube video URL is in the format https://www.youtube.com/watch?v=video_id.
The get_video_id() function extracts the video ID from the URL.
The YouTubeTranscriptApi.get_transcript() method retrieves the transcript of the video.
The script concatenates the text of each subtitle item into a single string and saves it to a text file.
