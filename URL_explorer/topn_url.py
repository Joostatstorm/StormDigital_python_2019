import os
import time

import pandas as pd
import tkinter as tkk
from URL_explorer import gui_widget
from tkinter import filedialog

from tkinter import simpledialog


# data collection
#raw_file = tkk.filedialog.askopenfilename(initialdir = "/",
#                                                title = "Select Internal HTML file",
#                                                filetypes = (("CSV Document", '.csv'),("all files","*.*")))

#seperator = simpledialog.askstring("Input", "What is the seperator",
#                                    parent= application_window)


#url_list = pd.read_csv(raw_file, sep=";")

#print(list(url_list))


# Start the GUI event loop
selection_widget = gui_widget.Selection_widget()

#metric_list = ['Impressions', 'Clicks', 'Click Rate (CTR)']
### functie ombouwen zodat die meerder metrics kan handelen.
### upload moet los staan van de explorer.

#time.sleep(10000)
print(selection_widget.selected_metric())

'''
###function that returns
def site_list_complete(dataframe, url_variable):
    CTR, PVC, metric, topN = selection_widget.selected_metric()

    top_observations = dataframe.nlargest(int(topN), metric)

    for i in top_observations[url_variable]:
        print(i)

site_list_complete(url_list, "App/URL")

'''



