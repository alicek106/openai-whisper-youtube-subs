# openai-whisper-youtube-subs

It downloads mp4 from youtube, extracts audio, and transcribe to `.srt` and `.txt` using openai whisper.

```bash
$ python3 main.py https://www.youtube.com/watch?v=Gm6dZ1q06ks tesla
...

$ ls -lash
...
 6656 -rw-r--r--   1 alicek106  wheel   2.3M  2 12 18:26 tesla.mp3
47528 -rw-r--r--   1 alicek106  wheel    23M  2 12 17:54 tesla.mp4
   16 -rw-r--r--   1 alicek106  wheel   5.0K  2 12 18:27 tesla.srt
    8 -rw-r--r--   1 alicek106  wheel   4.0K  2 12 18:35 tesla.txt

$ cat tesla.txt
...
[00:02:22,000] Yeah, we wanted to show a little bit more of what we've done over the past few months with the bot
[00:02:26,000] And just walking around and dancing on stage
[00:02:30,000] Just humble beginnings, but you can see the autopilot neural networks running as is, just retrained for the bot
[00:02:38,000] Directly on that new platform, that's my watering can
...

$ cat tesla.txt
...
18
00:02:38,000 --> 00:02:42,000
Directly on that new platform, that's my watering can
...

```

## How to use

- Change openai API token in main.py to yours
- Install dependencies and run python script

```bash
# if ffmpeg is not installed, run brew install ffmpeg
$ pip3 install -r requirements.txt

# how to use : python3 main.py <youtube url> <file identifier>
$ python3 main.py https://www.youtube.com/watch?v=Gm6dZ1q06ks tesla-blabla
```

## TODO
- As whisper limits max size of audio file to 25MB, large mp3 file should be splitted to a number of small file and merged after srt is created.

## See also
- [yashagarwal1411/SubtitlesForYoutube](https://github.com/yashagarwal1411/SubtitlesForYoutube) : you can use generated srt file directly in youtube.
