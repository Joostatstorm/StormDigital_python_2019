import os
import pandas as pd

from tkinter import filedialog
from tkinter import simpledialog

from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("URL explorer")

window.geometry('350x200')

def state():
     print("function is called")

chk_CTR_state = BooleanVar()
chk_PVC_state = BooleanVar()

chk_CTR_state.set(False)  # set check state
chk_PVC_state.set(False)  # set check state

chk_CTR = Checkbutton(window, text='CTR', var=chk_CTR_state, command=state)
chk_PVC = Checkbutton(window, text='Post View Conversions', var=chk_PVC_state, command=state)

chk_CTR.grid(column=0, row=0)
chk_PVC.grid(column=1, row=0)

print(chk_CTR_state.get())
window.mainloop()

print(chk_CTR_state.get())

'''

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
'''




