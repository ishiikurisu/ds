CSV_REDUZIDO = "darkenergy_reduzido.csv"
CSV = "darkenergy.csv"


.PHONY: default
default: completo

.PHONY: reduzido
reduzido:
	python insightnet.py $(CSV_REDUZIDO)

.PHONY: completo
completo:
	python insightnet.py $(CSV)

clean:
ifeq ($(OS), Windows_NT)
	del *.gexf
else
	rm *.gexf
endif
