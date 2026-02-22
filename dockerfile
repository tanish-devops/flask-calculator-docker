#base image
FROM python:3.12

#working dir
WORKDIR /calc

#copy
COPY . /calc

#run
RUN pip install -r requirements.txt

#port
EXPOSE 5000

#command
CMD ["python","./app.py"]

