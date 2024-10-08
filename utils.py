from moviepy.editor import VideoFileClip

def save_wav_from_mp4(mp4_file, wav_file = "audio.wav"):
    # Load the video clip
    video_clip = VideoFileClip(mp4_file)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to a separate file
    audio_clip.write_audiofile(wav_file)

    # Close the video and audio clips
    audio_clip.close()
    video_clip.close()
    return wav_file