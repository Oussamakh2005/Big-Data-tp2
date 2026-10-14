import time
import pandas as pd
import psutil
import os
def get_mem_info(tag:str) :
    proc = psutil.Process(os.getpid())
    proc_mem = proc.memory_info()
    rss = proc_mem.rss / (1024 * 1024)
    print(f"{tag} Current Process Memory : {rss:.2f}MB")

def process_in_chunks(path:str) :
    total_rows = 0
    total_fare_sum = 0.0
    chunk_count = 0
    start_time = time.perf_counter()
    for chunk in pd.read_csv(path,chunksize=100000) : 
        chunk_count += 1
        if "fare_amount" in chunk :
            fares = chunk["fare_amount"].dropna()
            total_rows += len(fares)
            total_fare_sum += fares.sum()
        if chunk_count % 50 == 0 :
            print(f"Processed {chunk_count} chunk , {chunk_count * 100000:,} row scanned")
    global_mean = total_fare_sum / total_rows if(total_rows) else 0 
    end_time = time.perf_counter() - start_time
    print(f"Total rows scanned : {total_rows:,}")
    print(f"Global fares mean : {global_mean:.2f}$")
    print(f"Total time : {end_time} second")
    get_mem_info("-")

process_in_chunks("./new-york-city-taxi-fare-prediction/train.csv")