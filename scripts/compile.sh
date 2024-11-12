rm -rf "$THEME_PATH/generated/"
mkdir "$THEME_PATH/generated/"
cp -r "$THEME_PATH/AIChipContest/img/" "$THEME_PATH/generated/img/"

# pre-conversion
python3 "$THEME_PATH/theme/scripts/markdown-multi-cols.py" $THEME_PATH/AIChipContest/slide/ $THEME_PATH/generated/slide

# generate marp slide
cd theme
npx marp --theme-set "$THEME_PATH/theme/academic.css" -c "$THEME_PATH/theme/marp.config.js" "$THEME_PATH/generated/" -s --html --allow-local-files


