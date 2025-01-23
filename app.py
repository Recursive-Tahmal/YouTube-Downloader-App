from concurrent.futures import ThreadPoolExecutor
import os
import signal
import subprocess

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class YouTubeDownloaderApp(QtWidgets.QWidget):
    # Path to ffmpeg
    ffmpeg_path = "Add your ffmpeg path here"




    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(200, 200, 500, 400)

        # Initialize UI elements
        self.url_label = QtWidgets.QLabel("YouTube URL:")
        self.url_input = QtWidgets.QLineEdit()

        self.format_label = QtWidgets.QLabel("Select Format:")
        self.format_combo = QtWidgets.QComboBox()
        self.format_combo.addItems(["MP3", "MP4"])

        self.quality_label = QtWidgets.QLabel("Select Quality:")
        self.quality_combo = QtWidgets.QComboBox()
        self.quality_combo.addItems(["Best", "Medium", "Low", "Worst"])

        self.download_button = QtWidgets.QPushButton("Download")
        self.download_button.clicked.connect(self.start_download)

        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_download)
        self.stop_button.setEnabled(False)  # Disable initially

        self.output_label = QtWidgets.QLabel("Output Folder:")
        self.output_path = QtWidgets.QLineEdit(os.getcwd())  # Default to current working directory
        self.browse_button = QtWidgets.QPushButton("Browse")
        self.browse_button.clicked.connect(self.select_output_folder)

        self.status_label = QtWidgets.QLabel("")

        # Set up the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.format_label)
        layout.addWidget(self.format_combo)
        layout.addWidget(self.quality_label)
        layout.addWidget(self.quality_combo)
        layout.addWidget(self.output_label)

        output_layout = QtWidgets.QHBoxLayout()
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(self.browse_button)
        layout.addLayout(output_layout)

        layout.addWidget(self.download_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        # Thread pool executor for handling downloads
        self.executor = ThreadPoolExecutor(max_workers=4)
        self.future = None  # Store the future object for the download task
        self.is_stopped = False  # Flag to manage stopping
        self.download_process = None  # Store the current download process

        # Signal handling to gracefully handle CTRL+C
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signal, frame):
        """Handle the SIGINT signal (CTRL+C) to terminate gracefully."""
        if self.download_process:
            self.download_process.terminate()
        QtWidgets.QApplication.quit()

    def select_output_folder(self):
        """Open a dialog to select the output folder."""
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.output_path.setText(folder)

    def start_download(self):
        """Validate inputs and initiate the download process."""
        youtube_url = self.url_input.text()
        format_choice = self.format_combo.currentText()
        quality_choice = self.quality_combo.currentText().lower()
        output_folder = self.output_path.text()

        # Validate inputs
        if not youtube_url:
            QMessageBox.warning(self, "Error", "YouTube URL cannot be empty.")
            return

        if format_choice not in ["MP3", "MP4"]:
            QMessageBox.warning(self, "Error", "Invalid format selected.")
            return

        if not os.path.exists(output_folder):
            QMessageBox.warning(self, "Error", "Output folder does not exist.")
            return

        self.status_label.setText("Downloading...")
        self.download_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.is_stopped = False

        # Start the download in a separate thread
        self.future = self.executor.submit(self.download_video, youtube_url, format_choice, quality_choice, output_folder)

    def stop_download(self):
        """Stop the current download."""
        if self.download_process:
            self.download_process.terminate()  # Forcefully terminate the process
        self.is_stopped = True
        self.update_status("Stopping download...")

    def download_video(self, youtube_url, format_choice, quality_choice, output_folder):
        """Download the YouTube video in the selected format and quality using subprocess."""
        try:
            # Build the command for yt_dlp
            cmd = [
                "yt-dlp",
                "--ffmpeg-location", self.ffmpeg_path,
                "--output", os.path.join(output_folder, "%(title)s.%(ext)s"),
                "--format", quality_choice,
            ]

            if format_choice == "MP3":
                cmd.extend(["--extract-audio", "--audio-format", "mp3", "--audio-quality", "192"])

            cmd.append(youtube_url)

            # Start the subprocess
            self.download_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Read process output and monitor stop flag
            while True:
                output = self.download_process.stdout.readline()
                if output == b"" and self.download_process.poll() is not None:
                    break  # Process finished

                if self.is_stopped:
                    self.download_process.terminate()
                    self.update_status("Download stopped.")
                    return

            # Check exit code
            if self.download_process.returncode == 0:
                self.update_status("Download complete.")
            else:
                self.update_status("Download failed.")

        except Exception as e:
            self.update_status(f"Error: {str(e)}")

        finally:
            self.download_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.download_process = None  # Clear the process

    def update_status(self, message):
        """Update the status label in the main thread."""
        QtCore.QMetaObject.invokeMethod(
            self.status_label, "setText", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, message)
        )


if __name__ == "__main__":
    # Run the application
    app = QtWidgets.QApplication([])
    window = YouTubeDownloaderApp()
    window.show()
    app.exec_()
