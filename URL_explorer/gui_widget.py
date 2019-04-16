import tkinter as tkk

class selection_widget():
    #set window
    def __init__(self):
        self.window = tkk.Tk()
        self.window.title("URL explorer")
        self.window.geometry('350x200')



    def state():
         print("function is called")

    def
    cmd_frame = tkk.LabelFrame(self.window, text="Commands", relief=tkk.RIDGE)
    #cmd_frame.grid(row=1, column=1, sticky=E + W + tk.N + tk.S)

    #button_label = ttk.Label(cmd_frame, text="tk.Button")
    #button_label.grid(row=1, column=1, sticky=tk.W, pady=3)


    chk_CTR_state = tkk.BooleanVar()
    chk_PVC_state = tkk.BooleanVar()

    chk_CTR_state.set(False)  # set check state
    chk_PVC_state.set(False)  # set check state

    chk_CTR = tkk.Checkbutton(window, text='CTR', var=chk_CTR_state, command=state)
    chk_PVC = tkk.Checkbutton(window, text='Post View Conversions', var=chk_PVC_state, command=state)

    chk_CTR.grid(column=0, row=0)
    chk_PVC.grid(column=1, row=0)

program = selection_widget()

# Start the GUI event loop
program.window.mainloop()