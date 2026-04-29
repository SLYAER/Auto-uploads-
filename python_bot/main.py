import time
import os
import random
import traceback
from modules.sourcing import download_videos, download_satisfying_background
from modules.slicing import slice_into_series
from modules.formatting import create_split_screen
from modules.upload import upload_short
from modules.ai_generator import get_ai_metadata
from keep_alive import keep_alive

def init_folders():
    directories = [
        'data/raw_videos', 
        'data/processed', 
        'data/ready_to_upload',
        'assets'
    ]
    for d in directories:
        os.makedirs(d, exist_ok=True)

def main_loop():
    keep_alive() # Starts Flask server for UptimeRobot
    print("=== 🤖 24/7 Viral Shorts Automation Bot Started 🤖 ===")
    init_folders()
    
    # The satisfies video at the bottom
    gameplay_video = "assets/gameplay_loop.mp4" 
    
    if not os.path.exists(gameplay_video):
        download_satisfying_background(gameplay_video)
        
    iteration = 1
    while True:
        try:
            print(f"\n=====================================")
            print(f"   [CYCLE {iteration}] Start")
            print(f"=====================================")
            
            # Use AI to decide what to search and upload
            ai_data = get_ai_metadata()
            query = ai_data["search_query"]
            print(f"[*] AI Chose Search Query: '{query}'")
            
            # 1. Download
            downloaded_paths = download_videos(query, max_results=1)
            if not downloaded_paths:
                print("[!] No videos downloaded. Retrying in 1 minute...")
                time.sleep(60)
                continue

            source_video = downloaded_paths[0]
            
            # 2. Slice into 55-second vertical chunks (Path A) 
            # (Chronological chunks keep the jokes intact better than random cutting)
            print("\n[*] Slicing source video...")
            sliced_clips = slice_into_series(source_video, chunk_len=55, output_dir='data/processed')
            
            # 3. Format & Upload loop
            total_clips = len(sliced_clips)
            print(f"\n[*] Generated {total_clips} unique clips from source.")
            
            for i, clip_path in enumerate(sliced_clips):
                final_output = f"data/ready_to_upload/cycle_{iteration}_part_{i+1}.mp4"
                
                print(f"\n[->] Creating & Uploading Clip {i+1} of {total_clips}")
                
                # Format to Split Screen
                create_split_screen(clip_path, gameplay_video, final_output)
                
                # Construct Metadata using AI
                title = ai_data['title']
                desc = ai_data['description']
                tags = ai_data['tags']
                
                # Upload
                upload_short(final_output, title, desc, tags)
                
                # Cleanup Chunk Memory to save Disk Space
                if os.path.exists(final_output): os.remove(final_output)
                if os.path.exists(clip_path): os.remove(clip_path)

                if os.environ.get("GITHUB_ACTIONS") == "true":
                    print("\n[GITHUB ACTIONS ENVIRONMENT DETECTED]")
                    print("[!] Uploaded 1 clip successfully. Exiting gracefully to save free-tier minutes.")
                    break # Break the 3-clip loop
                
                # 🔥 EXACTLY 10 MINUTE DELAY 🔥
                print("\n[⏳] Upload Success! Waiting exactly 10 minutes before the next upload...\n")
                time.sleep(600) 
            
            # Final Source Cleanup
            if os.path.exists(source_video):
                os.remove(source_video)

            if os.environ.get("GITHUB_ACTIONS") == "true":
                break # Break the infinite outer while-loop too

            iteration += 1

        except Exception as e:
            print(f"\n[ERROR] Crash in main loop: {str(e)}")
            traceback.print_exc()
            print("[⏳] Sleeping for 60 seconds before trying again...")
            time.sleep(60)

if __name__ == "__main__":
    main_loop()
