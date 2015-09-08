FROM python:3

RUN pip install dask pyzmq dill
RUN pip install toolz
ADD sched.py /

EXPOSE 4444
EXPOSE 5555

CMD ["python", "sched.py"]
