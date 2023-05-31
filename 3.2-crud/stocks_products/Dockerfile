FROM python:3.9

WORKDIR /src

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

COPY . .

COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf

RUN python manage.py collectstatic --noinput

EXPOSE 6050

CMD gunicorn stocks_products.wsgi -b 0.0.0.0:6050
