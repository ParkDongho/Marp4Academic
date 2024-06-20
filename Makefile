run: install
	cd theme && npx marp --theme-set "academic.css" -c "marp.config.js" "../slide/example.md" -p --html

serve: install
	cd theme && PORT=5000 npx marp --theme-set "academic.css" -c "marp.config.js" "../slide/" -p --html -s


install: 
	cd theme && npm i
