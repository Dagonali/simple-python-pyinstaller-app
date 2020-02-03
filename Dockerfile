FROM python:3.7-alpine0

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app
WORKDIR /app
CMD ["gunicorn", "-w 4", "main:app"]