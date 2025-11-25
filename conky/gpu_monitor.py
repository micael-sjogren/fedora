#!/usr/bin/env python3
import sys
import subprocess

def get_gpu_info():
    try:
        # Temperatur
        temp = int(subprocess.check_output(
            ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"]
        ).decode().strip())
        
        # Minne
        mem_used = int(subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"]
        ).decode().strip())
        
        mem_total = int(subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"]
        ).decode().strip())
        
        # Procentvärden för bars
        temp_pct = min(int(temp / 100 * 100), 100)        # max 100°C
        mem_pct  = min(int(mem_used / mem_total * 100), 100)
        
        return temp, temp_pct, mem_used, mem_pct

    except Exception:
        return 0, 0, 0, 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gpu_monitor.py temp|temp_pct|mem|mem_pct")
        sys.exit(1)

    temp, temp_pct, mem_used, mem_pct = get_gpu_info()
    arg = sys.argv[1].lower()

    if arg == "temp":
        print(temp)           # visad i °C
    elif arg == "temp_pct":
        print(temp_pct)       # används för bar
    elif arg == "mem":
        print(mem_used)       # visad i MB
    elif arg == "mem_pct":
        print(mem_pct)        # används för bar
    else:
        print("Unknown argument")
