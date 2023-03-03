mu:
	cd ./storage && python3 migrate_up.py


md:
	cd ./storage && python3 migrate_down.py

postgres:
	@docker-compose -f ./postgress/docker-compose.yml up

up:
	cd ./postgres && sudo docker-compose up
kill:
	sudo kill -9 $(sudo lsof -t -i:8000)