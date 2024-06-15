FROM debian:bullseye

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y python3-venv python3-pip hunspell-vi libenchant-2-2 \
    && pip3 install revscoring editquality scikit-learn==1.0.2
