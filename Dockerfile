FROM python:3.7

WORKDIR /app

RUN apt update && apt install -y libpq-dev --no-install-recommends && pip install --no-cache-dir requests PyGreSQL pyxlsb xlrd

CMD [ "python", "app.py" ]