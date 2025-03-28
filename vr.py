import os
import subprocess
import re

name1 = "chrome.exe" 
name2 = "steam.exe"
if input("have chrome? Y/N") == "y":
    subprocess.run(["taskkill", "/F", "/IM", name1], check=True)
    print(name1, "killed")
if input("have steam? Y/N") == "y":
    subprocess.run(["taskkill", "/F", "/IM", name2], check=True)
    print(name2, "killed")


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

match = ping()
vrdt = input("need VRDT? Y/N")
svr = input("need steamvr? Y/N")
intmatch = match
if not match > "50":
    vrdt
    svr
    if vrdt == "y":
        subprocess.Popen([r"C:\Program Files\Virtual Desktop Streamer\VirtualDesktop.Streamer.exe"])
    if svr == "y":
                subprocess.Popen([r"explorer", r"C:\Users\windw\SteamVR.url"])
if match > "50" and input("keep try? Y/N") == "y":
    while match > "50":
        match = ping()
    if vrdt == "y":
        subprocess.Popen([r"C:\Program Files\Virtual Desktop Streamer\VirtualDesktop.Streamer.exe"])
    if svr == "y":
        subprocess.Popen([r"explorer", r"C:\Users\windw\SteamVR.url"])