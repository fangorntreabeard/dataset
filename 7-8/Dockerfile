FROM python:3.10.6
COPY Pipfile .
COPY Pipfile.lock .
COPY app app
RUN pipenv install
CMD ["python3", "app/application.py"]
RUN cat Pipfile
RUN cd /app && ls -a
