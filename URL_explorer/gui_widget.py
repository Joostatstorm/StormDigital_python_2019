import tkinter as tkk

class Selection_widget():
    #set window
    def __init__(self):
        self.window = tkk.Tk()
        self.window.title("URL explorer")
        self.window.geometry('1000x200')

        ## metric selections to show
        #text box
        self.label_metric_viewing = tkk.Label(text="Which variables do you want to return", relief=tkk.RIDGE).grid(column=0, row=0)
        # make state of boolean var
        self.chk_CTR_state = tkk.BooleanVar()
        self.chk_PVC_state = tkk.BooleanVar()
        # set state to false as initial value
        self.chk_CTR_state.set(False)
        self.chk_PVC_state.set(False)
        # generate checkbuttons
        self.chk_CTR = tkk.Checkbutton(self.window, text='CTR', var=self.chk_CTR_state)
        self.chk_PVC = tkk.Checkbutton(self.window, text='Post View Conversions', var=self.chk_PVC_state)
        # set position of checkbuttons
        self.chk_CTR.grid(column=0, row=1)
        self.chk_PVC.grid(column=1, row=1)

        ##metric selection to base ranking on
        #
        self.label_metric_ranking = tkk.Label(text="Select the label you wish to rank by", relief=tkk.RIDGE).grid(column=0, row=2)

        #generate radiobuttons per metric
        self.metric_selection = tkk.StringVar()
        self.radio_imp = tkk.Radiobutton(self.window, text="Impression", variable=self.metric_selection, value="Impression")
        self.radio_clicks = tkk.Radiobutton(self.window, text="Clicks", variable=self.metric_selection, value="Clicks")
        self.radio_CTR = tkk.Radiobutton(self.window, text="CTR", variable=self.metric_selection, value="CTR")
        self.radio_totconv = tkk.Radiobutton(self.window, text="Total conversions", variable=self.metric_selection, value="Total conversion")
        self.radio_viewconv = tkk.Radiobutton(self.window, text="Post-view Conversions", variable=self.metric_selection, value="Post-view Conversions")
        self.radio_clickconv = tkk.Radiobutton(self.window, text="Post-click Conversions", variable=self.metric_selection, value="Post-click Conversions")
        self.radio_rev = tkk.Radiobutton(self.window, text="Revenue", variable=self.metric_selection, value="Revenue")

        # set position of metric selection
        self.radio_imp.grid(column=0, row=3)
        self.radio_clicks.grid(column=1, row=3)
        self.radio_CTR.grid(column=2, row=3)
        self.radio_totconv.grid(column=3, row=3)
        self.radio_viewconv.grid(column=0, row=4)
        self.radio_clickconv.grid(column=1, row=4)
        self.radio_rev.grid(column=2, row=4)

        #topN selection
        self.topN_label = tkk.Label(text="How many URL's do you want to return", relief=tkk.RIDGE)

        self.topN_var = tkk.StringVar()
        self.topN = tkk.Entry(self.window, textvariable=self.topN_var)

        self.topN_label.grid(column=0, row=5)
        self.topN.grid(column=0, row=6)

        ## ad select button
        self.select_button = tkk.Button(self.window, text='select', command=self.window.quit())
        self.select_button.grid(column=0, row=7)


    def selected_metric(self):
        #print(self.metric_selection.get())
        return self.chk_CTR_state.get(), self.chk_PVC_state.get(), self.metric_selection.get(), self.topN_var.get()


program = Selection_widget()
program.window.mainloop()
program.selected_metric()


#'Impressions', 'Clicks', 'Click Rate (CTR)', 'Total Conversions', 'Post-Click Conversions', 'Post-View Conversions', 'Revenue (Adv Currency)'