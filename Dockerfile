FROM python:3
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8001
CMD [ "python", "main.py"]