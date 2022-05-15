flask:
	make -C src/python flask

frontend:
	npm install
	npm start

run:
	make frontend ; make flask
