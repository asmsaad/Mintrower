from window import *
from navigationbar import *
from tab import *
from icons import *
import os




class MainWindow:
    def __init__(self):
        # Create a window
        self.root = Tk()
        self.window = Toplevel()
        self.window_configuration = WindowConfiguration(self.window)
        self.window_configuration.geometry(1300, 700)
        self.window_configuration.resizable(width=False, height=False)
        self.navigation_bar_canvas, self.working_area_canvas = self.window_configuration.custom_navigation_bar()
        # Navigation bar design
        self.navigation_bar_property = NavigationBarProperty(self.navigation_bar_canvas,root_window=self.root)
        self.navigation_bar_property.window_control()   # Enable Window Control Buttons
        self.navigation_bar_property.notification()     # Notification Button
        # Add tab
        self.tab_frame = self.navigation_bar_property.tab_frame()
        Tab(self.tab_frame,self.working_area_canvas)

        # self.window.winfo_toplevel()



        self.window_configuration.draggable()

        # working area design
        self.root.iconify()
        self.root.geometry("0x0")
        self.root.bind("<Configure>",self.window_response)
        self.root.iconphoto(False,image__.icons("logo"))
        self.root.title("Mintrower")
        self.root.mainloop()

    def window_response(self,e):
        self.root.iconify()
        if self.window.state() == 'normal':
            self.window.withdraw()
        elif self.window.state() == 'withdrawn':
            self.window.deiconify()





if __name__ == "__main__":
    MainWindow()
