"""
╔══════════════════════════════════════════════════════════╗
║                        tasks.py                          ║
╚══════════════════════════════════════════════════════════╝
┌──────────────────────────────────────────────────────────┐
│                        Author                            │
├──────┬────────────────────┬───────┬──────────────────────┤
│ Name │ A S M Saad         │ Email │ asmsaad3@gmail.com   │
├──────┼────────────────────┼───────┼──────────────────────┤
│ Date │ June 6, 2023       │ Github│ asmsaad/mintrower    │
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""
from tkinter import *
from tkinter import ttk
from colors import *
from icons import *
from tksupport import *
from addnewtask import *
from tabs.tktabsupport import *

class TaskTab:
    def __init__(self, base_canvas):
        self.base_canvas = base_canvas

        self.column_data_details = {
            "Selector": {"width": 50, "text_align": CENTER, "anchor": "center"},
            "ID": {"width": 100, "text_align": LEFT, "anchor": "center"},
            "Website": {"width": 240 - 10, "text_align": LEFT, "anchor": W},
            "Size": {"width": 120, "text_align": LEFT, "anchor": W},
            "Keyword": {"width": 180, "text_align": LEFT, "anchor": W},
            "Proxy": {"width": 150, "text_align": CENTER, "anchor": W},
            "Billing Profile": {"width": 150, "text_align": LEFT, "anchor": W},
            "Status": {"width": 130, "text_align": CENTER, "anchor": W},
            "Actions": {"width": 178 + 30 + 10 - 50, "text_align": LEFT, "anchor": W},
        }

        self.tab_property = TabProperty(self.base_canvas)
        self.tab_property.set_individual_data_control(controls=("run", "edit", "delete"), tab_name="task")
        self.header_frame ,self.data_show_frame , self.total_control_frame = self.tab_property.create_frames(header_height=70,middle_height=540,bottom_height=58)
        #Make Heading
        self.tab_property.tree_view_heading(self.header_frame,self.column_data_details)
        #Total Control Area
        self.total_control_panel(self.total_control_frame)

        ''''
        In this section,  retrieve  the data from the  database that
        was previously imported. The initial  imported  data will be 
        displayed at the top  of  the frame. Ensure that the data is 
        provided,  as  the  display_data  dictionary   keys  remains 
        unchanged. 
        '''
        for i in range(25):
            display_data = {
                "ID": str(i+1),
                "Website": "",
                "Size": "",
                "Keyword": "",
                "Proxy": "",
                "Billing Profile": "",
                "Status": "",
            }
            self.tab_property.individual_data(self.data_show_frame,display_data)





    def total_control_panel(self,frame):
        # Total Control button
        self.control_btns_details = {
            "add_new": {"dimension": (138 + 10, 32+10)},
            "delete_all": {"dimension": (129 + 10, 32 + 10)},
            "run_all": {"dimension": (114+10, 32+10)},
            "stop_all": {"dimension": (114+10, 32+10)},
        }

        self.left_control_frmae = Frame(frame, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.left_control_frmae.pack(side=LEFT, anchor=W)

        self.right_control_frmae = Frame(frame, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.right_control_frmae.pack(side=RIGHT, anchor=E)

        self.total_control_btns = {}
        for each_control_btn in list(self.control_btns_details.keys())[:2]:
            self.total_control_btns[each_control_btn] = {}
            self.total_control_btns[each_control_btn]["btn_obj"] = TkWidget()
            self.total_control_btns[each_control_btn]["btn"] = self.total_control_btns[each_control_btn]["btn_obj"].image_btn(self.left_control_frmae, imgTk=image__.icons(each_control_btn.lower()), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover"), dimension=self.control_btns_details[each_control_btn]["dimension"], bg=Colors__.color()["working space"]["bg"], activebackground=Colors__.color()["working space"]["bg"])
            self.total_control_btns[each_control_btn]["btn"].pack(side=LEFT, anchor=W)
            # Add New Task Button Call
            if each_control_btn == "add_new":
                self.total_control_btns[each_control_btn]["btn"]["command"] = lambda: self.add_new_data_task()

        # Left Control Button's Frame
        for each_control_btn in list(self.control_btns_details.keys())[2:]:
            self.total_control_btns[each_control_btn] = {}
            self.total_control_btns[each_control_btn]["btn_obj"] = TkWidget()
            self.total_control_btns[each_control_btn]["btn"] = self.total_control_btns[each_control_btn]["btn_obj"].image_btn(self.right_control_frmae, imgTk=image__.icons(each_control_btn.lower()), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover"), dimension=self.control_btns_details[each_control_btn]["dimension"], bg=Colors__.color()["working space"]["bg"], activebackground=Colors__.color()["working space"]["bg"])
            self.total_control_btns[each_control_btn]["btn"].pack(side=LEFT, anchor=W)


    def add_new_data_task(self):
        AddNewTask(self.base_canvas.winfo_toplevel(), self.data_show_frame, self.tab_property)








