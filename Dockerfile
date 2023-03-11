FROM python:3.11
RUN pip install pipenv
WORKDIR /src
COPY Pipfile /src
COPY Pipfile.lock /src
RUN pipenv install --deploy --system
RUN pipenv install --dev
COPY . /src
