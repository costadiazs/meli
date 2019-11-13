FROM python:2.7
ENV PYTHON 1
RUN rm -rf /meli
RUN mkdir /meli
WORKDIR /meli
ADD . .
RUN pip install mysql-connector-python
