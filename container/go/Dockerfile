FROM alpine

LABEL maintainer="Xiewj<183778760@qq.com>"

ARG GOLANG_VERSION=1.12

WORKDIR /tmp

RUN sed -i 's/http:\/\/archive\.ubuntu\.com\/ubuntu\//http:\/\/mirrors\.163\.com\/ubuntu\//g' /etc/apt/sources.list

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get install -y wget \
	&& wget https://studygolang.com/dl/golang/go${GOLANG_VERSION}.linux-amd64.tar.gz \
	&& tar -zxf go1.12.linux-amd64.tar.gz -C /usr/local \
	&& rm go${GOLANG_VERSION}.linux-amd64.tar.gz
	
RUN echo "export GOPATH=/opt/go" >> ~/.bashrc \
	&& echo "export GOROOT=/usr/local/go" >> ~/.bashrc \
	&& echo "export GOARCH=amd64" >> ~/.bashrc \
	&& echo "export GOOS=linux" >> ~/.bashrc \
	&& echo "export GOBIN=$GOROOT/bin/" >> ~/.bashrc \
	&& echo "export GOTOOLS=$GOROOT/pkg/tool/" >> ~/.bashrc \
	&& echo "export PATH=$PATH:$GOBIN:$GOTOOLS" >> ~/.bashrc \
	&& source ~/.bashrc

CMD ["/bin/bash"]

EXPOSE 80 8080