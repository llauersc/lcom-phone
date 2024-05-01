FROM python:3.10

RUN pip install pipenv
COPY ./src /opt/app/src
COPY Pipfile /opt/app/
COPY Pipfile.lock /opt/app/

WORKDIR /opt/app/
ENV PYTHONUNBUFFERED=1

RUN pipenv install
WORKDIR /opt/app/src

CMD ["pipenv", "run", "hypercorn", "-k", "uvloop", "main:app", "-b", "0.0.0.0", "--reload"]