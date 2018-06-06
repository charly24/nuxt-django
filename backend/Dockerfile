FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y mysql-client
ADD . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --dev
CMD ["pipenv", "run" ,"./teamfinder/manage.py", "migrate"]