#!/bin/bash

# Train set
SOURCE_DIR="/data/aihub/224.멀티_영상_동일_상황_및_객체_식별_데이터/01-1.정식개방데이터/Training/02.라벨링데이터"
DEST_DIR="/data/aihub/dayt_data/train/labels"

for file in "$SOURCE_DIR"/*.zip; do
	echo "Unzipping $file to $DEST_DIR"
	unzip "$file" -d "$DEST_DIR"
done

echo "[Train]All files unzipped to $DEST_DIR"

# Valid set
SOURCE_DIR="/data/aihub/224.멀티_영상_동일_상황_및_객체_식별_데이터/01-1.정식개방데이터/Validation/02.라벨링데이터"
DEST_DIR="/data/aihub/day_data/valid/labels"

for file in "$SOURCE_DIR"/*.zip; do
	echo "Unzipping $file to $DEST_DIR"
	unzip "$file" -d "$DEST_DIR"
done

echo "[Valid]All files unzipped to $DEST_DIR"
