.PHONY: default
default: collect_from_source

PY = python3
ifeq ($(OS), Windows_NT)
	PY = python
endif

.PHONY: collect_from_source filter get_ids consultant test_duplicates

collect_from_source:
	$(PY) collect_from_source.py $(WHERE)

filter: collect_from_source
	$(PY) filter.py $(WHERE) $(TARGET)

docs:
	pandoc -f markdown -t docx -o $(DOC:.md=.docx) $(DOC)

get-ids:
	$(PY) get_ids.py $(TARGET) $(TARGET:.csv=.txt)

get-keywords:
	$(PY) get_keywords.py $(WHERE)

consultant:
	FLASK_APP=consultant.py flask run

test_duplicates:
	$(PY) test_duplicates.py $(WHERE) $(OP)
