# generate marp slide
cd theme
npx marp --theme-set "$THEME_PATH/theme/academic.css" -c "$THEME_PATH/theme/marp.config.js" "$THEME_PATH/generated/" -s --html --allow-local-files true


