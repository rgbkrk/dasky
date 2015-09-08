from dask.distributed import Client

c = Client('tcp://scheduler:5555')
