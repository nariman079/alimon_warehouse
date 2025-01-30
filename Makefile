run local db:
	docker compose -f docker-compose-local.yaml up db pgadmin
run local app:
	uvicorn src.main:app --reload
