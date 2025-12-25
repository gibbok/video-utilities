import os
import csv
from pathlib import Path
from datetime import datetime

def find_videos_and_report(target_folder, output_csv):
    """
    Scan a folder for video files and generate a report.
    Usage: python3 video_report.py <folder_path> [output_csv]
    """
    # Common video extensions
    video_extensions = {
        '.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v',
        '.mpg', '.mpeg', '.3gp', '.ts', '.vob', '.ogv', '.mts', '.m2ts'
    }
    
    video_data = []

    # Walk through the directory recursively
    print(f"Scanning {target_folder} for video files...")
    
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = Path(root) / file
            
            # Check if file extension is a video format
            if file_path.suffix.lower() in video_extensions:
                try:
                    stats = file_path.stat()
                    
                    # Calculate size in MB
                    size_mb = round(stats.st_size / (1024 * 1024), 2)
                    
                    # Get creation date (formatted)
                    # Use st_birthtime on macOS (actual creation time), fallback to st_ctime
                    creation_time = getattr(stats, 'st_birthtime', stats.st_ctime)
                    creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
                    
                    video_data.append({
                        'path': str(file_path.absolute()),
                        'size_mb': size_mb,
                        'date_created': creation_date
                    })
                except Exception as e:
                    print(f"Could not process {file_path}: {e}")

    # Sort data by size DESC (largest files first)
    video_data.sort(key=lambda x: x['size_mb'], reverse=True)

    # Write to CSV
    headers = ['File Location Path', 'Size (MB)', 'Date of Creation']
    
    try:
        with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['path', 'size_mb', 'date_created'])
            # Write custom headers
            f.write(','.join(headers) + '\n')
            writer.writerows(video_data)
            
        print(f"Successfully created: {output_csv}")
        print(f"Total videos found: {len(video_data)}")
        
    except IOError as e:
        print(f"Error writing CSV: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python video_report.py <folder_path> [output_csv]")
        print("Example: poetry run python video_report.py /Users/gibbok/Desktop/video-test")
        sys.exit(1)
    
    folder_to_scan = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else 'video_inventory.csv'
    
    # Validate folder exists
    if not os.path.isdir(folder_to_scan):
        print(f"Error: '{folder_to_scan}' is not a valid directory")
        sys.exit(1)
    
    find_videos_and_report(folder_to_scan, output_filename)