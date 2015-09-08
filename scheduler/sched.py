#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dask.distributed import Scheduler

if __name__ == '__main__':
    s = Scheduler(
      port_to_workers=4444,
      port_to_clients=5555,
    )

    print("Scheduler up and ready!")
    print("For workers: {}".format(s.address_to_workers))
    print("For clients: {}".format(s.address_to_clients))

    # TODO: if/when a KeyboardInterrupt occurs, should we call s.close()
