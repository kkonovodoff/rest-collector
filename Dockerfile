FROM python:alpine3.12
WORKDIR /code
ENV FLASK_APP=src/server.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install pipenv
COPY . .
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 5000
CMD ["flask", "run"]