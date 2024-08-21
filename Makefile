REGISTRY=ghcr.io/almazkun
IMAGE=sentimental
VERSION=0.1.0
CONTAINER=sentimental


runserver:
	pipenv run python manage.py runserver

lint:
	ruff check --fix -e .
	black .
	djlint . --reformat

run:
	docker run \
		--rm \
		--env-file .env \
		-p 8000:8000 \
		--name $(CONTAINER) \
		$(REGISTRY)/$(IMAGE):$(VERSION)

stop:
	docker stop $(CONTAINER)

build:
	docker build -t $(REGISTRY)/$(IMAGE):$(VERSION) .
	docker tag $(REGISTRY)/$(IMAGE):$(VERSION) $(REGISTRY)/$(IMAGE):latest

push:
	docker push $(REGISTRY)/$(IMAGE):$(VERSION)
	docker push $(REGISTRY)/$(IMAGE):latest
