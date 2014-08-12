FROM centos:centos6
RUN yum install -q -y postfix python-setuptools
RUN easy_install supervisor supervisor-stdout syslog-stdout 
ADD supervisord.conf /etc/
CMD python -u /usr/bin/supervisord
EXPOSE 25
RUN postconf -e "inet_interfaces = all"
RUN newaliases
