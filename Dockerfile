FROM python:3

ADD . /app
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt


CMD ["uvicorn", "mongodb_api.api:app", "--host", "0.0.0.0", "--port", "8000"]
