from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
from colors import *




def tab_button_icon(icon:object = None, text:str = None, text_bg:str = None, img_width:int = 286, img_original_height:int =18, diff_icon_text:int = 250):

    width, height = (len(text)*img_width, 512+140-140)
    position = (0,110)
    # Create Text Image
    text_image = Image.new("RGBA", (width, height), 0)
    font = ImageFont.truetype('./res/fonts/OxfordStreet.ttf', size=512+190-190-90)
    draw = ImageDraw.Draw(text_image)
    draw.text(position, text, font=font, fill=text_bg)
    # Marge Text Image with Icon
    total_width = width + 512 + diff_icon_text
    merged_image = Image.new("RGBA", (total_width, height), 0)
    merged_image.paste(icon, (0, 0))
    merged_image.paste(text_image, (512+diff_icon_text, 0))

    final_image = merged_image.resize((int((total_width/height)*img_original_height),img_original_height),Image.LANCZOS)
    # final_image.show()
    # print(final_image.size)
    return ImageTk.PhotoImage(final_image)


class image__:
    def __init__(self) -> None:
        pass

    def icons(name, dimension=()):
        if name == "logo": return ImageTk.PhotoImage(Image.open("./res/icons/logo.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        # Window control
        elif name == "terminate": return ImageTk.PhotoImage(Image.open("./res/icons/terminate.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "terminate_hover": return ImageTk.PhotoImage(Image.open("./res/icons/terminate_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "minimize": return ImageTk.PhotoImage(Image.open("./res/icons/minimize.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "minimize_hover": return ImageTk.PhotoImage(Image.open("./res/icons/minimize_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        # Notification
        elif name == "notification": return ImageTk.PhotoImage(Image.open("./res/icons/notification.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "notification_hover": return ImageTk.PhotoImage(Image.open("./res/icons/notification_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "pending_notification": return ImageTk.PhotoImage(Image.open("./res/icons/pending_notification.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "pending_notification_hover": return ImageTk.PhotoImage(Image.open("./res/icons/pending_notification_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        # Tab
        elif name == "task": return tab_button_icon(icon=Image.open("./res/icons/tabs/task.png"),text="Tasks",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=193)
        elif name == "task_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/task_hover.png"),text="Tasks",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=193)
        elif name == "task_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/task_selected.png"),text="Tasks",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=193)

        elif name == "billing": return tab_button_icon(icon=Image.open("./res/icons/tabs/billing.png"),text="Billings",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=193)
        elif name == "billing_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/billing_hover.png"),text="Billings",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=193)
        elif name == "billing_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/billing_selected.png"),text="Billings",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=193)

        elif name == "proxies": return tab_button_icon(icon=Image.open("./res/icons/tabs/proxies.png"),text="Proxies",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=174)
        elif name == "proxies_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/proxies_hover.png"),text="Proxies",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=174)
        elif name == "proxies_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/proxies_selected.png"),text="Proxies",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=174)

        elif name == "capture": return tab_button_icon(icon=Image.open("./res/icons/tabs/capture.png"),text="Capture",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=184)
        elif name == "capture_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/capture_hover.png"),text="Capture",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=184)
        elif name == "capture_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/capture_selected.png"),text="Capture",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=184)

        elif name == "settings": return tab_button_icon(icon=Image.open("./res/icons/tabs/settings.png"),text="Settings",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=172)
        elif name == "settings_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/settings_hover.png"),text="Settings",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=172)
        elif name == "settings_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/settings_selected.png"),text="Settings",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=172)


        # Control
        elif name == "add_new": return ImageTk.PhotoImage(Image.open("./res/icons/control/add_new.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "add_new_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/add_new_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "delete": return ImageTk.PhotoImage(Image.open("./res/icons/control/delete.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "delete_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/delete_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "paush": return ImageTk.PhotoImage(Image.open("./res/icons/control/paush.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "paush_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/paush_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "run": return ImageTk.PhotoImage(Image.open("./res/icons/control/run.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "run_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/run_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "edit": return ImageTk.PhotoImage(Image.open("./res/icons/control/edit.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "edit_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/edit_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "stop": return ImageTk.PhotoImage(Image.open("./res/icons/control/stop.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "stop_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/stop_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        #Select Box
        elif name == "select_box": return ImageTk.PhotoImage(Image.open("./res/icons/select_box.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))
        elif name == "select_box_hover": return ImageTk.PhotoImage(Image.open("./res/icons/select_box_hover.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))

        elif name == "select_box_selected": return ImageTk.PhotoImage(Image.open("./res/icons/select_box_selected.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))
        elif name == "select_box_selected_hover": return ImageTk.PhotoImage(Image.open("./res/icons/select_box_selected_hover.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))


        # Save
        elif name == "save": return ImageTk.PhotoImage(Image.open("./res/icons/save.png").resize((dimension if len(dimension) == 2 else (107, 35)), Image.LANCZOS))
        elif name == "save_hover": return ImageTk.PhotoImage(Image.open("./res/icons/save_hover.png").resize((dimension if len(dimension) == 2 else (107, 35)), Image.LANCZOS))

        ## Save
        elif name == "activate": return ImageTk.PhotoImage(Image.open("./res/icons/activate.png").resize((dimension if len(dimension) == 2 else (116, 40)), Image.LANCZOS))
        elif name == "activate_hover": return ImageTk.PhotoImage(Image.open("./res/icons/activate_hover.png").resize((dimension if len(dimension) == 2 else (116, 40)), Image.LANCZOS))









