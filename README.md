# AudioMouth

AudioMouth is a Python app that generates animated videos by syncing mouth movements with audio decibel levels. It processes an audio file and switches between two images (open and closed mouth) to create a lip-sync effect. The output video has a green background for easy chroma keying, making it ideal for video production workflows.

## Features
- Syncs mouth images to audio based on decibel levels.
- Produces 24fps animation.
- Outputs video with green screen background for chroma keying.
- Supports mp3 audio input and PNG image input.

## Installation

Before running the script, you need to install the required dependencies. You can do this by running:

```bash
pip install pydub opencv-python moviepy pillow numpy
```
## Usage

Simply add 1-4 images in the frames folder and modify the paths in the config.json to use the images you want.
Add the audios into the audio folder. If you're on Windows, now you can open run.bat and the output will be saved in the output folder.
If you're on Linux, simply run the main.py file.
```bash
python run.py
```
