# AI Audio Transcriber

Welcome to the Whisper Audio Transcription repository! This project utilizes OpenAI's powerful Whisper model to transcribe audio files into text. It's designed to be user-friendly, allowing both developers and non-technical users to easily transcribe audio files with minimal setup.

## Features

- **Audio Transcription:** Transcribe your audio files to text using the state-of-the-art Whisper model.
- **Customizable Output:** Choose where to save your transcription results.
- **Easy to Use:** Run as a standalone script or integrate into your projects.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.6 or later

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/lamb-russell/audio-transcriber.git
cd audio-transcriber
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies, including the Whisper package.

### Usage

#### As a Script

To use the script from the command line, navigate to the repository's directory and run:

```bash
python main.py path_to_audio_file [path_to_output_text_file]
```

- `path_to_audio_file` is the path to the audio file you want to transcribe.
- `path_to_output_text_file` is an optional argument specifying where to save the transcription. If not provided, the transcription will be saved in the same directory as the audio file, with the same name but a `.txt` extension.

#### As a Module

You can also import and use the `process_audio_with_whisper` function in your own Python projects:

```python
from main import process_audio_with_whisper

process_audio_with_whisper(audio_file_path, output_file_path=None)
```

## Contributing

Contributions to the Whisper Audio Transcription project are welcome! Please feel free to submit pull requests or create issues for bugs, questions, and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- OpenAI's Whisper model for providing the transcription capabilities.
- The Python community for maintaining such robust libraries and tools.

## Support

For support, you can open an issue in the GitHub repository or contact the maintainers directly.

---

Thank you for trying out Whisper Audio Transcription. Happy transcribing!
