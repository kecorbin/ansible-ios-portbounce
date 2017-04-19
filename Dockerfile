FROM ubuntu
RUN apt-get update && apt-get -y install python python-pip gcc python-dev
COPY . /opt/ansible-scripts
WORKDIR /opt/ansible-scripts
RUN pip install -r requirements.txt
