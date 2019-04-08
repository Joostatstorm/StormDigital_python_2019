import os
import pandas as pd

# data collection
path="/Users/Joost/Documents/Scripts/Top_URL_Script"
os.chdir(path)

url_list = pd.read_csv("URL_report_PL.csv", sep=";")

print(list(url_list))
def site_list_complete(dataframe, metric, number, url_variable):

    top_observations = dataframe.nlargest(number, metric)

    for i in top_observations[url_variable]:
        print(i)

site_list_complete(url_list,'Post-View Conversions', 10, "App/URL")
