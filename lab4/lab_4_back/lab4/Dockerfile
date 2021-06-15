FROM python:3.9
EXPOSE 80
ENV PYTHONUNBUFFERED=1
WORKDIR /Users/d_osyko/Desktop/Web-labs/lab4/lab_4_back/lab4
COPY . /Users/d_osyko/Desktop/Web-labs/lab4/lab_4_back/lab4

COPY requirements.txt .
RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]