FROM python:3.6

ENV PYTHON 1
RUN rm -rf /meli
RUN mkdir /meli
WORKDIR /meli
ADD . /meli
RUN pip install mysql-connector-python
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#CMD ["python","./quickstart.py"]
