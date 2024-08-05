#!/bin/bash

# Train set
#SOURCE_DIR="/data/aihub/136.야간_사건사고_대응을_위한_버드아이뷰_IR열화상_데이터/01.데이터/1.Training/원천데이터"
#DEST_DIR="/data/aihub/night_data/train/images"

#for file in "$SOURCE_DIR"/*.zip; do
#	echo "Unzipping $file to $DEST_DIR"
#	unzip "$file" -d "$DEST_DIR"
#done
#
#echo "[Train]All files unzipped to $DEST_DIR"

# Valid set
SOURCE_DIR="/data/aihub/136.야간_사건사고_대응을_위한_버드아이뷰_IR열화상_데이터/01.데이터/2.Validation/원천데이터"
DEST_DIR="/data/aihub/night_data/valid/images"

for file in "$SOURCE_DIR"/*.zip; do
	echo "Unzipping $file to $DEST_DIR"
	unzip "$file" -d "$DEST_DIR"
done

echo "[Valid]All files unzipped to $DEST_DIR"
