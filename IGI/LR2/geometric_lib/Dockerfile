FROM python:3.11.7-alpine3.17

ENV LENGTH_VAL=14
COPY . /app
RUN chmod +x app/square.py
ENTRYPOINT [ "python3","app/square.py" ]