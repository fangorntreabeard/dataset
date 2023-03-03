FROM python:3.10.6

#RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
#
#ENV PYTHONPATH "/app"
#ENV PYTHONUNBUFFERED=1
#ENV PYTHONDONTWRITEBYTECODE=1
#
#WORKDIR /app
#
#COPY requirements.txt .
#COPY app /app
#
#RUN pip install -r requirements.txt
#CMD ["python3", "app/application.py"]

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app app
RUN export PYTHONPATH="${PYTHONPATH}:/code/"
VOLUME settings:./settings
RUN ls -a && cd app && ls -a
CMD [ "python3", "app/application.py" ]
#RUN pip install pipenv

#COPY Pipfile .
#COPY Pipfile.lock .

# так делать не нужно:
#RUN pipenv shell
#RUN pipenv install python-magic
#RUN pipenv install pandas
#RUN pipenv install asyncpg
#RUN pipenv install jinja2

# так делать не нужно:
# RUN pipenv shell
# RUN pipenv install

