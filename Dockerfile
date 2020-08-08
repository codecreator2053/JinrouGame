FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install flask
CMD ["python", "backend/api.py"]
