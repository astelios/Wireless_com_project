from subprocess import Popen, STDOUT
from time import time, sleep
from random import randrange, seed
from os import makedirs
from sys import argv

seed(1)

#iperf_cmd = [iperf -c 192.168.2.AP -u -b "Speed in Mb"M -p 5003 -t "Time in seconds", "-i", "1"]

start = time()
i = 1
output_dir = "iperf_outputs"
makedirs(output_dir, exist_ok=True)

# List to keep track of subprocesses
processes = []

# experiment
while(time() - start <= 300): 
    file_path = f"{output_dir}/output_{i}_{round(time()-start, 1)}.txt"
    i += 1
    file = open(file_path, "w+") 
    iperf_cmd = ["iperf", "-c", "192.168.2."+argv[1], "-u", "-b", f"{randrange(30, 61, 1)}M", "-p", "5003", "-t", f"{randrange(10, 41, 1)}", "-i", "1"]
    process = Popen(iperf_cmd, stdout=file, stderr=STDOUT)
    processes.append((process, file))
    sleep(randrange(10, 16, 1))
    
for process, file in processes:
    process.wait()
    file.close()

