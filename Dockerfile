FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY cfv_demo /app/cfv_demo/
EXPOSE 8080
ENTRYPOINT ["python","-m","cfv_demo"]
