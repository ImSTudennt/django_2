FROM python:3.9

COPY . /src

RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY .nginx/nginx.conf /etc/nginx/nginx.conf

ENV MY_ENV=netology

WORKDIR src

EXPOSE 6050

RUN python manage.py collectstatic --noinput

CMD gunicorn stocks_products.wsgi -b 0.0.0.0:6050
