FROM dask/base

RUN pip install ipython

ADD client.py /

CMD ["ipython", "-i", "/client.py"]
