
FROM python:3.12-slim

WORKDIR /app

COPY student.py .

CMD ["python", "student.py"]
