import os
hostname = "73.98.71.235"
port = "25565"
response = os.system("ping " + hostname + ":" + port)

print(response)