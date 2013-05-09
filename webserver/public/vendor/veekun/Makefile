# Fetch veekun pokedex media data
#

fetch:
	@echo "--- fetchvendor: Fetching veekun media data..."
	git clone http://git.veekun.com/pokedex-media.git
	mv pokedex-media/pokemon/sugimori/ sugimori
	rm -rf pokedex-media
	@echo "--- fetchvendor: ...done!"

clean:
	@echo "--- cleanvendor: Cleaning veekun media data..."
	rm -r sugimori
	@echo "--- cleanvendor: ...done!"
