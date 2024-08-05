# pre-conversion
python3 "$THEME_PATH/theme/scripts/markdown-multi-cols.py" $THEME_PATH/lab_meeting/slide/ $THEME_PATH/generated/slide

# generate marp slide
cd theme
npx marp --theme-set "$THEME_PATH/theme/academic.css" -c "$THEME_PATH/theme/marp.config.js" "$THEME_PATH/generated/" -s --html


