include .env

dev-run:
	cd ./deployment/docker && docker-compose -f docker-compose.dev.yml up -d --build
dev-rm:
	cd ./deployment/docker && docker-compose -f docker-compose.dev.yml rm
dev-log:
	cd ./deployment/docker && docker-compose -f docker-compose.dev.yml logs -f
dev-stop:
	cd ./deployment/docker && docker-compose -f docker-compose.dev.yml stop
dev-restart:
	cd ./deployment/docker && docker-compose -f docker-compose.dev.yml restart
dev-down:
	cd ./deployment/docker && docker-compose -f docker-compose.dev.yml down
run:
	cd ./deployment/docker && docker-compose -f docker-compose.yml -f ./docker-compose.prod.yml up -d --build
cert:
	cd ./deployment/docker && docker-compose -f docker-compose.cert.yml up --build
rm:
	cd ./deployment/docker && docker-compose -f docker-compose.yml -f ./docker-compose.prod.yml rm
log:
	cd ./deployment/docker && docker-compose -f docker-compose.yml -f ./docker-compose.prod.yml logs -f
stop:
	cd ./deployment/docker && docker-compose -f docker-compose.yml -f ./docker-compose.prod.yml stop
restart:
	cd ./deployment/docker && docker-compose -f docker-compose.yml -f ./docker-compose.prod.yml restart


.PHONY: dev-run dev-rm dev-log dev-stop dev-restart dev-down run cert rm log stop restart
