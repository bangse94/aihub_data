#!/bin/bash

# Night data 136
# Train set
SOURCE_DIR="/data/aihub/136.야간_사건사고_대응을_위한_버드아이뷰_IR열화상_데이터/01.데이터/1.Training/라벨링데이터"
DEST_DIR="/data/aihub/person_dataset/origin/night/train/labels"

for file in "$SOURCE_DIR"/*.zip; do
	echo "Unzipping $file to $DEST_DIR"
	unzip "$file" -d "$DEST_DIR"
done

echo "[Train]All files unzipped to $DEST_DIR"

# Valid set
SOURCE_DIR="/data/aihub/136.야간_사건사고_대응을_위한_버드아이뷰_IR열화상_데이터/01.데이터/2.Validation/라벨링데이터"
DEST_DIR="/data/aihub/person_dataset/origin/night/valid/labels"

for file in "$SOURCE_DIR"/*.zip; do
	echo "Unzipping $file to $DEST_DIR"
	unzip "$file" -d "$DEST_DIR"
done

echo "[Valid]All files unzipped to $DEST_DIR"


# Train set
SOURCE_DIR="/data/aihub/224.멀티_영상_동일_상황_및_객체_식별_데이터/01-1.정식개방데이터/Training/02.라벨링데이터"
DEST_DIR="/data/aihub/person_dataset/origin/day/train/labels"

for file in "$SOURCE_DIR"/*.zip; do
	echo "Unzipping $file to $DEST_DIR"
	unzip "$file" -d "$DEST_DIR"
done

echo "[Train]All files unzipped to $DEST_DIR"

# Valid set
SOURCE_DIR="/data/aihub/224.멀티_영상_동일_상황_및_객체_식별_데이터/01-1.정식개방데이터/Validation/02.라벨링데이터"
DEST_DIR="/data/aihub/person_dataset/origin/day/valid/labels"

for file in "$SOURCE_DIR"/*.zip; do
	echo "Unzipping $file to $DEST_DIR"
	unzip "$file" -d "$DEST_DIR"
done

echo "[Valid]All files unzipped to $DEST_DIR"
