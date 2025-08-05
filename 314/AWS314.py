import psutil

#CPU Usage(%)
# CPUusage1=psutil.cpu_percent(interval=0.1,percpu=True)
CPUusage2=psutil.cpu_percent(interval=0.1)
# print(f"CPU percentage : {CPUusage1}%")
print("################ CPU ################")
print(f"CPU Usage(%) : {CPUusage2}%")

#Memory
mem = psutil.virtual_memory()
print("################ Memory ################")
print(f"Total : {round(mem.total/1024**3,3)} GB")
print(f"Available : {round(mem.available/1024**3,3)} GB")
print(f"Memory Usage(%) : {mem.percent}%")

#Disk
disk=psutil.disk_usage('/')
print("################ Disk ################")
print(f"Disk usage(%) : {disk.percent}%")

#Network
network=psutil.net_io_counters()
print("################ Network ################")
print(f"Sent Bytes : {network.bytes_sent}")
print(f"Receive Bytes : {network.bytes_recv}")