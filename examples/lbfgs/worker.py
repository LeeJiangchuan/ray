import argparse

import ray
import ray.worker as worker

import ray.arrays.remote as ra
import ray.arrays.distributed as da

import functions

parser = argparse.ArgumentParser(description="Parse addresses for the worker to connect to.")
parser.add_argument("--scheduler-address", default="127.0.0.1:10001", type=str, help="the scheduler's address")
parser.add_argument("--objstore-address", default="127.0.0.1:20001", type=str, help="the objstore's address")
parser.add_argument("--worker-address", default="127.0.0.1:40001", type=str, help="the worker's address")

if __name__ == "__main__":
  args = parser.parse_args()
  worker.connect(args.scheduler_address, args.objstore_address, args.worker_address)

  ray.register_module(functions)

  ray.register_module(ra)
  ray.register_module(ra.random)
  ray.register_module(ra.linalg)
  ray.register_module(da)
  ray.register_module(da.random)
  ray.register_module(da.linalg)

  worker.main_loop()
