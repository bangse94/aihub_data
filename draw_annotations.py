import cv2
import os

def draw_bounding_boxes(image_dir, label_dir):
    image_files = os.listdir(image_dir)
    label_files = os.listdir(label_dir)

    for label_file in label_files:
        image_file = label_file.replace(".txt", ".jpg")
        if image_file not in image_files:
            continue

        image_path = os.path.join(image_dir, image_file)
        label_path = os.path.join(label_dir, label_file)

        image = cv2.imread(image_path)
        height, width, _ = image.shape

        with open(label_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            class_id, x, y, w, h = map(float, line.strip().split())

            x = int((x - w/2) * width)
            y = int((y - h/2) * height)
            w = int(w * width)
            h = int(h * height)

            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Image with Bounding Boxes", image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

# Example usage
image_dir = "/path/to/images"
label_dir = "/path/to/labels"
draw_bounding_boxes(image_dir, label_dir)