from src import hello_world
import time
import datetime

if __name__ == "__main__":
    while True:
        print(f"{hello_world()}  {datetime.datetime.now()}")
        time.sleep(5)