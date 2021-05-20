from datadog import initialize, api

options = {
    "api_key": "",
    "app_key": ""
}

initialize(**options)

total_monitors = api.Monitor.get_all()
total_monitors_list = open("Monitor hyperlinks", "w")
for monitor in total_monitors:
    monitorId = monitor["id"]
    name = monitor["name"]
    total_monitors_list.write("=HYPERLINK(\"https://app.datadoghq.com/monitors/"+ str(monitorId) + "\", " + "\"" + name + "\"" + ")" + "\n")



total_monitors_list.close()



