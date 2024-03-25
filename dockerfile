
FROM nvcr.io/nvidia/nvhpc:24.3-devel-cuda12.3-ubuntu20.04

RUN apt-get update

RUN apt-get install -y --no-install-recommends --fix-missing \
    python3 python3-pip python3-numpy

COPY ./extras/requirements.txt /

RUN pip install -r requirements.txt

RUN rm requirements.txt
