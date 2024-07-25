# pre-conversion
python3 "$THEME_PATH/theme/scripts/markdown-multi-cols.py" $THEME_PATH/lab_meeting/slide/ $THEME_PATH/generated

# generate marp slide
cd theme
npx marp --theme-set "$THEME_PATH/theme/academic.css" -c "$THEME_PATH/theme/marp.config.js" "$THEME_PATH/generated/lab_meeting_23_07_19.md.md" -p --html
