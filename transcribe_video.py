import os
import subprocess

def extract_audio(video_path, audio_path):
    """
    Extract audio from a video file using FFmpeg.
    """
    command = f'ffmpeg -i "{video_path}" -vn -acodec pcm_s16le -ar 44100 -ac 2 "{audio_path}"'
    subprocess.run(command, shell=True, check=True)

def transcribe_audio(audio_path, output_text_path):
    """
    Transcribe audio using Whisper and save the output to a text file.
    """
    output_dir = os.path.dirname(output_text_path)
    command = f'whisper "{audio_path}" --output_dir "{output_dir}" --output_format txt'
    subprocess.run(command, shell=True, check=True)

def main():
    videos_dir = 'videos-to-be-transcribed'
    output_dir = 'transcribed-text'
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each video file in the videos directory
    for video_file in os.listdir(videos_dir):
        video_path = os.path.join(videos_dir, video_file)
        base_name, _ = os.path.splitext(video_file)
        audio_path = os.path.join(output_dir, f"{base_name}.wav")
        output_text_path = os.path.join(output_dir, f"{base_name}.txt")

        # Skip already transcribed videos
        if os.path.exists(output_text_path):
            print(f"Skipping {video_file}, transcription already exists.")
            continue

        try:
            # Extract audio
            print(f"Extracting audio from {video_file}...")
            extract_audio(video_path, audio_path)

            # Transcribe audio
            print(f"Transcribing {video_file}...")
            transcribe_audio(audio_path, output_text_path)

            print(f"Transcription for {video_file} completed and saved to {output_text_path}.")

        except subprocess.CalledProcessError as e:
            print(f"Error processing {video_file}: {e}")

if __name__ == "__main__":
    main()
