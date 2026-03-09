# Video utilities

1. Convert Video to Static Images
2. Convert Video to H265
3. Report a video inventory

### Prerequisites

1. Ensure you have Python installed (version 3.12+ recommended).
2. Install [uv](https://docs.astral.sh/uv/) for dependency management.
3. Install FFmpeg, as it is required for processing video files. Follow the instructions for your operating system:
   - **Linux:** `sudo apt install ffmpeg`
   - **macOS (Homebrew):** `brew install ffmpeg`
   - **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your `PATH`.

#### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/gibbok/video-utilities.git
   ```
2. Navigate to the project folder:
   ```bash
   cd video-utilities
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

## Convert Video to Static Images

This project allows you to extract static images (screenshots) from a video file at regular intervals.

- Supports input videos in `.mkv` and other common formats.
- Saves screenshots as sequentially numbered image files.
- Configurable screenshot intervals.

### Usage

```bash
make extract INPUT=/path/to/video.mkv OUTPUT=/path/to/output/folder INTERVAL=10
```

The screenshots will be saved in the specified output folder as `.png` files, named sequentially.

## Convert Video to H265

Compress a video to H265 format with medium settings.

### Usage

```bash
make compress INPUT=/path/to/video.mkv OUTPUT=/output
```

Notes: the script will save the output in `.mkv` format.

## Report a Video Inventory

Generate a CSV report of all video files in a directory with codec information and file sizes.

### Usage

```bash
make report FOLDER=/path/to/videos OUTPUT=inventory.csv
```

### License

This project is licensed under the MIT License.
