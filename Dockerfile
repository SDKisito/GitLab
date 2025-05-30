FROM python:3.11-slim

RUN apt-get update && apt-get install -y \

    curl \
    bash \
    ca-certificates \
    gnupg \
    lsb-release \
    apt-transport-https \
    coreutils \
    && curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash \
    && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl \
    && apt-get clean



WORKDIR /app
COPY . /app



COPY requirements.txt .
EXPOSE 80

RUN pip install --no-cache-dir -r requirements.txt

