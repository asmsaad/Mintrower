"""
╔══════════════════════════════════════════════════════════╗
║                     tktabssupport.py                     ║
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
from icons import *
from colors import *
from tksupport import *




class TabProperty:
    def __init__(self,base):
        self.tab_base_frame = base
        pass

    # Need to input height of each area
    def space_configure(self,header_height=0,middle_height=0,bottom_height=0):
        # Header Frame
        self.header_frame = Frame(self.tab_base_frame, bg=Colors__.color()["working space"]["bg"], width=1300 - 15,height=header_height, border=0, borderwidth=0, highlightthickness=0)
        self.header_frame.pack()
        self.header_frame.pack_propagate(False)
        # Header Bottom separation
        Label(self.header_frame, bg=Colors__.color()["working space"]["bg"]).pack()
        # self.tree_view_heading(self.header_frame)


        # Middle Frame
        self.middle_frame = Frame(self.tab_base_frame, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0,highlightthickness=0)
        self.middle_frame.pack()

        self.middle_frame_canvas = Canvas(self.middle_frame,height=middle_height,width=1300-15,bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.middle_frame_canvas.pack()
        # self.middle_frame_canvas.pack_propagate(False)
        # Scrollable Frame
        self.data_show_frame = Frame(self.middle_frame_canvas,bg=Colors__.color()["working space"]["bg"],padx=0,border=0, borderwidth=0,highlightthickness=0)
        self.middle_frame_canvas.create_window((0, 0), window=self.data_show_frame, anchor="nw")

        # Bind the mouse wheel event to the canvas
        self.middle_frame_canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        # Update the scroll region when the frame size changes
        self.data_show_frame.bind("<Configure>", lambda e: self.middle_frame_canvas.configure(scrollregion=self.middle_frame_canvas.bbox("all")))




        # Bottom Frame
        self.total_control_frame = Frame(self.tab_base_frame, bg=Colors__.color()["working space"]["bg"], width=1300 - 15,height=bottom_height, border=0, borderwidth=0, highlightthickness=0)
        self.total_control_frame.pack()
        self.total_control_frame.pack_propagate(False)
        # self.total_control_panel(self.total_control_frame)

        return self.header_frame ,self.data_show_frame , self.total_control_frame

    def test(self):
        for i in range(12):
            display_data = {
                "ID" : str(i+1),
                "Website": "",
                "Size": "",
                "Keyword": "",
                "Proxy": "",
                "Billing Profile": "",
                "Status": "",
            }
            self.individual_data(self.data_show_frame,display_data)

    def on_mousewheel(self,e):
        self.middle_frame_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        print("hi")
        # if len(self.data_show_frame.winfo_children()) > 12 :
        #     self.middle_frame_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        # else:
        #     self.middle_frame_canvas.yview_moveto(0)


    def tree_view_heading(self,frame,column_data_details):
        self.column_data_details = column_data_details

        header_column_data = {}
        for index, each_header_column_data in enumerate(list(self.column_data_details.keys())):
            header_column_data[each_header_column_data] = {}
            header_column_data[each_header_column_data]["frame"] = Frame(frame,width=self.column_data_details[each_header_column_data]["width"],height=40,padx=5,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
            header_column_data[each_header_column_data]["frame"].pack(side=LEFT,anchor=W)
            header_column_data[each_header_column_data]["frame"].pack_propagate(False)

            if each_header_column_data == "Selector":
                pass
            else:
                header_column_data[each_header_column_data]["label"] = Label(header_column_data[each_header_column_data]["frame"],bg=Colors__.color()["task"]["bg"],fg=Colors__.color()["task"]["fg"],font=("Arial","11","bold"),pady=12,border=0,borderwidth=0,highlightthickness=0)
                header_column_data[each_header_column_data]["label"]["text"] = each_header_column_data
                header_column_data[each_header_column_data]["label"].pack()

            if index != len(list(self.column_data_details.keys()))-1:
                header_column_data[each_header_column_data]["seperator"] = Frame(frame,width=1,height=25,bg="#313132",border=0,borderwidth=0,highlightthickness=0)
                header_column_data[each_header_column_data]["seperator"].pack(side=LEFT,anchor=W)
                header_column_data[each_header_column_data]["seperator"].pack_propagate(False)



    def individual_data(self,base_frame,display_data):



        individual_data_frame11 = Frame(self.data_show_frame,width=1300-15,height=45,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
        individual_data_frame11.pack()
        individual_data_frame11.pack_propagate(False)

        individual_data_frame = Frame(individual_data_frame11,width=1300-15,height=40,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
        individual_data_frame.pack()
        individual_data_frame.pack_propagate(False)

        individual_data_seperator_frame = Frame(individual_data_frame11,width=1300-15,height=5,bg=Colors__.color()["working space"]["bg"],border=0,borderwidth=0,highlightthickness=0)
        individual_data_seperator_frame.pack()
        individual_data_seperator_frame.pack_propagate(False)








        column_data = {}
        for index,each_column_data in enumerate(list(self.column_data_details.keys())):
            column_data[each_column_data] = {}
            column_data[each_column_data]["frame"] = Frame(individual_data_frame,width=self.column_data_details[each_column_data]["width"],height=40,padx=5,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
            column_data[each_column_data]["frame"].pack(side=LEFT,anchor=W)
            column_data[each_column_data]["frame"].pack_propagate(False)
            # Text Content
            if each_column_data == "Actions":
                self.individual_data_control(column_data[each_column_data]["frame"],individual_data_frame11)
            else:
                if each_column_data == "Selector":
                    column_data[each_column_data]["select_box_obj"] = TkWidget()
                    column_data[each_column_data]["select_box"] = column_data[each_column_data]["select_box_obj"].image_btn(column_data[each_column_data]["frame"] , imgTk=image__.icons("select_box".lower(),dimension=(14,14)), imgTk_hover=image__.icons("select_box".lower()+"_hover",dimension=(14,14)), dimension= (24,53), bg = Colors__.color()["task"]["bg"], activebackground = Colors__.color()["task"]["bg"])
                    column_data[each_column_data]["select_box"].pack()
                    column_data[each_column_data]["select_box"]["command"] = lambda selected = False, btn_widget = column_data[each_column_data]["select_box"], btn_obj = column_data[each_column_data]["select_box_obj"], base_frame = individual_data_frame: self.toggle_checkbox(selected,btn_widget,btn_obj,base_frame)


                else:

                    column_data[each_column_data]["label"] = Label(column_data[each_column_data]["frame"],bg=Colors__.color()["task"]["bg"],fg=Colors__.color()["task"]["fg"],font=("Arial","11"),pady=12,border=0,borderwidth=0,highlightthickness=0)
                    column_data[each_column_data]["label"]["text"] = display_data[each_column_data]

                    if self.column_data_details[each_column_data]["text_align"].upper() == "CENTER":
                        column_data[each_column_data]["label"].pack()
                    else:
                        column_data[each_column_data]["label"].pack(anchor=self.column_data_details[each_column_data]["anchor"])


            if index != len(list(self.column_data_details.keys()))-1:
                column_data[each_column_data]["seperator"] = Frame(individual_data_frame,width=1,height=25,bg="#313132",border=0,borderwidth=0,highlightthickness=0)
                column_data[each_column_data]["seperator"].pack(side=LEFT,anchor=W)
                column_data[each_column_data]["seperator"].pack_propagate(False)

        # self.middle_frame_canvas.yview_moveto(1.0)
        self.middle_frame_canvas.yview_moveto(1.0)  # Scrolls to the bottom


    def set_individual_data_control(self,controls=()):
        self.control_btns = controls
    def individual_data_control(self,frmae,root_frame):
        individual_control_frame = Frame(frmae,bg=Colors__.color()["task"]["bg"],pady=4,border=0,borderwidth=0,highlightthickness=0)
        individual_control_frame.pack()

        control_btn_details = {
            "run": {},
            "edit": {},
            "delete": {},
        }

        individual_control_btn = {}

        # control_base_image()
        if "run" in self.control_btns and "edit" in self.control_btns:
            Label(individual_control_frame, padx=3,bg=Colors__.color()["task"]["bg"], border=0, borderwidth=0, highlightthickness=0).pack(side=LEFT)

            combo = Canvas(individual_control_frame,bg=Colors__.color()["task"]["bg"],height=40,width=32*3,border=0,borderwidth=0,highlightthickness=0)
            combo.pack(side=LEFT)
            combo.pack_propagate()
            background = control_base_image(type="double")
            combo.background = background
            combo.create_image(int((32*3)/2), int(32/2), image=background)

            control_btn_details_type1 = {
                "run":  {"place":{"x":20,"y":8}},
                "edit": {"place":{"x":60,"y":8}},
            }

            for each_control_btn in control_btn_details_type1:
                individual_control_btn[each_control_btn] = {}
                individual_control_btn[each_control_btn]["btn_obj"] = TkWidget()
                individual_control_btn[each_control_btn]["btn"] = individual_control_btn[each_control_btn]["btn_obj"].image_btn(combo , imgTk=image__.icons(each_control_btn.lower(),dimension=(12,12)), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover",dimension=(12,12)), dimension= (16,16), bg = Colors__.color()["task"]["action bg"], activebackground = Colors__.color()["task"]["bg"])
                individual_control_btn[each_control_btn]["btn"].place(x=control_btn_details_type1[each_control_btn]["place"]["x"],y=control_btn_details_type1[each_control_btn]["place"]["y"])#pack(side=LEFT)

                if each_control_btn == "delete":
                    individual_control_btn["delete"]["btn"]["command"] = lambda root_frame=root_frame : self.delete_data(root_frame)
                elif each_control_btn == "run":
                    individual_control_btn["run"]["btn"]["command"] = lambda Tk_btn_=individual_control_btn["run"],stage = "run" : self.run_stop_each_individual(Tk_btn_,stage)

        if "delete" in self.control_btns:
            Label(individual_control_frame,padx=3,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0).pack(side=LEFT)

            combo1 = Canvas(individual_control_frame,bg=Colors__.color()["task"]["bg"],height=40,width=32*3,border=0,borderwidth=0,highlightthickness=0)
            combo1.pack(side=LEFT)
            combo1.pack_propagate()
            background1 = control_base_image(type="single")
            combo1.background1 = background1
            combo1.create_image(int((32*2)/2), int(32/2), image=background1)

            each_control_btn = "delete"
            individual_control_btn[each_control_btn] = {}
            individual_control_btn[each_control_btn]["btn_obj"] = TkWidget()
            individual_control_btn[each_control_btn]["btn"] = individual_control_btn[each_control_btn]["btn_obj"].image_btn(combo1 , imgTk=image__.icons(each_control_btn.lower(),dimension=(12,12)), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover",dimension=(12,12)), dimension= (16,16), bg = Colors__.color()["task"]["action bg"], activebackground = Colors__.color()["task"]["bg"])
            individual_control_btn[each_control_btn]["btn"].place(x=15,y=8)

            if each_control_btn == "delete":
                individual_control_btn["delete"]["btn"]["command"] = lambda root_frame=root_frame : self.delete_data(root_frame)



        # for each_control_btn in control_btn_details:
        #     if each_control_btn in self.control_btns:
        #         individual_control_btn[each_control_btn] = {}
        #         individual_control_btn[each_control_btn]["btn_obj"] = TkWidget()
        #         individual_control_btn[each_control_btn]["btn"] = individual_control_btn[each_control_btn]["btn_obj"].image_btn(individual_control_frame , imgTk=image__.icons(each_control_btn.lower(),dimension=(24,24)), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover",dimension=(24,24)), dimension= (50,50), bg = Colors__.color()["task"]["bg"], activebackground = Colors__.color()["task"]["bg"])
        #         individual_control_btn[each_control_btn]["btn"].pack(side=LEFT)
        #         if each_control_btn == "delete":
        #             individual_control_btn["delete"]["btn"]["command"] = lambda root_frame=root_frame : self.delete_data(root_frame)
        #         elif each_control_btn == "run":
        #             individual_control_btn["run"]["btn"]["command"] = lambda Tk_btn_=individual_control_btn["run"],stage = "run" : self.run_stop_each_individual(Tk_btn_,stage)

    #need to change according to tab
    def run_stop_each_individual(self,Tk_btn_,stage):
        if stage == "run":
            Tk_btn_["btn_obj"].update_btn_image(imgTk=image__.icons("stop".lower(),dimension=(12,12)), imgTk_hover=image__.icons("stop".lower()+"_hover",dimension=(12,12)))
            Tk_btn_["btn"]["command"] = lambda Tk_btn_=Tk_btn_,stage = "stop" : self.run_stop_each_individual(Tk_btn_,stage)
        else:
            Tk_btn_["btn_obj"].update_btn_image(imgTk=image__.icons("run".lower(),dimension=(12,12)), imgTk_hover=image__.icons("run".lower()+"_hover",dimension=(12,12)))
            Tk_btn_["btn"]["command"] = lambda Tk_btn_=Tk_btn_,stage = "run" : self.run_stop_each_individual(Tk_btn_,stage)


    def delete_data(self,root_frame):
        root_frame.destroy()


    def toggle_checkbox_highlighter(self,base_frame,color):
        for child in base_frame.winfo_children():
            if child.winfo_class() == "Frame":
                for child_ in child.winfo_children():
                    if child_.winfo_class() == "Label":
                        child_["fg"] = color

    # Need to change according to tab
    def toggle_checkbox(self,selected,btn_widget,btn_obj,base_frame):
        print(selected)
        if selected == True:
            btn_obj.update_btn_image(imgTk=image__.icons("select_box".lower(),dimension=(14,14)), imgTk_hover=image__.icons("select_box".lower()+"_hover",dimension=(14,14)))
            btn_widget["command"] = lambda selected = False, btn_widget = btn_widget, btn_obj = btn_obj , base_frame=base_frame: self.toggle_checkbox(selected,btn_widget,btn_obj,base_frame)
            self.toggle_checkbox_highlighter(base_frame, Colors__.color()["task"]["fg"])
        else:
            btn_obj.update_btn_image(imgTk=image__.icons("select_box_selected".lower(),dimension=(14,14)), imgTk_hover=image__.icons("select_box_selected".lower()+"_hover",dimension=(14,14)))
            btn_widget["command"] = lambda selected = True, btn_widget = btn_widget, btn_obj = btn_obj, base_frame=base_frame: self.toggle_checkbox(selected,btn_widget,btn_obj,base_frame)
            self.toggle_checkbox_highlighter(base_frame, Colors__.color()["task"]["active fg"])