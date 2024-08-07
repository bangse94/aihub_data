import os
import os.path
import argparse
from tqdm import tqdm

def main(source_dir: str, target_dir: str, data_num: int) -> None:
    '''
    replace origin label files with modified label files
    
    Args:
        source_dir: str, path to the directory containing label files
        target_dir: str, path to the target directory to save modified label files
        data_num: int, number of data to be processed
        
    Returns:
        None
    '''
    
    for root, dirs, files in tqdm(list(os.walk(source_dir))):
        for file in files:
            if file.endswith(".txt"):
                print(file)
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                    
                with open(os.path.join(target_dir, file), 'w') as f:
                    for line in lines:
                        class_id, x, y, w, h = map(float, line.strip().split())
                        if data_num == 224:
                            if class_id == 0:
                                class_id = 1
                            else:
                                continue
                        else:
                            class_id = 0
                        f.write(f"{int(class_id)} {x} {y} {w} {h}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change label format")
    parser.add_argument("--source_dir", type=str, required=True, help="Path to the directory containing label files")
    parser.add_argument("--target_dir", type=str, required=True, help="Path to the target directory to save modified label files")
    parser.add_argument("--data_num", type=int, required=True, help="Number of data to be processed")
    
    args = parser.parse_args()
    main(args.source_dir, args.target_dir, args.data_num)
