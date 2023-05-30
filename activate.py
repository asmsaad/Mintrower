
from tkinter import *
from tkinter import ttk
from window import *
from navigationbar import  *
from tksupport import *

class ActivationProducts:
    def __init__(self,root_window):
        # Create a window
        self.window = Toplevel(root_window)
        self.window_configuration = WindowConfiguration(self.window)
        self.window_configuration.geometry(800, 450)
        self.window_configuration.resizable(width=False, height=False)
        self.navigation_bar_canvas, self.working_area_canvas = self.window_configuration.custom_navigation_bar()
        # Navigation bar design
        self.navigation_bar_property = NavigationBarProperty(self.navigation_bar_canvas)
        self.navigation_bar_property.window_control()  # Enable Window Control Buttons

        # Label(, text="11").pack()

        self.window_configuration.draggable()

        self.property()


    def property(self):

        _Frame = Frame(self.working_area_canvas,bg=Colors__.color()["navigation bar"]["selected tab"],height=450-32+2,width=800,border=0,borderwidth=0,highlightthickness=0)
        _Frame.pack()
        _Frame.pack_propagate(False)

        _Frame1 = Frame(_Frame, bg=Colors__.color()["navigation bar"]["selected tab"],pady=180, border=0, borderwidth=0, highlightthickness=0)
        _Frame1.pack()

        activation_code = Entry(_Frame1,width=45,font=("Arial","18"),bg=Colors__.color()["task"]["bg"],fg="#9c9c9e",border=0,borderwidth=0,highlightthickness=0)
        activation_code.pack(side=LEFT,ipady=3)

        Label(_Frame1,bg=Colors__.color()["navigation bar"]["selected tab"],padx=10).pack(side=LEFT)

        save_btn_obj = TkWidget()
        save_btn = save_btn_obj.image_btn(_Frame1 , imgTk=image__.icons("activate".lower()), imgTk_hover=image__.icons("activate".lower()+"_hover"), dimension= (107+10,35+10), bg = Colors__.color()["navigation bar"]["selected tab"], activebackground = Colors__.color()["navigation bar"]["selected tab"])
        save_btn.pack(side=LEFT)


if __name__ == "__main__":
    root = Tk()
    ActivationProducts(root)
    root.mainloop()