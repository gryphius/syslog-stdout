# syslog-stdout

Minimalistic syslog which just prints all messages received from /dev/log to standard out.
This is useful in docker containers where you don't want to install a full blown syslog daemon, in combination with supervisord/supervisor-stdout.

example Dockerfile:

```
FROM centos:centos6
RUN yum install -q -y postfix python-setuptools
RUN easy_install supervisor supervisor-stdout syslog-stdout 
ADD supervisord.conf /etc/
CMD python -u /usr/bin/supervisord
EXPOSE 25
RUN postconf -e "inet_interfaces = all"
RUN newaliases
```

supervisord.conf:
```
[eventlistener:stdout]
command = supervisor_stdout
buffer_size = 100
events = PROCESS_LOG
result_handler = supervisor_stdout:event_handler
priority = 1

[program:syslog]
command=/usr/bin/syslog-stdout.py
stdout_events_enabled = true
stderr_events_enabled = true
priority = 10

[program:postfix]
process_name = master
directory = /etc/postfix
command = /usr/sbin/postfix -c /etc/postfix start
startsecs = 0
autorestart = false
priority = 50
```

