import os
import shutil
import json
import argparse

def copy_files(source_dir: str, target_dir: str) -> None:
    pass
    
def main(source_dir: str, target_dir: str, data_num: int) -> None:
    
    if data_num == 224:
        mode = 1
    else:
        mode = 2
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_name = file.split(".")[0]
            file_name_list = file_name.split("_")
            if mode == 1:
                if file_name_list[1] == "NOR":
                    shutil.copy(os.path.join(root, file), os.path.join(target_dir, file))
            else:
                if file_name_list[2] == "IR":
                    shutil.copy(os.path.join(root, file), os.path.join(target_dir, file))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert AIHub 224 Day dataset to YOLO format")
    parser.add_argument("--source_dir", type=str, required=True, help="Path to the AIHub 224 Day dataset")
    parser.add_argument("--target_dir", type=str, required=True, help="Path to the target directory")
    parser.add_argument("--data_num", type=int, required=True, help="Number of data to be copied")
    
    args = parser.parse_args()
    main(args.source_dir, args.target_dir, args.data_num)