# Dockerfile for Nginx webserver
FROM centos:centos7
LABEL maintainer="Eugene Chen & Jamaica Noriel"
RUN yum makecache fast
RUN yum install epel-release update -y
RUN yum install nginx -y
ADD index.html /usr/share/nginx/html/index.html
CMD ["chmod", "644" "/usr/share/nginx/html/index.html"]
EXPOSE 80
EXPOSE 22
CMD ["nginx", "-g", "daemon off;"]
