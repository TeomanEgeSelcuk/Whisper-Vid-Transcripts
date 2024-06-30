# Audio Transcription Converter

This project provides a Python script for automatically transcribing audio from video files. It utilizes FFmpeg for extracting audio from videos and Whisper for transcribing the extracted audio to text.

## Prerequisites

- Python 3.12
- FFmpeg
- Whisper

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Conda installed. If not, install it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
3. Create a Conda environment using the `environment.yaml` file provided in the repository:

```sh
conda env create -f environment.yaml
```

4. Activate the Conda environment:

```sh
conda activate audio-transcription-converter
```

## Usage

1. Place your video files in the `videos-to-be-transcribed` directory.
2. Run the script:

```sh
python transcribe_video.py
```

The script will process each video file in the `videos-to-be-transcribed` directory, extract the audio, transcribe it using Whisper, and save the transcription as a text file in the `transcribed-text` directory.

## Notes

* The script skips video files that have already been transcribed.
* Transcriptions are saved with the same base name as the video file but with a `.txt` extension.

## Troubleshooting

If you encounter any issues with FFmpeg or Whisper, ensure that they are correctly installed and accessible in your environment. You can test this by running `ffmpeg -version` and `whisper --version` in your terminal.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
