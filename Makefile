
prepare-dev:
	rm -rf application/static && rm -rf frontend/build/*


deploy:
	./infra/stop.sh
	./infra/build.sh
	./infra/restart.sh
