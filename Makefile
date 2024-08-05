main: compile

compile:
	./scripts/compile.sh

run: install
	cd theme && npx marp --theme-set "academic.css" -c "marp.config.js" "../slide/example.md" -p --html

serve: install
	cd theme && PORT=5000 npx marp --theme-set "academic.css" -c "marp.config.js" "../slide/" -p --html -s

install: 
	cd theme && npm i

lab_meeting: install
	cd theme && npx marp --theme-set "academic.css" -c "marp.config.js" $(THEME_PATH)/slide/lab_meeting_23_07_19.md -p --html #-o converted.pdf

pre-convert:
	python3 $(THEME_PATH)/theme/scripts/markdown-multi-cols.py $(THEME_PATH)/lab_meeting/slide/ $(THEME_PATH)/generated

