import cv2
from argparse import ArgumentParser
import os

def get_frame_count(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.release()
    return frame_count

def main():
    parser = ArgumentParser()
    parser.add_argument("--path", default="data")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        raise Exception("Path does not exist")
    
    videos = []

    if os.path.isdir(args.path):
        videos.extend([f for f in os.listdir(args.path) if f.endswith(".avi")])
    else:
        if args.path.endswith(".avi"):
            videos.append(args.path)

    if len(videos) == 0:
        raise Exception("No videos found. Check path.")
    
    print(f"Found {len(videos)} video{'s' if len(videos) > 1 else ''}")
    
    # Ensure all videos have the same length
    frame_count = get_frame_count(os.path.join(args.path, videos[0]))

    for video in videos:
        v_frame_count = get_frame_count(os.path.join(args.path, video))
        if frame_count != v_frame_count:
            raise Exception(f"Found mismatched number of frames for video: {video} compared to {videos[0]}")
    
    print(f"All videos have the same frame count of {frame_count}")


if __name__ == "__main__":
    main()