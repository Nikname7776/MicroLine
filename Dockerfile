FROM python:3.10

EXPOSE 1488

COPY echo_server/server.py server.py

CMD python ./server.py