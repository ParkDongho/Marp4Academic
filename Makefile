main: remove convert compile

remove:
	./scripts/remove.sh

convert: 
	./scripts/convert.sh

compile: remove convert
	./scripts/compile.sh

