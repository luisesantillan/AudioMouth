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
![image](https://imgur.com/a/vvoh2vI)

Simply add 1-4 images in the frames folder and modify the paths in the config.json to use the images you want.
Add the audios into the audio folder. If you're on Windows, now you can open run.bat and the output will be saved in the output folder.
If you're on Linux, simply run the main.py file.

https://github.com/user-attachments/assets/01d82d8f-7cad-4929-80b7-96cbc3bca781

