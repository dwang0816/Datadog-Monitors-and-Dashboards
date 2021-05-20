from datadog import initialize, api

options = {
    "api_key": "",
    "app_key": ""
}

initialize(**options)

# Grabbing the hosts list
total_monitors = api.Monitor.get_all()
total_monitors_list = open("Monitors", "w")
for monitor in total_monitors:
    total_monitors_list.write(monitor["name"] + "\n")

    

total_monitors_list.close()