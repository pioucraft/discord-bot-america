FROM ubuntu:latest

RUN apt update 
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y

RUN pip install discord
RUN pip install youtube_dl
RUN pip install ffmpeg
RUN pip install pynacl

WORKDIR /usr/app/src

COPY main.py /usr/app/src
COPY users.json /usr/app/src	
	
CMD ["python3", "main.py"]
