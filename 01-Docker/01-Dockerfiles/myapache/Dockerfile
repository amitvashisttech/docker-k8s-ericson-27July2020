# Base Image Name
FROM ubuntu:16.04

# Owner
MAINTAINER Amit Vashist <amitvashist7@outlook.com>

# Update the Repo.
RUN apt-get update

# Install Apache Packages 
RUN apt-get install apache2 -y 

# Bring up the Service
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
