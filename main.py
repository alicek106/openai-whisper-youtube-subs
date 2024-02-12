import os

from openai import OpenAI
from pytube import YouTube
from moviepy.editor import *


OPENAI_API_KEY = "sk-..."

if len(sys.argv) != 3:
    exit(-1)

youtube_link = sys.argv[1]
identifier = sys.argv[2]


def download_youtube():
    print("Downloading youtube..")
    if not os.path.exists(f"./{identifier}.mp4"):
        youtube_video = YouTube(youtube_link)
        youtube_video.streams.filter(file_extension='mp4').get_by_resolution('360p').download(output_path='.', filename=f'{identifier}.mp4')


# NOTE: ffmpeg should be available.
# > brew install ffmpeg
def convert_mp4_to_mp3():
    print("Converting from mp4 to mp3..")
    if not os.path.exists(f"./{identifier}.mp3"):
        video = VideoFileClip(os.path.join(f"./{identifier}.mp4"))
        video.audio.write_audiofile(os.path.join(f"./{identifier}.mp3"), bitrate='50k')


def transcribe():
    print("Transcribing to srt..")
    client = OpenAI(api_key=OPENAI_API_KEY)
    audio_file = open(f"./{identifier}.mp3", "rb")

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="srt",
    )

    with open(f'./{identifier}.srt', "w") as f:
        f.write(transcription)

    with open(f'./{identifier}.txt', "w") as f:
        f.write(__process_transcription(transcription))


def __process_transcription(transcription):
    blocks = transcription.split('\n\n')
    processed_lines = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            time_range = lines[1]
            text = lines[2]
            start_time = time_range.split(' --> ')[0]
            processed_line = f"[{start_time}] {text}"
            processed_lines.append(processed_line)

    return '\n'.join(processed_lines)


download_youtube()
convert_mp4_to_mp3()
transcribe()
