from datadog import initialize, api

options = {
    "api_key": "",
    "app_key": ""
}

initialize(**options)


total_dashboards = api.Dashboard.get_all()
total_dashboard_list = open("Dashboards", "w")
for dashboard in total_dashboards["dashboards"]:
    title = dashboard["title"]
    total_dashboard_list.write("https://app.datadoghq.com/"+title + "\n")

    

total_dashboard_list.close()