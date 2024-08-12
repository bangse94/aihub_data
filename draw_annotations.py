import cv2
import os
import argparse


def main(image_dir: str, label_dir: str, target_dir: str) -> None:
    '''
    draw bounding boxes on images
    
    Args:
        image_dir: str, path to the directory containing images
        label_dir: str, path to the directory containing label files
        target_dir: str, path to the target directory to save modified label files
        
    Returns:
        None
    '''
    
    
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            print(file)
            if file.endswith(".jpg"):
                image = cv2.imread(os.path.join(root, file))
                height, width, _ = image.shape
                
                with open(os.path.join(label_dir, file.replace(".jpg", ".txt")), 'r') as f:
                    lines = f.readlines()
                
                for line in lines:
                    class_id, x, y, w, h = map(float, line.strip().split())
                    center_x = int(x * width)
                    center_y = int(y * height)
                    bbox_w = int(w * width)
                    bbox_h = int(h * height)
                    
                    x = int(center_x - bbox_w / 2)
                    y = int(center_y - bbox_h / 2)
                    w = int(bbox_w)
                    h = int(bbox_h)
                    print(x,y,w,h)
                    image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                cv2.imwrite(os.path.join(target_dir, file), image)
                


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw bounding boxes on images")
    parser.add_argument("--image_dir", type=str, required=True, help="Path to the directory containing images")
    parser.add_argument("--label_dir", type=str, required=True, help="Path to the directory containing label files")
    parser.add_argument("--target_dir", type=str, required=True, help="Path to the target directory to save modified label files")

    args = parser.parse_args()
    main(args.image_dir, args.label_dir, args.target_dir)
