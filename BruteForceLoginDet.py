#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Generate a random log file named auth.log 


# In[1]:


import random
from datetime import datetime, timedelta 

ips = ["192.168.1.12", "10.0.0.7", "172.16.0.221"]
users = ["admin", "root", "test", "user"]

time = datetime.now()

with open("auth.log", "w") as log:
    for i in range(20):
        ip = random.choice(ips)
        user = random.choice(users)
        timestamp = time + timedelta(seconds=i*10)
        
        log.write(
             f"{timestamp.strftime('%b %d %H:%M:%S')} server sshd[{1000+i}]: "
             f"Failed password for invald user {user} from {ip} port {random.randint(50000,60000)}\n"
         )


# In[ ]:


##Detection script


# In[2]:


import re                           ## re = Regularr expressions module - helps search, match and extract patterns from text.
from collections import defaultdict 


# In[3]:


THRESHOLD = 5 

failed_attempts = defaultdict(int)

with open("auth.log", "r") as log:
    for line in log:
        if "Failed password" in line:
            ip = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip:
                failed_attempts[ip.group(1)] += 1
                
print("\n SOC Alert Summary")
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"ALERT: Possible brute force attack from {ip} ({count}) failed attempts)")


# In[ ]:




