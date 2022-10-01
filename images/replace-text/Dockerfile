FROM python:3 as test

WORKDIR /test

COPY requirements.txt *.py ./
RUN pip --no-cache-dir install --requirement requirements.txt
RUN python test.py

FROM python:3 as app

WORKDIR /app

COPY requirements.txt rt.py ./
RUN pip --no-cache-dir install --requirement requirements.txt

CMD ['python', 'rt.py']
