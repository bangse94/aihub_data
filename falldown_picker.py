'''
    This script is used to pick the image and labels from the dataset
    
    version: 1.0
        - fall down situation
    author:
        - sjpark@mgensolutions.kr
'''


# import
import os
import os.path
import shutil
import argparse


def main(config):
    '''
        config : argparse.ArgumentParser()
            - img_src   (str) : source directory
            - img_dst   (str) : destination directory
            - label_src (str) : label source directory
            - label_dst (str) : label destination directory
    '''
    
    falldown = ["사람 대 자전거 사고상황", "사람 대 킥보드 사고상황", "쓰러짐 상황", "응급상황",
                "자전거 대 자전거 사고상황", "킥보드 대 자전거 사고상황", "킥보드 대 킥보드 사고상황"]
    
    # checck the directory
    if not os.path.exists(config.img_dst):
        os.makedirs(config.img_dst)
    if not os.path.exists(config.label_dst):
        os.makedirs(config.label_dst)
        
    # sarach the image and label
    dir_list = os.listdir(config.img_src)
    for dir in dir_list:
        if dir in falldown:
            search_file(dir, config.img_dst, config.label_dst)
    
def search_file(src_dir: str, img_dst: str, label_dst: str) -> None:
    '''This function is used to search the image and label file and copy to the destination directory
        src_dir   (str) : source directory
        img_dst   (str) : destination directory
        label_dst (str) : label destination directory
    '''

    # sarach and copy root directory
    for root, dirs, files in os.walk(src):
        for file in files:
            if not "NOR" in file.split("_"):
                continue
            
            if file.endswith("jpg"):
                shutil.copy(os.path.join(root, file), img_dst)
            if file.endswith("txt"):
                shutil.copy(os.path.join(root, file), label_dst)
    
    print(f"Searched and copied {src_dir} directory")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--src", type=str, default="data", help="source directory")
    args.add_argument("--label_src", type=str, default="label", help="label source directory")
    args.add_argument("--label_dst", type=str, default="fall_down_label", help="label destination directory")
    
    config = args.parse_args()
    
    main(config)