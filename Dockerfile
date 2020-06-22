FROM ubuntu:18.04
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python3 python3-pip gunicorn3
WORKDIR /capstone
COPY Blogger .
RUN pip3 install -r requirements.txt
EXPOSE 8000
SHELL ["/bin/bash", "-c"]
CMD ["gunicorn3","-b","0.0.0.0:8000","app:app"]
