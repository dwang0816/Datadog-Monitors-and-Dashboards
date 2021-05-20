from datadog import initialize, api

options = {
    "api_key": "",
    "app_key": ""
}

initialize(**options)

total_dashboards = api.Dashboard.get_all()
total_dashboards_list = open("Dashboards hyperlinks", "w")
for dashboard in total_dashboards["dashboards"]:
    dashboardLink = dashboard["url"]
    title = dashboard["title"]
    total_dashboards_list.write("=HYPERLINK(\"https://app.datadoghq.com/"+ dashboardLink + "\", " + "\"" + title + "\"" + ")" + "\n")



total_dashboards_list.close()



