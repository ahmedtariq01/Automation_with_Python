import shutil
import psutil

disk_usage = shutil.disk_usage("/")
free_space = disk_usage.free / disk_usage.total * 100
print(f"Free space: {free_space:.2f}%")
print('Total space:',disk_usage)

cpu_usage = psutil.cpu_percent(1)
print(f"CPU usage: {cpu_usage}%")


