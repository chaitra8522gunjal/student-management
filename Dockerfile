
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .             

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]




# FROM python:3.12-slim —     Python environment provide karta hai.
# WORKDIR /app —     container ke andar working directory set karta hai.
# COPY requirements.txt . —     dependencies ki file copy karta hai.
# RUN pip install ... —     FastAPI aur Uvicorn install karta hai.
# COPY main.py . —      tumhari API ki Python file copy karta hai.
# CMD [...] —       container start hone par Uvicorn server run karta hai.
# --host 0.0.0.0 —      container ke bahar se API tak pahunchne ke liye server ko sabhi container interfaces par listen karwata hai.






# ye code pehale practice ke liye tha github action ke liye 
# FROM python:3.12-slim

# WORKDIR /app

# COPY student.py .

# CMD ["python", "student.py"]
