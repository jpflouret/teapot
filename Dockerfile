FROM python:3.9.18-alpine
WORKDIR /app
COPY server.py .
expose 8080/tcp
CMD ["python", "-u", "/app/server.py"]
