import os
import subprocess
import argparse
from pathlib import Path


def extract_screenshots(video_path, output_folder, interval=5):
    """
    Extracts screenshots from a video every `interval` seconds.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder where screenshots will be saved.
        interval (int): Time interval in seconds between screenshots.
    """
    # Ensure the output folder exists
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Construct the FFmpeg command
    output_pattern = os.path.join(output_folder, "screenshot_%04d.png")
    command = [
        "ffmpeg",
        "-i",
        video_path,  # Input file
        "-vf",
        f"fps=1/{interval}",  # Set frames per second based on interval
        output_pattern,  # Output file pattern
    ]

    try:
        # Run the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Screenshots saved to: {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Make sure FFmpeg is installed and in your PATH.")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Extract screenshots from a video file every few seconds."
    )
    parser.add_argument(
        "video_path", help="Path to the input video file (.mkv or other formats)."
    )
    parser.add_argument(
        "output_folder",
        help="Path to the output folder where screenshots will be saved.",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=5,
        help="Interval in seconds between screenshots (default: 5 seconds).",
    )

    args = parser.parse_args()

    # Extract screenshots based on the provided arguments
    extract_screenshots(args.video_path, args.output_folder, args.interval)
