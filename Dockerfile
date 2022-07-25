FROM python:3.9-alpine

LABEL "title"="test-case"
LABEL "creator"="Misha"

WORKDIR ./python/test_for_infotecs

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD pytest -v