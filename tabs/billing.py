"""
╔══════════════════════════════════════════════════════════╗
║                       billing.py                         ║
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

class BillingTab:
    def __init__(self, base_canvas):
        self.base_canvas = base_canvas

        self.column_data_details = {
            "Selector": {"width": 50, "text_align": CENTER, "anchor": "center"},
            "ID": {"width": 100, "text_align": LEFT, "anchor": "center"},
            "Profile": {"width": 230, "text_align": LEFT, "anchor": W},
            "Name On Card": {"width": 120+130, "text_align": LEFT, "anchor": W},
            "Email": {"width": 180+56, "text_align": LEFT, "anchor": W},
            "Shipping Address": {"width": 150+150, "text_align": CENTER, "anchor": W},
            # "Billing Profile": {"width": 150, "text_align": LEFT, "anchor": W},
            # "Status": {"width": 130, "text_align": CENTER, "anchor": W},
            "Actions": {"width": 112, "text_align": LEFT, "anchor": W}, #56
        }

        self.tab_property = TabProperty(self.base_canvas)
        self.tab_property.set_individual_data_control( controls=("edit","delete"))
        self.header_frame ,self.data_show_frame , self.total_control_frame = self.tab_property.space_configure(header_height=70,middle_height=540,bottom_height=58)
        #Make Heading
        self.tab_property.tree_view_heading(self.header_frame,self.column_data_details)


        for i in range(12):
            display_data = {
                "Selector": "",
                "ID": str(i),
                "Profile": "",
                "Name On Card": "",
                "Email": "",
                "Shipping Address": "",
                "Actions": "", #56
            }
            self.tab_property.individual_data(self.data_show_frame,display_data)












