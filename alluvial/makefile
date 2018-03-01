.PHONY: default all
default: collect
# default: all
all: flow collect

.PHONY: flow collect
flow:
	python flow.py $(WHERE)

collect:
	python collect.py $(WHERE)
