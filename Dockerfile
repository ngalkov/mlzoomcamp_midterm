FROM python:3.9-slim

RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system  --deploy --ignore-pipfile && \
    rm -rf /root/.cache

COPY ["models", "./models"]
COPY ["predict.py", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen", "0.0.0.0:9696", "predict:app"] 
