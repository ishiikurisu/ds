.PHONY: default all
default: collect
# default: all
all: flow collect flow3

.PHONY: flow collect flow3
flow:
	python flow.py $(WHERE)

collect:
	python collect.py $(WHERE)

flow3:
	python flow3.py $(WHERE)
