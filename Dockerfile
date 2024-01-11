FROM python:3.12

WORKDIR /app
COPY . /app


RUN python -m venv venv && \
    source venv/Scripts/activate && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py"]
