FROM python:3

WORKDIR /docker_build

ADD catfacts.py /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/catfacts.py"]
