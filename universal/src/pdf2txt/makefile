.PHONY: default main test
default: main

test:
	node test.js $(PDF)

main:
	node main.js $(PDF) $(PDF:.pdf=.txt)
