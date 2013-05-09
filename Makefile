NOSEOPTS=--with-doctest
TESTTARGETS=.


alltest:
	make cleanpyc
	@echo "--- alltest: Running all tests except for web driver tests"
	nosetests $(NOSEOPTS) $(TESTTARGETS)

alltests: alltest


cleanpyc:
	@echo "--- cleanpyc: Removing *.pyc recursively"
	find . -name '*.pyc' -exec rm -f {} \;

cleanvendor:
	@echo "--- cleanvendor: Remove all vendor data"
	make -C scribe/data/vendor/* clean
	make -C webserver/public/vendor/* clean

clean: cleanpyc


fetchvendor:
	@echo "--- fetchvendor: Get exernal datafiles"
	make -C scribe/data/vendor/* fetch
	make -C `ls webserver/public/vendor/*/Makefile | sed 's/Makefile//g'` fetch


pep8:
	@pep8 . --repeat --filename=*.py,*.wsgi --exclude='*site_modules*'
