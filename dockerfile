FROM python:3.12-slim 

WORKDIR /app 

COPY ./requirements.txt /app/requirements.txt  


RUN  pip install --no-cache-dir --upgrade -r /app/requirements.txt 

COPY  . /app 


EXPOSE 8000  


CMD ["gunicorn", "main:app", "--workers", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
