run:
	@echo "Starting Flask application..."
	set PYTHONPATH=src && flask run

test:
	@echo "Starting run tests..."
	set PYTHONPATH=src && pytest -s