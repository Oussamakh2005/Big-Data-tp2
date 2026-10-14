import os 
import psutil
import time
import pandas as pd

def get_mem_info(tag:str) :
    proc = psutil.Process(os.getpid())
    proc_mem = proc.memory_info()
    rss = proc_mem.rss / (1024 * 1024)
    print(f"{tag} Current Process Memory : {rss:.2f}MB")

def read_csv_file(path : str) :
    print(f"File size {os.path.getsize(path) / (1024 ** 3):.2f}GB")
    print(f"Start uploading {path} to the memory")
    get_mem_info("Before Reading")
    try : 
        start_reading = time.perf_counter()
        df = pd.read_csv(path)
        end_reading = time.perf_counter() - start_reading
        get_mem_info("After Successfully Reading")
        print(f"dataset uploaded successuflly {df.shape}")
        print(f"Total reading time {end_reading}second")
    except MemoryError as e :
        print("Memory error")
        print(e)
        get_mem_info("After memory error")
    except Exception as e :
        print("Something went wrong")
        print(e)
        get_mem_info("After unknown error")

read_csv_file("./new-york-city-taxi-fare-prediction/train.csv")