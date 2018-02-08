CSV_REDUZIDO = "darkenergy_reduzido.csv"
CSV = "darkenergy.csv"


default: reduzido

reduzido:
	python insightnet.py $(CSV_REDUZIDO)

completo:
	python insightnet.py $(CSV)

clean:
	rm *.gexf
