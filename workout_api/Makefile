.PHONY: run create-migrations run-migrations

run:
	@PYTHONPATH=$(PWD) uvicorn workout_api.main:app --host 127.0.0.1 --port 8000 --reload

create-migrations:
	@PYTHONPATH=$(PWD):$(PYTHONPATH) alembic revision --autogenerate -m "$(d)"

run-migrations:
	@PYTHONPATH=$(PWD):$(PYTHONPATH) alembic upgrade head
