FROM python:3

WORKDIR /app

COPY requirements.txt count.py ./
RUN pip --no-cache-dir install --requirement requirements.txt

CMD ['python', 'count.py']
