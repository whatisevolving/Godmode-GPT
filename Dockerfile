FROM python:3.11

WORKDIR /app
COPY scripts/ /app
COPY requirements.txt /app
COPY credentials/ /app/credentials

RUN pip install -r requirements.txt
EXPOSE 8080

ENV PORT 8080
ENV HOST 0.0.0.0

# Run app.py when the container launches
CMD ["python", "api.py"]
