FROM ubuntu:18.04

LABEL MAINTAINER Xiewj<183778760@qq.com>

RUN sed -i 's/http:\/\/archive\.ubuntu\.com\/ubuntu\//http:\/\/mirrors\.163\.com\/ubuntu\//g' /etc/apt/sources.list

RUN apt-get update \
	&& apt-get install -y openssh-server \
	&& mkdir -p /var/run/sshd \
	&& mkdir -p /root/.ssh

RUN sed -ri 's/session required pam_ loginuid.so/#session required pam_loginuid.so/g' /etc/pam.d/sshd

ADD authorized_keys /root/.ssh/authorized_keys
ADD run.sh /run.sh
RUN chmod 755 /run.sh

EXPOSE 22

CMD ["/run.sh"]
