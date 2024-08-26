from moviepy.editor import *
import os

# Path configurations
main_audio_file = 'Fact.mp3'
background_audio_file = 'background.mp3'
images_folder_shorts = 'scenes'
images_folder_video = 'scenes1'
output_video_shorts = 'output_shorts.mp4'
output_video = 'output_video.mp4'

# Load main audio file
main_audio = AudioFileClip(main_audio_file)

# Load background audio file and set its volume
background_audio = AudioFileClip(background_audio_file).volumex(0.1)  # Adjust volume as needed

# Adjust the duration of background audio to match the main audio
background_audio = background_audio.set_duration(main_audio.duration)

# Combine the main and background audio
combined_audio = CompositeAudioClip([main_audio, background_audio])

def create_video(images_folder, output_file, resolution):
    # Get images from the specified folder
    images = sorted([os.path.join(images_folder, img) for img in os.listdir(images_folder) if img.endswith(('.png', '.jpg', '.jpeg'))])

    # Create video clips from images
    clips = []
    for img in images:
        img_clip = ImageClip(img).set_duration(main_audio.duration / len(images)).resize(resolution)
        clips.append(img_clip)

    # Concatenate image clips
    video_clip = concatenate_videoclips(clips, method="compose")
    video_clip = video_clip.set_audio(combined_audio)

    # Write the result to a file
    video_clip.write_videofile(output_file, fps=24)

# Create the shorts video (1280x1920)
create_video(images_folder_shorts, output_video_shorts, (1280, 1920))

# Create the regular video (1280x720)
create_video(images_folder_video, output_video, (1280, 720))
