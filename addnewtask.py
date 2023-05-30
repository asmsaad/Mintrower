
from tkinter import *
from tkinter import ttk
from window import *
from navigationbar import  *
from tksupport import *

class AddNewTask:
    def __init__(self,root_window,data_show_frame,tab_property):
        self.data_show_frame = data_show_frame
        self.tab_property = tab_property

        # Create a window
        self.toplevel_window_obj = TkTopLevel(root_window.winfo_toplevel(),(350, 550))
        self.window = self.toplevel_window_obj.create()

        self.window_configuration = WindowConfiguration(self.window)
        self.window_configuration.geometry(350, 550)
        self.window_configuration.resizable(width=False, height=False)
        self.navigation_bar_canvas, self.working_area_canvas = self.window_configuration.custom_navigation_bar()
        # Navigation bar design
        self.navigation_bar_property = NavigationBarProperty(self.navigation_bar_canvas,btns=("terminate"))
        self.navigation_bar_property.window_control()  # Enable Window Control Buttons

        self.window_configuration.draggable()

        self.toplevel_window_obj.make_center_on_root_window()

        self.property()


    def property(self):

        self.entry_widget_info = {
            "Website": {"type": "ComboBox", "values": []},
            "Billing Profile": {"type": "ComboBox", "values": []},
            "Proxy": {"type": "ComboBox", "values": []},
            "Catagory": {"type": "ComboBox", "values": ["Started", "Created Browser", "At Homepage", "At View All", "At Category Page", "At Product Page", "Selected Size", "Added to Cart", "Checked Out"]},
            "Size": {"type": "ComboBox", "values": []},
            "Color/Style": {"type": "Entry", "values": []},
            "Method": {"type": "ComboBox", "values": []},
            "Keywords": {"type": "Entry", "values": []},
            "Navigation Keyword": {"type": "Entry", "values": []},
            "Checkout Delay": {"type": "Entry", "values": []},
            "Monitor Delay": {"type": "Entry", "values": []},
        }

        self.data_entry_root_Frame = Frame(self.working_area_canvas,bg=Colors__.color()["navigation bar"]["selected tab"],height=650-32,width=350,border=0,borderwidth=0,highlightthickness=0)
        self.data_entry_root_Frame.pack()
        self.data_entry_root_Frame.pack_propagate(False)

        data_entry_Frame = Frame(self.data_entry_root_Frame,bg=Colors__.color()["navigation bar"]["selected tab"],height=470,width=350-15,pady=5,border=0,borderwidth=0,highlightthickness=0)
        data_entry_Frame.pack()
        # Set the initial theme
        # self.data_entry_Frame.tk.call("source", "res/Theme/azure.tcl")
        # self.data_entry_Frame.tk.call("set_theme", "dark")

        # Label(data_entry_Frame,text="11").pack()
        data_entry_Frame.pack_propagate(False)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Round.TButton", relief="flat", borderwidth=0, padding=6 , foreground="#9c9c9e" )

        style.configure("TCombobox", fieldbackground=Colors__.color()["task"]["bg"], background=Colors__.color()["task"]["bg"] ,  fieldforeground=[('readonly', 'blue')] , border=0,borderwidth=0,foreground="#9c9c9e")
        # style.configure("TCombobox.field", foreground="blue")
        style.configure("TEntry", fieldbackground=Colors__.color()["task"]["bg"], background=Colors__.color()["task"]["bg"],border=0,borderwidth=0,foreground="#9c9c9e")
        # style.configure("TCombobox.padding", padding=10)

        self.add_new_data_widget = {}
        for index, each_info in enumerate(list(self.entry_widget_info.keys())):
            self.add_new_data_widget[each_info] = {}
            self.add_new_data_widget[each_info]["frame"]= Frame(data_entry_Frame,bg=Colors__.color()["navigation bar"]["selected tab"],height=42,width=350-15,border=0,borderwidth=0,highlightthickness=0)
            self.add_new_data_widget[each_info]["frame"].pack(anchor=W)
            self.add_new_data_widget[each_info]["frame"].pack_propagate(False)

            self.add_new_data_widget[each_info]["label"] = Label(self.add_new_data_widget[each_info]["frame"],text=each_info,bg=Colors__.color()["navigation bar"]["selected tab"],fg="#9c9c9e",font=("Arial", "12", "normal"))
            self.add_new_data_widget[each_info]["label"].pack(side=LEFT,anchor=W)

            if self.entry_widget_info[each_info]["type"] == "ComboBox":

                self.add_new_data_widget[each_info]["insert_data"] = ttk.Combobox(self.add_new_data_widget[each_info]["frame"],state="normaltasks.py", width=17,font=("Arial", "12", "normal"),style="TCombobox")
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4)
                self.add_new_data_widget[each_info]["insert_data"]["value"] = self.entry_widget_info[each_info]["values"]


            elif self.entry_widget_info[each_info]["type"] == "Entry":
                self.add_new_data_widget[each_info]["insert_data"] = ttk.Entry(self.add_new_data_widget[each_info]["frame"], width=16+2, font=("Arial", "12", "normal"))
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4,ipadx=2)

        save_btn_obj = TkWidget()
        save_btn = save_btn_obj.image_btn(self.data_entry_root_Frame , imgTk=image__.icons("save".lower()), imgTk_hover=image__.icons("save".lower()+"_hover"), dimension= (107+10,35+10), bg = Colors__.color()["navigation bar"]["selected tab"], activebackground = Colors__.color()["navigation bar"]["selected tab"])
        save_btn.pack()
        save_btn["command"] = self.save_btn_action





    def save_btn_action(self):
        display_data = {
            "ID": str(111),
            "Website": "",
            "Size": "",
            "Keyword": "",
            "Proxy": "",
            "Billing Profile": "",
            "Status": "",
        }
        self.tab_property.individual_data(self.data_show_frame, display_data)

        self.window.destroy()






if __name__ == "__main__":
    root = Tk()
    AddNewTask(root)
    root.mainloop()