FROM python:3

WORKDIR /app

COPY requirements.txt rt.py ./
RUN pip --no-cache-dir install --requirement requirements.txt

CMD ['python', 'rt.py']
