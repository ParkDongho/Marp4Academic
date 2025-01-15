cp -r "$THEME_PATH/soc_design/img" "$THEME_PATH/generated/img"
#cp -r "$THEME_PATH/PaperReader/assets/" "$THEME_PATH/generated/assets/"
#cp -r "$THEME_PATH/AIChipContest/img" "$THEME_PATH/generated/img"

TEXT_PATH="soc_design/slide" 
#TEXT_PATH="PaperReader/posts/semantic"
#TEXT_PATH="AIChipContest/slide"

python3 "$THEME_PATH/theme/scripts/markdown-multi-cols.py"       "$THEME_PATH/$TEXT_PATH" $THEME_PATH/generated/slide
python3 "$THEME_PATH/theme/scripts/markdown-dataview-remover.py" $THEME_PATH/generated/slide $THEME_PATH/generated/slide
python3 "$THEME_PATH/theme/scripts/graphical_abstract_gen.py"    $THEME_PATH/generated/slide $THEME_PATH/generated/slide
