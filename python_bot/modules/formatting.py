import os
import random
from moviepy.editor import VideoFileClip, clips_array, CompositeVideoClip, TextClip

def create_split_screen(top_clip_path: str, bottom_clip_path: str, output_path: str):
    """
    Module 3: Editing & Formatting
    Creates the viral 9:16 layout: Main clip on top, satisfy looping video on bottom.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 1. Load Top Video and crop it to 1080x960 (half of 1080x1920)
    top_clip = VideoFileClip(top_clip_path).resize(width=1080)
    top_clip = top_clip.crop(x_center=top_clip.w/2, y_center=top_clip.h/2, width=1080, height=960)
    
    # 2. Load Bottom Video (e.g. GTA 5 / Subway Surfers / Blox Fruits) and crop
    bottom_clip = VideoFileClip(bottom_clip_path).resize(width=1080)
    bottom_clip = bottom_clip.crop(x_center=bottom_clip.w/2, y_center=bottom_clip.h/2, width=1080, height=960)
    
    # 3. Handle Timings - loop bottom clip if it's too short
    if bottom_clip.duration < top_clip.duration:
        # MoviePy's loop doesn't always perform perfectly on audio-embedded clips, 
        # so removing audio from background video is safer.
        bottom_clip = bottom_clip.without_audio().loop(duration=top_clip.duration)
    else:
        bottom_clip = bottom_clip.without_audio().subclip(0, top_clip.duration)
        
    # 4. Stack them
    final_clip = clips_array([[top_clip], [bottom_clip]])
    
    # Optional Text Overlay (Needs ImageMagick config)
    try:
        # Just an example of how you'd inject the text
        txt = TextClip("Wait for it...", fontsize=80, color='yellow', stroke_color='black', stroke_width=4, font='Impact')
        txt = txt.set_position(('center', 'top')).set_duration(final_clip.duration).margin(top=100, opacity=0)
        final_clip = CompositeVideoClip([final_clip, txt])
    except Exception as e:
        print("[WARNING] ImageMagick not installed/detected. Skipping text overlay.")
        pass

    # 5. Render
    print(f"[*] Rendering Split Screen Video: {os.path.basename(output_path)}...")
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=4)
    
    top_clip.close()
    bottom_clip.close()
    return output_path
