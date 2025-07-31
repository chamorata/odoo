FROM odoo:18

USER root

RUN apt-get update && \
    apt-get install -y fonts-freefont-ttf && \
    apt-get install -y gsfonts && \
    apt-get clean

USER odoo