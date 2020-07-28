# Base Image Name
FROM ubuntu:16.04

# Owner
MAINTAINER Amit Vashist <amitvashist7@outlook.com>

# Update the Repo.
RUN apt-get update

# Install Apache Packages 
RUN apt-get install apache2 -y 

# Introduce Custom web Page
COPY info.html /var/www/html/info.html

# Port Expose
EXPOSE 80
EXPOSE 3306
EXPOSE 8091

# Bring up the Service
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
