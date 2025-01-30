run local db:
	docker compose -f docker-compose-local.yaml up db pgadmin
run local app:
	uvicorn src.main:app --reload
run dev:
	docker compose -f docker-copmse.local.yaml up --build
run prod:
	docker compose -f docker-copmse.local.yaml up --build
