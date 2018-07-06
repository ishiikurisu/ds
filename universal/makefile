.PHONY: default
default: pydo

find_files = $(wildcard $(WHERE)/*.pdf)

.PHONY: pydo
pydo:
	python main.py $(WHERE)

.PHONY: do
do:
	$(foreach pdf, $(find_files), $(MAKE) -C ./src/pdf2txt PDF=$(pdf);)
