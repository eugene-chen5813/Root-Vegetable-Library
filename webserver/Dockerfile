# Dockerfile for Nginx webserver
FROM centos:centos7
LABEL maintainer="Eugene Chen & Jamaica Noriel"
RUN yum install update -y
RUN yum install nginx -y
# ADD index.html /usr/share/nginx/html/index.html
EXPOSE 80/tcp
CMD ["nginx", "-g daemon on;"]
