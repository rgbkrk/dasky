from dask.distributed import Worker
w = Worker(
    scheduler='tcp://scheduler:4444',
    port_to_workers=1234,
)
