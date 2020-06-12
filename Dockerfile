FROM python:3

WORKDIR /src

ADD main.py .
ADD functions.py .
ADD file.txt .


CMD [ "python", "./main.py" ]