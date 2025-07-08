FROM python:3.12-slim

WORKDIR /api

COPY api.py ./

RUN apt-get update && apt-get -y install curl && \
    pip install --upgrade pip && \
    pip install Flask requests && \
    useradd -ms /bin/bash flask && \
    chown -R flask /api
    
EXPOSE 5010

ENV FLASK_APP=api.py

USER flask

HEALTHCHECK --interval=2s --timeout=2s --start-period=2s --retries=2 \
  CMD curl -f http://localhost:5010/ || exit 1

CMD ["flask", "run", "--host=0.0.0.0", "--port=5010"] 

