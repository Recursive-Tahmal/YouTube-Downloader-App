# YouTube Downloader App

A user-friendly desktop application built using PyQt5 for downloading YouTube videos and audio in various formats and qualities.

## Features

- Download videos in MP4 format.
- Extract audio as MP3 with customizable quality.
- Choose from different quality options: Best, Medium, Low, and Worst.
- Set your preferred output folder for downloads.

## Screenshots

![App Screenshot](https://github.com/user-attachments/assets/aaf13907-e2f0-4177-b185-05ed41ce6cf2)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/YouTube-Downloader-App.git
   cd YouTube-Downloader-App
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure FFmpeg is installed and accessible:

   - Download and configure [FFmpeg](https://ffmpeg.org/download.html).
   - Update the `ffmpeg_path` variable in the code to point to your FFmpeg installation.

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Enter the YouTube URL, select the desired format and quality, and set the output folder.

3. Click **Download** to start.

## Requirements

- Python 3.8 or higher
- PyQt5
- yt-dlp
- FFmpeg

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube downloading functionality.
- [FFmpeg](https://ffmpeg.org/) for audio and video processing.

