import cv2
from argparse import ArgumentParser
import os
import ffmpeg

def main():
    parser = ArgumentParser()
    parser.add_argument("--input", default="")
    parser.add_argument("--input_file_format", type=str, default=".avi")
    parser.add_argument("--output", default="")
    parser.add_argument("--output_file_format", type=str, default=".mp4")
    parser.add_argument("--overwrite", action='store_true', default=False)
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise Exception(f"Input: {args.input} does not exist")
    
    if os.path.isdir(args.input):
        videos = [f"{args.input}/{filename}" for filename in os.listdir(args.input) if filename.endswith(args.input_file_format)]
    else:
        videos = [os.path.abspath(args.input)]

    if videos is None or len(videos) == 0:
        print(f"No videos were found in: {args.input}")

    os.makedirs(args.output, exist_ok=True)
    output_folder = os.path.abspath(args.output)

    for video in videos:
        output_filename = f"{output_folder}/{os.path.basename(os.path.splitext(video)[0])}{args.output_file_format}"
        if not args.overwrite and os.path.exists(output_filename):
            raise ValueError(f"Output file: {output_filename} already exists")
        print(f"Converting {video} into {output_filename}...")
        stream = ffmpeg.input(video)
        stream = ffmpeg.output(stream, output_filename)
        ffmpeg.run(stream)


if __name__ == "__main__":
    main()