.PHONY: default obtain analyze compare
default: analyze

PY = python3
ifeq ($(OS), Windows_NT)
	PY = python
endif

obtain:
	$(PY) obtain.py $(CONFIG)

analyze:
	$(PY) analyze.py $(CONFIG)

compare: analyze
	$(PY) compare.py $(CONFIG)
