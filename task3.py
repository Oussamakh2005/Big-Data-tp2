import dask.dataframe as dd
import time
import os
import psutil
def get_mem_info(tag:str) :
    proc = psutil.Process(os.getpid())
    proc_mem = proc.memory_info()
    rss = proc_mem.rss / (1024 * 1024)
    print(f"{tag} Current Process Memory : {rss:.2f}MB")
def proc_with_dask(path : str) :
    start_time = time.perf_counter()
    ddf = dd.read_csv(path,blocksize=64e6)
    # Define operation laizly 
    mean_fare = ddf["fare_amount"].mean()
    min_fare = ddf["fare_amount"].min()
    max_fare = ddf["fare_amount"].max()

    res_mean , res_min , res_max = dd.compute(mean_fare,min_fare,max_fare)
    end_time = time.perf_counter() - start_time
    print(f"Global mean : {res_mean:.2f}$")
    print(f"Min fare {res_min}$")
    print(f"Max fare {res_max}$")
    print(f"Total time {end_time:.2f} second")
    get_mem_info("-")


proc_with_dask("./new-york-city-taxi-fare-prediction/train.csv")