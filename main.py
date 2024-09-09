import os, random, json
import numpy as np
from pydub import AudioSegment
from pydub.utils import make_chunks
from PIL import Image
import cv2
from moviepy.editor import VideoClip, AudioFileClip

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Load the images
closed_mouth_img = Image.open(config['frame_paths']['closed_mouth'])
open_mouth_img = Image.open(config['frame_paths']['open_mouth'])
closed_mouth_blinking_img = Image.open(config['frame_paths']['closed_mouth_blinking'])
open_mouth_blinking_img = Image.open(config['frame_paths']['open_mouth_blinking'])

# Create a background with the color from config
background_color = tuple(config['background_color'])
background = Image.new('RGBA', closed_mouth_img.size, background_color)

# Composite the images with the background
closed_mouth_img = Image.alpha_composite(background, closed_mouth_img)
open_mouth_img = Image.alpha_composite(background, open_mouth_img)
closed_mouth_blinking_img = Image.alpha_composite(background, closed_mouth_blinking_img)
open_mouth_blinking_img = Image.alpha_composite(background, open_mouth_blinking_img)

# Convert images to OpenCV format
closed_mouth_cv = cv2.cvtColor(np.array(closed_mouth_img), cv2.COLOR_RGBA2RGB)
open_mouth_cv = cv2.cvtColor(np.array(open_mouth_img), cv2.COLOR_RGBA2RGB)
closed_mouth_blinking_cv = cv2.cvtColor(np.array(closed_mouth_blinking_img), cv2.COLOR_RGBA2RGB)
open_mouth_blinking_cv = cv2.cvtColor(np.array(open_mouth_blinking_img), cv2.COLOR_RGBA2RGB)

# Decide whether to blink
def should_blink(t, last_blink_time):
    if t - last_blink_time > random.uniform(config['minimum_blinking_delay'],config['maximum_blinking_delay']):
        return True
    return False

blink_duration = config['blink_duration']
last_blink_time = config['initial_blink_time']

# Set parameters
frame_rate = config['frame_rate']
frame_duration_ms = config['frame_duration_ms'] // frame_rate

for audio_file in os.listdir(config['audio_path']):
    # Load the audio
    audio_path = os.path.join(config['audio_path'], audio_file)
    audio = AudioSegment.from_file(audio_path)

    # Split the audio into chunks
    audio_chunks = make_chunks(audio, frame_duration_ms)

    # Function to calculate decibels of a chunk
    def calculate_decibels(chunk):
        return chunk.dBFS

    # Threshold from config
    decibel_threshold = config['decibel_threshold']

    # Function to generate frames
    def make_frame(t):
        global last_blink_time
        frame_index = int(t * frame_rate)

        if should_blink(t, last_blink_time):
            last_blink_time = t

        if 0 <= (t - last_blink_time) <= blink_duration:
            if frame_index < len(audio_chunks):
                chunk = audio_chunks[frame_index]
                decibels = calculate_decibels(chunk)
                
                return open_mouth_blinking_cv if decibels > decibel_threshold else closed_mouth_blinking_cv
            else:
                return closed_mouth_blinking_cv
        
        if frame_index < len(audio_chunks):
            chunk = audio_chunks[frame_index]
            decibels = calculate_decibels(chunk)
            
            return open_mouth_cv if decibels > decibel_threshold else closed_mouth_cv
        else:
            return closed_mouth_cv

    # Create a video clip
    video_clip = VideoClip(make_frame, duration=len(audio_chunks) / frame_rate)

    # Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video to the loaded audio
    video_with_audio = video_clip.set_audio(audio_clip)

    # Write the final video with audio
    output_video_path = os.path.join(config['output_path'], f"{audio_file.split('.')[0]}.mp4")
    video_with_audio.write_videofile(output_video_path, fps=frame_rate, codec=config['codec'], audio_codec=config["audio_codec"])

print("Animation created successfully!")