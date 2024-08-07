import cv2
import os


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
    
    gpu_image = cv2.cuda_GpuMat()
    
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith(".jpg"):
                image = cv2.imread(os.path.join(root, file))
                gpu_image.upload(image)
                
                h, w, _ = image.shape
                
                with open(os.path.join(label_dir, file.replace(".jpg", ".txt")), 'r') as f:
                    lines = f.readlines()
                
                for line in lines:
                    class_id, x, y, w, h = map(float, line.strip().split())
                    x1 = int((x - w/2) * w)
                    y1 = int((y - h/2) * h)
                    x2 = int((x + w/2) * w)
                    y2 = int((y + h/2) * h)
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                gpu_image.download(image)
                
                cv2.imwrite(os.path.join(target_dir, file), image)
                


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw bounding boxes on images")
    parser.add_argument("--image_dir", type=str, required=True, help="Path to the directory containing images")
    parser.add_argument("--label_dir", type=str, required=True, help="Path to the directory containing label files")
    parser.add_argument("--target_dir", type=str, required=True, help="Path to the target directory to save modified label files")

    args = parser.parse_args()
    main(args.image_dir, args.label_dir)