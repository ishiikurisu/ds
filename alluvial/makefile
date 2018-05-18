.PHONY: default
default: get_works

PY = python3
ifeq ($(OS), Windows_NT)
	PY = python
endif

.PHONY: collect_from_source filter get_ids consultant test_duplicates get_keywords

collect_from_source:
	$(PY) collect_from_source.py $(WHERE)

filter: collect_from_source balance
	$(PY) filter.py $(WHERE) $(TARGET)

docs:
	pandoc -f markdown -t docx -o $(DOC:.md=.docx) $(DOC)

get-ids:
	$(PY) get_ids.py $(TARGET) $(TARGET:.csv=.txt)

test_duplicates:
	$(PY) test_duplicates.py $(WHERE) $(OP)

balance: collect_from_source
	$(PY) balance.py $(WHERE)

percent_balance: balance collect_from_source
	$(PY) percent_balance.py $(WHERE)

get_works:
	$(PY) get_works.py $(WHERE)
