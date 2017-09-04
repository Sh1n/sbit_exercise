FROM python:2.7

WORKDIR /usr/src/app

COPY requirements.pip ./
RUN pip install --no-cache-dir -r requirements.pip

COPY . .
CMD [ "python", "./main.py"]