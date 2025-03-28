import os
import subprocess
import re
import matplotlib.pyplot as plt
import numpy as np


ping_data:list = [""]*11

def ping():
    try:
        # 執行 ping 命令
        output = subprocess.run(["ping", "google.com"], capture_output=True, text=True, check=True)
        print(output.stdout)
        # 使用正則表達式提取平均延遲時間
        match = re.search(r'平均 = ([\d.]+)ms', output.stdout)
        if match:
            print(f"Average latency: {match.group(1)} ms")
        else:
            print("Could not find average latency.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode} - {e.output}")
    return match.group(1)

for i in range (0, 11):
    match = ping()
    ping_data[i] = match



x_data = list(range(len(ping_data)))

print(ping_data)
# 將字符串轉換為整數進行數值排序
ping_data = list(map(int, ping_data))

# 冒泡排序
n = len(ping_data)
for j in range(n):
    for i in range(0, n-j-1):
        if ping_data[i] > ping_data[i+1]:
            # 交換
            ping_data[i], ping_data[i+1] = ping_data[i+1], ping_data[i]

print(ping_data)

data_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(x_data, ping_data, marker="x") 

#計算並繪製趨勢線 
coefficients = np.polyfit(x_data, ping_data, 1) 
trendline = np.polyval(coefficients, x_data) 
plt.plot(x_data, trendline, color='red', linestyle='--', label='trend line')

plt.xlabel("time")
plt.ylabel("ping")

plt.show()