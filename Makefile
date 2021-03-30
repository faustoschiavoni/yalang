pre: requirements.txt
	pip install -r requirements.txt

test:
	PYTHONPATH=. python -m unittest discover -v test

main: bin/main.py
	PYTHONPATH=. python bin/main.py

antlr4.jar:
	wget -O antlr4.jar https://www.antlr.org/download/antlr-4.9-complete.jar

generate: antlr4.jar yalang/generated yalang/Yalang.g4
	java -Xmx500M -cp $(shell pwd)/antlr4.jar:$(CLASSPATH) \
		org.antlr.v4.Tool \
		-Dlanguage=Python3 \
		-visitor \
		-o $(shell pwd)/yalang/generated \
		$(shell pwd)/yalang/Yalang.g4

.PHONY: pre test main generate
