FROM nginx:1.21-alpine

# RUN addgroup --system appgroup && adduser --system --disabled-password --group appgroup appuser

#USER appuser

RUN useradd -u 1001 appuser
# Change to non-root privilege
USER appuser

RUN rm /etc/nginx/conf.d/default.conf
COPY ./deploy/nginx/nginx.conf /etc/nginx/
