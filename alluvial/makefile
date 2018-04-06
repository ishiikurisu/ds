.PHONY: default all
default: filter
all: compare_sources

PY = python3
ifeq ($(OS), Windows_NT)
	PY = python
endif

.PHONY: collect_from_raw collect_from_paycheck collect_from_source report_from_source report_from_raw compares_sources

collect_from_raw:
	$(PY) collect_from_raw.py $(WHERE)

collect_from_paycheck:
	$(PY) collect_from_paycheck.py $(WHERE)

collect_from_source:
	$(PY) collect_from_source.py $(WHERE)

report_from_source: collect_from_source
	$(PY) report_from_source.py $(WHERE)

report_from_raw: collect_from_raw
	$(PY) report_from_raw.py $(WHERE)

compares_sources: collect_from_source collect_from_raw
	$(PY) compare_sources.py $(WHERE)

.PHONY: consultant filter
filter: collect_from_source collect_from_raw
	$(PY) filter.py $(WHERE) $(TARGET)

consultant:
	FLASK_APP=consultant.py flask run
