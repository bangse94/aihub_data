#!/bin/bash

#read -p "Enter the source directory : " SOURCE_DIR

read -p "Enter the file name pattern (e.g., *_7358_*): " NAME_PATTERN

#read -p "Enter the images destination directory : " IMG_DESTINATION

#read -p "Enter the labels destination directory : " LBS_DESTINATION

SOURCE_DIR=/data/aihub/person_dataset/train/day_data

IMG_DESTINATION=/data/aihub/person_dataset/valid/day_data/images

LBS_DESTINATION=/data/aihub/person_dataset/valid/day_data/labels

find "$SOURCE_DIR/images" -type f -name "$NAME_PATTERN" -exec mv "{}" "$IMG_DESTINATION" \;

find "$SOURCE_DIR/labels" -type f -name "$NAME_PATTERN" -exec mv "{}" "$LBS_DESTINATION" \;

echo "Files matching '$NAME_PATTERN' have been moved to '$IMG_DESTINATION' and '$LBS_DESTINATION'."
