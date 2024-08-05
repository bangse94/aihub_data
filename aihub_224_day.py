import os
import shutil
import json
import argparse

def convert_annotation_to_yolo_format(annotation, image_width, image_height):
    yolo_annotation = []
    
    for ann in annotation:
        category_id = ann["category_id"]
        xmin = ann["bbox"]["xmin"]
        ymin = ann["bbox"]["ymin"]
        xmax = ann["bbox"]["xmax"]
        ymax = ann["bbox"]["ymax"]
        
        x_center = (xmin + xmax) / 2
        y_center = (ymin + ymax) / 2
        width = xmax - xmin
        height = ymax - ymin
        
        yolo_annotations.append(f"{category_id} {x_center/image_width} {y_center/image_height} {width/image_width} {height/image_height}")
    return yolo_annotations
    

def main(source_dir, target_dir):
    os.makedirs(target_dir + "/images", exist_ok=True)
    os.makedirs(target_dir + "/labels", exist_ok=True)
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file), "r") as f:
                    data = json.load(f)
                print(f"{root}, {file}")
                image_info = data['images'][0]
                annotations = data['annotations']
                image_width = image_info['width']
                image_height = image_info['height']
                image_file_name = image_info['file_name']
                
                image_path = os.path.join(root, image_file_name)
                if os.path.exists(image_path):
                    shutil.copy(image_path, os.path.join(target_dir, "images", image_file_name))
                
                yolo_annotations = convert_annotation_to_yolo_format(annotations, image_width, image_height)
                label_filename = image_file_name.replace(".jpg", ".txt")
                label_path = os.path.join(target_dir, 'labels', label_filename)
                
                with open(label_path, "w") as f:
                    for line in yolo_annotations:
                        f.write(line + "\n")
                        
    print("Transformation completed.")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert AIHub 224 Day dataset to YOLO format")
    parser.add_argument("--source_dir", type=str, required=True, help="Path to the AIHub 224 Day dataset")
    parser.add_argument("--target_dir", type=str, required=True, help="Path to the target directory")
    
    args = parser.parse_args()
    main(args.source_dir, args.target_dir)
