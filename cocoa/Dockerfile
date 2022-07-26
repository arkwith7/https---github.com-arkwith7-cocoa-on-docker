# pull official base image
FROM ubuntu:20.04

# set work directory
RUN mkdir  /usr/src/app
WORKDIR  /usr/src/app

# set environment variables
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 카카오 ubuntu archive mirror server 추가. 다운로드 속도 향상
RUN sed -i 's@archive.ubuntu.com@mirror.kakao.com@g' /etc/apt/sources.list && \
    apt update -yqq

RUN apt -yqq install software-properties-common

RUN add-apt-repository ppa:alex-p/tesseract-ocr-devel -y

RUN apt -yqq update && \
    apt -yqq install build-essential && \
    apt -yqq install libffi-dev && \
    apt -yqq install libssl-dev && \
    # apt -yqq install ffmpeg libsm6 libxext6 && \
    apt -yqq install python3-dev && \
    apt -yqq install python3-pip && \
    apt -yqq install python-is-python3 && \
    apt -yqq install python3-opencv && \
    apt -yqq install netcat && \
    # apt -yqq install mysql-server && \
    # apt -yqq install default-libmysqlclient-dev && \
    apt -yqq install tesseract-ocr && \
    apt -yqq install tesseract-ocr-kor && \
    apt -yqq install tesseract-ocr-jpn && \
    apt -yqq install ghostscript && \
    apt -yqq install imagemagick && \
    apt -yqq install python3-psycopg2
    
RUN  pip install --upgrade pip --no-cache-dir && \
     pip install --upgrade setuptools --no-cache-dir && \
     pip install loguru --no-cache-dir && \
     pip install cryptography==2.6.1 --no-cache-dir && \
     pip install Pillow --no-cache-dir && \
     pip install easyocr --no-cache-dir && \
     pip install opencv-python --no-cache-dir && \
     pip install pytesseract --no-cache-dir && \
     pip install Image --no-cache-dir && \
     pip install pyyaml --no-cache-dir




# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir  -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# python3를 python으로 alias 설정
# RUN alias python='python3'

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
