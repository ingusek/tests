FROM node:14.17.0

EXPOSE 80

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN npm config set unsafe-perm true
RUN chmod a+x /docker-entrypoint.sh
RUN mkdir -p /root/.cache

ENTRYPOINT [ "/docker-entrypoint.sh" ]
