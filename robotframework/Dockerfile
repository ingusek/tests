FROM debian:11.3 as novnc

# Install git, supervisor, VNC, & X11 packages
RUN set -ex; \
    apt-get update; \
    apt-get install -y \
      bash \
      fluxbox \
      git \
      net-tools \
      novnc \
      supervisor \
      x11vnc \
      xterm \
      xvfb

# Setup demo environment variables
ENV HOME=/home/developer \
    DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    DISPLAY=:0.0 \
    DISPLAY_WIDTH=1024 \
    DISPLAY_HEIGHT=768 \
    RUN_XTERM=yes \
    RUN_FLUXBOX=yes
COPY . /app
RUN chmod +x /app/entrypoint.sh
EXPOSE 8080

FROM novnc

#Python
RUN set -ex; \
    apt-get update; \
    apt-get install -y \
      libglib2.0-0 \
      libnss3 \
      libgconf-2-4 \
      libfontconfig1 \
      python3 \
      unzip \
      wget \
      pip

#Chrome
RUN wget https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_linux64.zip && \
      unzip chromedriver_linux64.zip && \
      chmod +x chromedriver && \
      mv chromedriver /usr/bin/ && \
      rm chromedriver_linux64.zip

#Robot
RUN pip install \
      robotframework \
      robotframework-seleniumlibrary \
      robotframework-xvfb

#Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
      apt install -y ./google-chrome-stable_current_amd64.deb

ARG OWNER_ID
ARG GROUP_ID

RUN groupadd -g ${GROUP_ID} developer && useradd -d /home/developer -l -u ${OWNER_ID} -g developer developer && \
    install -g developer -o developer -d /home/developer && \
    chmod +x /app/entrypoint.sh && \
    chown -R developer:developer /app

WORKDIR /home/developer
USER developer

CMD ["/app/entrypoint.sh"]
