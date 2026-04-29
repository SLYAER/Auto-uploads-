import os
from moviepy.editor import VideoFileClip
from scenedetect import open_video, SceneManager
from scenedetect.detectors import ContentDetector

def slice_into_series(video_path: str, chunk_len: int = 60, output_dir: str = 'data/processed') -> list:
    """ 
    Path A: Slices into chronological chunks (e.g. 60 seconds).
    Requires MoviePy for cutting. 
    """
    os.makedirs(output_dir, exist_ok=True)
    clip = VideoFileClip(video_path)
    base_name = os.path.basename(video_path).split('.')[0]
    
    chunk_paths = []
    # Iterate through the duration in 60s steps
    for i in range(0, int(clip.duration), chunk_len):
        start = i
        end = min(i + chunk_len, clip.duration)
        subclip = clip.subclip(start, end)
        
        out_path = os.path.join(output_dir, f"{base_name}_part_{int(start//chunk_len)+1}.mp4")
        subclip.write_videofile(out_path, codec="libx264", audio_codec="aac")
        chunk_paths.append(out_path)
        
    clip.close()
    return chunk_paths

def detect_rapid_scenes(video_path: str) -> list:
    """ 
    Path B: Detects rapid scene changes for compilations.
    JS Context: Returns an array of tuples [(start_time, end_time), ...]
    """
    video = open_video(video_path)
    scene_manager = SceneManager()
    
    # threshold 27.0 is standard. Lower = more sensitive to fast cuts.
    scene_manager.add_detector(ContentDetector(threshold=27.0))
    
    print(f"[*] Analyzing scenes for {os.path.basename(video_path)}...")
    scene_manager.detect_scenes(video, show_progress=True)
    
    # Returns list of Timecode objects (start, end)
    return scene_manager.get_scene_list()
