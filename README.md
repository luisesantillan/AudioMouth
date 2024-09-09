# AudioMouth

AudioMouth is a Python app that generates animated videos by syncing mouth movements with audio decibel levels. It processes an audio file and switches between two images (open and closed mouth) to create a lip-sync effect. The output video has a green background for easy chroma keying, making it ideal for video production workflows.

## Features
- Syncs mouth images to audio based on decibel levels.
- Produces 24fps animation.
- Outputs video with green screen background for chroma keying.
- Supports mp3 audio input and PNG image input.

## Installation
Git clone the repository and install the required dependencies. You can do this by opening the command line in the AudioMouth folder and running:

```bash
git clone https://github.com/luisesantillan/AudioMouth
cd AudioMouth
pip install -r requirements.txt
```
## Usage
Simply add 1-4 images in the frames folder and modify the paths in the config.json to use the images you want.
Add the audios into the audio folder.

closed_mouth            |  closed_mouth_blinking            |  open_mouth            |  open_mouth_blinking
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![closed_mouth](https://github.com/user-attachments/assets/3ed0c597-df0e-4165-98d4-cf978e1338bb) | ![closed_mouth_blinking](https://github.com/user-attachments/assets/1296c2a7-4304-4935-b398-4ee5e1fe8a10) | ![open_mouth](https://github.com/user-attachments/assets/4715a73a-1a27-4ac9-a20b-954dde0aac0b) | ![open_mouth_blinking](https://github.com/user-attachments/assets/b7d04648-9158-4dd2-889c-27c67a64e0b2)

If you're on Windows, now you can open run.bat and the output will be saved in the output folder.
If you're on Linux, simply run the main.py file.

https://github.com/user-attachments/assets/dcf3728c-0d3b-455d-b17e-5e9819be069b



