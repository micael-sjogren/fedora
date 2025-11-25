#!/usr/bin/env python3
import os
import sys

hwmon = "/sys/class/hwmon/hwmon2"  # coretemp
MAX_TEMP = 100  # Max temperatur för procentberäkning

temps = []
for i in range(2, 10):  # temp2_input -> temp9_input
    temp_file = os.path.join(hwmon, f"temp{i}_input")
    if os.path.isfile(temp_file):
        try:
            val = int(open(temp_file).read().strip())
            temps.append(val // 1000)  # °C
        except:
            pass

if temps:
    max_temp = max(temps)
else:
    max_temp = 0

# Bestäm output-mode: "value" = grader, "pct" = procent
mode = sys.argv[1] if len(sys.argv) > 1 else "value"

if mode == "pct":
    temp_pct = min(100, max(0, int((max_temp / MAX_TEMP) * 100)))
    print(temp_pct)
else:
    print(max_temp)
