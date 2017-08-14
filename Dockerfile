FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Add requirements
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt

RUN git clone -b develop https://github.com/HelloDHLyn/tinyweb /usr/src/tinyweb
RUN pip install -e /usr/src/tinyweb

# Add application
ADD . /usr/src/app
