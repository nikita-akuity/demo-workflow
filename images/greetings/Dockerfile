FROM python:3

WORKDIR /app

COPY requirements.txt greet.py ./
RUN pip --no-cache-dir install --requirement requirements.txt

CMD ['python', 'greet.py']
