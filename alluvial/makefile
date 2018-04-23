.PHONY: default
default: get-keywords

PY = python3
ifeq ($(OS), Windows_NT)
	PY = python
endif

.PHONY: collect_from_source filter get-ids

collect_from_source:
	$(PY) collect_from_source.py $(WHERE)

filter: collect_from_source
	$(PY) filter.py $(WHERE) $(TARGET)

docs:
	pandoc -f markdown -t docx -o $(DOC:.md=.docx) $(DOC)

get-ids:
	$(PY) get-ids.py $(TARGET) $(TARGET:.csv=.txt)

get-keywords:
	$(PY) get-keywords.py $(WHERE)
