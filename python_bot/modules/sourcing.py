import os
import yt_dlp

def download_videos(query: str, max_results: int = 1, output_dir: str = 'data/raw_videos', archive_file: str = 'data/download_history.txt') -> list:
    """
    Module 1: Auto-Sourcing
    Uses yt-dlp to search and download the top matching videos.
    Uses 'download_archive' to act as a memory bank so it NEVER downloads the same video twice.
    """
    os.makedirs(output_dir, exist_ok=True)
    downloaded_paths = []
    
    # Hook into the download process to capture the final filename
    def yt_hook(d):
        if d['status'] == 'finished':
            downloaded_paths.append(d['filename'])

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': f'{output_dir}/%(id)s_%(title)s.%(ext)s',
        'noplaylist': True,
        'download_archive': archive_file, # <--- The Magic Memory Anti-Repeat
        'max_downloads': max_results,
        'progress_hooks': [yt_hook],
    }

    print(f"[*] Searching YouTube for: '{query}'")
    print(f"[*] Skips previous downloads automatically using {archive_file}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Search the top 50. yt-dlp checks the archive, skips known ones,
        # and downloads 'max_results' (1) that is brand new!
        ydl.download([f'ytsearch50:{query}'])
        
    return downloaded_paths
