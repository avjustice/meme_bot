FROM python:3

# WORKDIR /meme_bot

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
# RUN python main.py
EXPOSE 8001
CMD [ "python", "main.py"]