import os
import pandas as pd

from tkinter import filedialog
from tkinter import simpledialog

from URL_explorer import gui_widget

selection_widget()

#def metric_selection():

#print(chk_CTR_state.get())
#print(chk_PVC_state.get())

# data collection
raw_file = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select Internal HTML file",
                                                filetypes = (("CSV Document", '.csv'),("all files","*.*")))

seperator = simpledialog.askstring("Input", "What is the seperator",
                                    parent= application_window)

url_list = pd.read_csv(raw_file, sep = seperator)



print(list(url_list))
def site_list_complete(dataframe, metric, number, url_variable):

    top_observations = dataframe.nlargest(number, metric)

    for i in top_observations[url_variable]:
        print(i)


site_list_complete(url_list,'Post-View Conversions', 10, "App/URL")





