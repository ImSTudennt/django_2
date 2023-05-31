FROM python:3.8

COPY . /src

COPY ./requirements.txt /src/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt 

WORKDIR src

ENV MY_ENV=my

EXPOSE 6050

CMD gunicorn stocks_products.wsgi -b 0.0.0.0:6050
