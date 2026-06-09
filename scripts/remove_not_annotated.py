from argparse import ArgumentParser
import yaml
import os
import shutil

def main():
    parser = ArgumentParser()
    parser.add_argument("--dataset_folder", default="C:\Git\JARVIS-HybridNet\datasets\AnnasOpenHandDataset")
    args = parser.parse_args()

    yaml_file = [os.path.join(args.dataset_folder, yaml_file) for yaml_file in os.listdir(args.dataset_folder) if yaml_file.endswith(".yaml")][0]
    with open(yaml_file, "r") as f:
        yaml_data = yaml.load(f, Loader=yaml.Loader)

    recordings = [os.path.join(args.dataset_folder, recording) for recording in yaml_data["Recordings"].keys()]
    
    for recording in recordings:
        video_folders = [os.path.join(recording, folder) for folder in os.listdir(recording)]

        annotated = []

        for folder in video_folders:
            old_annotations_file = os.path.join(folder, "annotations.csv")
            new_annotations_file = os.path.join(folder, "new_annotations.csv")
            with open(old_annotations_file, "r") as f:
                with open(new_annotations_file, "w") as f2:
                    for row in f:
                        if row.startswith("Frame_"):
                            row_split = row.split(",")
                            if all([a == "" or a=="0" for a in row_split[1:-1]]):
                                image_file = os.path.join(folder, row_split[0])
                                if os.path.exists(image_file):
                                    os.remove(image_file)
                            else:
                                annotated.append(row_split[0])
                                f2.write(row)
                        else:
                            f2.write(row)
            shutil.move(new_annotations_file, old_annotations_file)

if __name__ == "__main__":
    main()