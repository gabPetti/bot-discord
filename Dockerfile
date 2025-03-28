FROM python:slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
