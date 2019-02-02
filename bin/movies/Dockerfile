FROM ubuntu:16.04

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y git curl apache2 
RUN apt-get install -y python 
RUN apt-get install -y python-pip
RUN apt-get install -y awscli
RUN apt-get install -y nano
RUN pip install --upgrade pip
RUN pip install boto3 
RUN pip install flask

# Install app
ADD src /var/

EXPOSE 5000

CMD [ "python", "/var/api-movies-latest.py" ]
#CMD [ "/bin/bash"]
