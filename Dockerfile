FROM python:3.7-alpine

COPY api_tests /bin/at-summer/api_tests
COPY config.json /bin/at-summer/config.json
COPY test_runner.py /bin/at-summer/test_runner.py
COPY Pipfile /bin/at-summer/Pipfile
COPY Pipfile.lock /bin/at-summer/Pipfile.lock

WORKDIR /bin/at-summer
RUN pip3 install pipenv
RUN pipenv install

COPY summer /bin/summer
ENTRYPOINT ["/bin/summer"]