FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /pathvalidate
WORKDIR /pathvalidate
RUN python3 -m pip install . && chmod +x fuzz/fuzz.py