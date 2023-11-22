FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip
#RUN pip install flask

#COPY *.* /opt/app
COPY requirements.txt /opt/app/
 
WORKDIR = /opt/app/

RUN pip install -r /opt/app/requirements.txt 

COPY . /opt/app/

ENTRYPOINT FLASK_APP=/opt/app/app.py flask run --host=0.0.0.0
