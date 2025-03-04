# указываем версию пайтона
FROM python:3.11
#
COPY . /code
#
WORKDIR /code
#
RUN pip install -r requirements.txt
#
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]
