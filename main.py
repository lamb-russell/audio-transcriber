"""
This module provides functionality for transcribing audio files using the Whisper model. It is designed to be easily
used as a script or imported into other Python projects for audio transcription tasks.

The core of this module is the `process_audio_with_whisper` function, which takes an audio file path as input,
transcribes the audio content using OpenAI's Whisper model, and saves the transcription to a text file.

Features:
- Transcription of audio files using the Whisper model.
- Customizable output file path for transcriptions.
- Logging of process steps and errors for easier debugging and tracking.

Dependencies:
- whisper: The module uses OpenAI's Whisper model for transcribing audio. Ensure you have whisper installed.
- sys: Used for retrieving command-line arguments.
- os: Used for file and path operations.
- logging: Used for logging information and errors throughout the transcription process.

Usage:
As a script:
    Run this module from the command line, providing the path to the audio file as the first argument
    and optionally the path to the output text file as the second argument.
    ```
    python this_script.py path_to_audio_file [path_to_output_text_file]
    ```
    If the output file path is not specified, the transcription is saved in the same directory as the audio file
    with the same base name and a `.txt` extension.

As a module:
    Import the `process_audio_with_whisper` function from this module into your Python code and call it with the
    necessary arguments.
    ```python
    from this_module import process_audio_with_whisper
    process_audio_with_whisper(audio_file_path, output_file_path=None)
    ```

This module is designed to be simple to use yet flexible, allowing for easy integration into larger projects
or for use as a standalone script for quick audio transcription tasks.

Note: This module requires the Whisper model. The model size can be specified when loading the model (the default is "base").
Different model sizes ("tiny", "small", "medium", "large") offer trade-offs between speed and accuracy.
"""


import whisper
import sys
import os
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def process_audio_with_whisper(audio_file_path: str, output_file_path: str = None):
    """
    Transcribe the given audio file using the Whisper model and save the transcription to a text file.

    Args:
    audio_file_path (str): The path to the audio file to be transcribed.
    output_file_path (str, optional): The path where the transcription text file will be saved.
                                     Defaults to the same name as the audio file in the current directory.
    """


    try:
        # Resolve tilde in paths
        audio_file_path = os.path.expanduser(audio_file_path)
        if output_file_path:
            output_file_path = os.path.expanduser(output_file_path)
        else:
            # Default output file path to the current directory
            base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
            output_file_path = os.path.join(os.getcwd(), base_name + '.txt')

        # Load the Whisper model
        logging.info("Loading Whisper model...")
        model = whisper.load_model("base")  # You can choose other model sizes like "tiny", "small", "medium", or "large"

        # Process the audio file
        logging.info(f"Processing audio file: {audio_file_path}")
        result = model.transcribe(audio_file_path)

        # Save the transcription to a text file
        with open(output_file_path, 'w') as file:
            file.write(result["text"])
        logging.info(f"Transcription saved to {output_file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py path_to_audio_file [path_to_output_text_file]")
        sys.exit(1)

    audio_file_path = sys.argv[1]
    logging.info(f"audio file: {audio_file_path}")
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else None
    logging.info(f"output path: {output_file_path}")
    process_audio_with_whisper(audio_file_path, output_file_path)
    logging.info(f"Complete")
