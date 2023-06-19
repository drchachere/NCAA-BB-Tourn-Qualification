FROM python:3.10-bookworm
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python3" ]
CMD ["app.py"]


