# YouTube Downloader App

A lightweight desktop application to download YouTube videos and audio in various formats and qualities using `yt-dlp` and `ffmpeg`. Built with Python and PyQt5, it offers an easy-to-use graphical interface for managing downloads.

## Features
- **Download Formats**: MP3 (audio) and MP4 (video).
- **Quality Options**: Best, Medium, Low, or Worst.
- **Custom Output Folder**: Choose where to save the downloads.
- **Pause/Stop Downloads**: Ability to stop ongoing downloads.
- **Multithreading**: Executes downloads in the background to keep the interface responsive.

## Requirements
- Python 3.8 or newer
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed
- [FFmpeg](https://ffmpeg.org/) installed and accessible (path configurable in the app)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-downloader-app.git
   cd youtube-downloader-app
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Install `yt-dlp`:
   ```bash
   pip install yt-dlp
   ```
4. Ensure `ffmpeg` is installed and provide its path in the app.

## Running the Application
Run the application with:
```bash
python youtube_downloader.py
```

## Usage
1. Enter the YouTube URL of the video you want to download.
2. Select the format (MP3 or MP4).
3. Choose the quality (Best, Medium, Low, Worst).
4. Specify the output folder (default: current working directory).
5. Click **Download** to start downloading.
6. To stop the download, click **Stop**.

## Configuration
- **FFmpeg Path**: Update the `ffmpeg_path` variable in the `YouTubeDownloaderApp` class to point to your `ffmpeg` executable.

## Screenshots
![App Screenshot](![image](https://github.com/user-attachments/assets/aaf13907-e2f0-4177-b185-05ed41ce6cf2))

## Troubleshooting
- Ensure `yt-dlp` and `ffmpeg` are correctly installed.
- Check the output folder path exists.
- If the app fails to launch, ensure all dependencies are installed.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)
