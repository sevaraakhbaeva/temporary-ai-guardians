FROM continuumio/miniconda3
EXPOSE 5000

RUN apt-get update
RUN apt-get --assume-yes install libasound2
RUN pip install azure-cognitiveservices-speech
RUN pip install -U Flask
RUN pip install werkzeug==0.16.0

RUN mkdir -p /app
COPY speech_processor.py /app
COPY server.py /app

WORKDIR /app

CMD python server.py