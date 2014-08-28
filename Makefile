
server: env
	. $</bin/activate; python app.py runserver

env: requirements.txt
	virtualenv $@
	. $@/bin/activate && pip install --requirement $< || (rm -r $@ && exit 1)

console: env
	bash --rcfile $</bin/activate; exit

syncdb: env
	. $</bin/activate; python app.py syncdb
