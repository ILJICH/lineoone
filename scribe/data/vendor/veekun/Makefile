# Fetch veekun pokedex data
#

fetch:
	@echo "--- fetchvendor: Fetching veekun csv data..."
	git clone https://github.com/veekun/pokedex.git
	mv pokedex/pokedex/data/csv/ csv
	rm -rf pokedex
	@echo "--- fetchvendor: ...done!"

clean:
	@echo "--- cleanvendor: Cleaning veekun csv data..."
	rm -r cvs
	@echo "--- cleanvendor: ...done!"
