# django-sentimental
Django website with ML model for Sentiment Analysis


## Installation
1. Clone the repository
2. Install the requirements
```bash
    pipenv install
    pipenv shell
```
3. Run the server
```bash
    python manage.py runserver
```
4. Open the browser and go to http://127.0.0.1:8000/


## Usage
1. Enter the text in the text area.
2. Click on the "Analyze".


## Deploy
1. Install docker: https://docs.docker.com/engine/install/ubuntu/
2. Download image:
```bash
    docker pull docker pull ghcr.io/almazkun/sentimental:latest
```
3. Create and populate the .env file:
```bash
    touch .env
    echo "DJANGO_SECRET_KEY=your_secret_key" >> .env
    echo "DJANGO_DEBUG=your_debug" >> .env
    echo "DJANGO_ALLOWED_HOSTS=localhost" >> .env
    echo "DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:8000" >> .env
    echo "SENTIMENT_MODEL_PATH=./model.pkl" >> .env
```
3. Run the container:
```bash
    docker run --rm -d -p 80:8000 -env-file .env ghcr.io/almazkun/sentimental:latest
```
4. Open the browser and go to http://localhost/