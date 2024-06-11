install: run
	cd theme && npm i

run:
	cd theme && npx marp --theme-set "academic.css" -c "marp.config.js" "../example.md" -p --html

serve:
	cd theme && npx marp --theme-set "academic.css" -c "marp.config.js" "../" -p --html -s


