import os
import subprocess
import argparse
from pathlib import Path


def convert_to_h265(video_path, output_folder):
    """
    Convert video to H.265 HEVC format.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder where the converted video will be saved.
    """
    # Ensure the output folder exists
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Extract the original video filename without extension
    input_filename = Path(video_path).stem
    h265_output_file = os.path.join(output_folder, f"{input_filename}_h265.mp4")

    # Construct the FFmpeg command for H.265 conversion
    command = [
        "ffmpeg",
        "-i",
        video_path,  # Input file
        "-c:v",
        "libx265",  # Use H.265 codec
        "-crf",
        "28",  # Set constant rate factor (quality)
        "-preset",
        "medium",  # Set encoding speed vs. compression tradeoff
        h265_output_file,  # Output file
    ]

    try:
        # Run the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Converted video saved to: {h265_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during H.265 conversion: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Make sure FFmpeg is installed and in your PATH.")

    return h265_output_file


def convert_to_mkv(video_path, output_folder):
    """
    Convert video to MKV format using stream copy mode.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder where the converted video will be saved.
    """
    # Ensure the output folder exists
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Extract the original video filename without extension
    input_filename = Path(video_path).stem
    mkv_output_file = os.path.join(output_folder, f"{input_filename}.mkv")

    # Construct the FFmpeg command for remuxing with stream copy
    command = [
        "ffmpeg",
        "-i",
        video_path,  # Input file
        "-c:v",
        "copy",  # Copy video stream without re-encoding
        "-c:a",
        "copy",  # Copy audio stream without re-encoding
        mkv_output_file,  # Output file in MKV format
    ]

    try:
        # Run the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Video remuxed and saved to: {mkv_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during MKV remuxing: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Make sure FFmpeg is installed and in your PATH.")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Convert video to H.265 and then remux to MKV"
    )
    parser.add_argument("video_path", help="Path to the input video file.")
    parser.add_argument(
        "output_folder",
        help="Path to the folder where the converted video will be saved.",
    )

    args = parser.parse_args()

    # Convert to H.265
    h265_output_file = convert_to_h265(args.video_path, args.output_folder)

    # Convert H.265 to MKV
    convert_to_mkv(h265_output_file, args.output_folder)
