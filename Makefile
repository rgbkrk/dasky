default: images

.PHONY: images base scheduler worker client

images: base scheduler worker client

base:
	docker build -t dask/$@ $@

scheduler: base
	docker build -t dask/$@ $@

worker: base
	docker build -t dask/$@ $@

client: base
	docker build -t dask/$@ $@
