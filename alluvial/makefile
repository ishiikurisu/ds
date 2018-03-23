.PHONY: default all
default: compares_sources
all: flow collect_from_raw flow3

PY = python3
ifeq ($(OS), Windows_NT)
	PY = python
endif

.PHONY: flow collect_from_raw flow3 collect_from_paycheck collect_from_source report_from_source compares_sources
flow:
	$(PY) flow.py $(WHERE)

collect_from_raw:
	$(PY) collect_from_raw.py $(WHERE)

flow3:
	$(PY) flow3.py $(WHERE)

collect_from_paycheck:
	$(PY) collect_from_paycheck.py $(WHERE)

collect_from_source:
	$(PY) collect_from_source.py $(WHERE)

report_from_source: collect_from_source
	$(PY) report_from_source.py $(WHERE)

compares_sources:
	$(PY) compare_sources.py $(WHERE)

.PHONY: consultant
consultant:
	FLASK_APP=consultant.py flask run
