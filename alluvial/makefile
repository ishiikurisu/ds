.PHONY: default
default: filter_keywords

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

consultant: collect_from_source
	FLASK_APP=consultant.py flask run

test_duplicates:
	$(PY) test_duplicates.py $(WHERE) $(OP)

test_consultant: collect_from_source get-keywords
	$(PY) test_consultant.py $(WHERE)

get_relevant_keywords: collect_from_source get-keywords
	$(PY) get_relevant_keywords.py $(WHERE)

filter_keywords: get_relevant_keywords
	$(PY) filter_keywords.py $(WHERE)
