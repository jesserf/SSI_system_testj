from typing import Optional, Tuple, Union
import customtkinter as ctk
from typing import *
import datetime
from Theme import Color
from PIL import Image
from customcustomtkinter import customcustomtkinter as cctk
from tkinter import messagebox
import re
from util import database
from util import *


class pet_info_frame(ctk.CTkFrame):
    def __init__(self, master: any, title:str, name_select_callback: callable, name_selection:list = None, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        #self.pack_propagate(0)
        self._title = title
        self._corner_radius = 0
        self._fg_color= Color.White_Platinum
        self.grid_columnconfigure(0, weight=1)
        self.name_select_callback = name_select_callback
        
        self.pholder = ctk.CTkImage(light_image=Image.open("image/pholder.png"), size=(100,100))
        self.calendar= ctk.CTkImage(light_image=Image.open("image/calendar.png"), size=(18,18))
        
        ctk.CTkFrame(self, height=height*0.035, fg_color=Color.Blue_Yale, corner_radius=0).grid(row=0, column=0, sticky="nsew")
        
        self.main_frame = ctk.CTkFrame(self, fg_color=Color.White_Platinum)
        self.main_frame.grid(row =1, column=0, sticky ="nsew")
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.main_frame, text = title.title(), font=('DM Sans Medium', 16), fg_color=Color.White_Lotion, corner_radius=5, 
                     width=width*0.4).grid(row=0, column=0, padx=(width*0.05), pady=(height*0.05), sticky="n")
        
        self.info_frame = ctk.CTkFrame(self.main_frame, fg_color=Color.White_Lotion)
        self.info_frame.grid(row = 0, column=1, padx=(0, width*0.05), pady=(height*0.05), sticky="nsew")
        self.info_frame.grid_rowconfigure(0, weight=1)
        
        ctk.CTkLabel(self.info_frame, text="", image=self.pholder).grid(row=0,column=0, rowspan=2, sticky="nsew",padx=(width*0.05,width*0.0015), pady=(height*0.05))
        self.sub_frame =ctk.CTkFrame(self.info_frame, fg_color="transparent")
        self.sub_frame.grid(row=0, column=1, sticky="nsew")
        ctk.CTkLabel(self.sub_frame, text =f'Name: ', font=("DM Sans Medium",14), anchor='e', width=width*0.35).grid(row=0, column=0,sticky="n", pady=(height*0.05,0))
        self.name = ctk.CTkOptionMenu(self.sub_frame, values= name_selection or None, font=("DM Sans Medium", 14), width=width*1.15, height=height*0.225, dropdown_fg_color=Color.White_AntiFlash,  fg_color=Color.White_Platinum,
                                                 text_color=Color.Blue_Maastricht, button_color=Color.Blue_Tufts,)
        self.name.configure(command = lambda _: name_select_callback(self, self.name.get()))
        self.name.grid(row=0, column=1, columnspan=2, sticky="nsew", pady=(height*0.05,0))
        self.name.set('')
        
        ctk.CTkLabel(self.sub_frame, text =f'Date: ', font=("DM Sans Medium",14), anchor='e', width=width*0.35).grid(row=1, column=0,sticky="n", pady=(height*0.05))
        self.first_date_entry = ctk.CTkLabel(self.sub_frame, width=width*1.15,  height=height*0.225, text="Set Date", font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5)
        self.first_date_entry.grid(row=1, column=1, sticky="n", pady=(height*0.05,0)) 
        
        self.first_date_btn = ctk.CTkButton(self.sub_frame, text="", image=self.calendar, height=height*0.225, width=width*0.18,
                                            command=lambda:cctk.tk_calendar(self.first_date_entry, "%s", date_format="numerical", min_date=datetime.datetime.now()))
        self.first_date_btn.grid(row=1,column=2, sticky="w", pady=(height*0.05,0))
        #enable this part when service requires multiple days
        """ctk.CTkLabel(self.sub_frame, text ="up to", font=("DM Sans Medium",12), width=width*0.35).grid(row=2, column=1,sticky="nsew")
        self.second_date_entry = ctk.CTkLabel(self.sub_frame, width=width*1.15,  height=height*0.225, text="Set Date", font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5)
        self.second_date_entry.grid(row=3, column=1, sticky="n", pady=(0,height*0.05)) 
        
        self.second_date_btn = ctk.CTkButton(self.sub_frame, text="", image=self.calendar, height=height*0.225, width=width*0.18,
                                            command=lambda:cctk.tk_calendar(self.second_date_entry, "%s", date_format="numerical", min_date=datetime.datetime.now()))
        self.second_date_btn.grid(row=3,column=2, sticky="w", pady=(0,height*0.05))"""
        
    '''functions'''
    def get_data(self, data_format: Literal['metadata', 'tuple']) -> dict | list:
        if data_format == 'metadata':
            return {'name': self.name.get(), 'schedule': self.date.get()}
        elif data_format == 'tuple':
            d_temp = None if self.first_date_entry._text == "Set Date" else datetime.datetime.strptime(self.first_date_entry._text, "%m-%d-%Y").strftime('%Y-%m-%d')
            return (self.name.get(), d_temp)
        
class pet_period_info_frame(ctk.CTkFrame):
    def __init__(self, master: any, title:str, name_select_callback: callable, name_selection:list = None, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self._title = title
        self._corner_radius = 0
        self._fg_color= Color.White_Platinum
        self.grid_columnconfigure(0, weight=1)
        self.name_select_callback = name_select_callback
        
        self.pholder = ctk.CTkImage(light_image=Image.open("image/pholder.png"), size=(100,100))
        self.calendar= ctk.CTkImage(light_image=Image.open("image/calendar.png"), size=(18,18))
        
        ctk.CTkFrame(self, height=height*0.035, fg_color=Color.Blue_Yale, corner_radius=0).grid(row=0, column=0, sticky="nsew")
        
        self.main_frame = ctk.CTkFrame(self, fg_color=Color.White_Platinum)
        self.main_frame.grid(row =1, column=0, sticky ="nsew")
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.main_frame, text = title.title(), font=('DM Sans Medium', 16), fg_color=Color.White_Lotion, corner_radius=5, 
                     width=width*0.4).grid(row=0, column=0, padx=(width*0.05), pady=(height*0.05), sticky="n")
        
        self.info_frame = ctk.CTkFrame(self.main_frame, fg_color=Color.White_Lotion)
        self.info_frame.grid(row = 0, column=1, padx=(0, width*0.05), pady=(height*0.05), sticky="nsew")
        self.info_frame.grid_rowconfigure(0, weight=1)
        
        ctk.CTkLabel(self.info_frame, text="", image=self.pholder).grid(row=0,column=0, rowspan=2, sticky="nsew",padx=(width*0.05,width*0.0015), pady=(height*0.05))
        self.sub_frame =ctk.CTkFrame(self.info_frame, fg_color="transparent")
        self.sub_frame.grid(row=0, column=1, sticky="nsew")
        ctk.CTkLabel(self.sub_frame, text =f'Name: ', font=("DM Sans Medium",14), anchor='e', width=width*0.35).grid(row=0, column=0,sticky="n", pady=(height*0.05,0))
        self.name = ctk.CTkOptionMenu(self.sub_frame, values= name_selection or None, font=("DM Sans Medium", 14), width=width*1.15, height=height*0.225, dropdown_fg_color=Color.White_AntiFlash,  fg_color=Color.White_Platinum,
                                                 text_color=Color.Blue_Maastricht, button_color=Color.Blue_Tufts,)
        self.name.configure(command = lambda _: name_select_callback(self, self.name.get()))
        self.name.grid(row=0, column=1, columnspan=2, sticky="nsew", pady=(height*0.05,0))
        self.name.set('')
        
        ctk.CTkLabel(self.sub_frame, text =f'Date: ', font=("DM Sans Medium",14), anchor='e', width=width*0.35).grid(row=1, column=0,sticky="n", pady=(height*0.05))
        self.first_date_entry = ctk.CTkLabel(self.sub_frame, width=width*1.15,  height=height*0.225, text="Set Date", font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5)
        self.first_date_entry.grid(row=1, column=1, sticky="n", pady=(height*0.05,0)) 
        
        self.first_date_btn = ctk.CTkButton(self.sub_frame, text="", image=self.calendar, height=height*0.225, width=width*0.18,
                                            command=lambda:cctk.tk_calendar(self.first_date_entry, "%s", date_format="numerical", min_date=datetime.datetime.now()))
        self.first_date_btn.grid(row=1,column=2, sticky="w", pady=(height*0.05,0))
        #enable this part when service requires multiple days
        ctk.CTkLabel(self.sub_frame, text ="up to", font=("DM Sans Medium",12), width=width*0.35).grid(row=2, column=1,sticky="nsew")
        self.second_date_entry = ctk.CTkLabel(self.sub_frame, width=width*1.15,  height=height*0.225, text="Set Date", font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5)
        self.second_date_entry.grid(row=3, column=1, sticky="n", pady=(0,height*0.05)) 
        
        self.second_date_btn = ctk.CTkButton(self.sub_frame, text="", image=self.calendar, height=height*0.225, width=width*0.18,
                                            command=lambda:cctk.tk_calendar(self.second_date_entry, "%s", date_format="numerical", min_date=datetime.datetime.strptime(self.first_date_entry._text, '%m-%d-%Y') if not self.first_date_entry._text.startswith("Set") else datetime.datetime.now()))
        self.second_date_btn.grid(row=3,column=2, sticky="w", pady=(0,height*0.05))
        
    '''functions'''
    def get_data(self, data_format: Literal['metadata', 'tuple']) -> dict | list:
        if data_format == 'metadata':
            return {'name': self.name.get(), 'schedule': self.date.get()}
        elif data_format == 'tuple':
            d_temp = None if self.first_date_entry._text == "Set Date" else datetime.datetime.strptime(self.first_date_entry._text, "%m-%d-%Y").strftime('%Y-%m-%d')
            dt_temp = None if self.second_date_entry._text == "Set Date" else datetime.datetime.strptime(self.second_date_entry._text, "%m-%d-%Y").strftime('%Y-%m-%d')
            return (self.name.get(), d_temp, dt_temp)
        
class pet_multiple_period_info_frame(ctk.CTkFrame):
    def __init__(self, master: any, title:str, name_select_callback: callable, name_selection:list = None, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self._title = title
        self._corner_radius = 0
        self._fg_color= Color.White_Platinum
        self.grid_columnconfigure(0, weight=1)
        self.name_select_callback = name_select_callback
        
        self.pholder = ctk.CTkImage(light_image=Image.open("image/pholder.png"), size=(100,100))
        self.calendar= ctk.CTkImage(light_image=Image.open("image/calendar.png"), size=(18,18))
        
        ctk.CTkFrame(self, height=height*0.035, fg_color=Color.Blue_Yale, corner_radius=0).grid(row=0, column=0, sticky="nsew")
        
        self.main_frame = ctk.CTkFrame(self, fg_color=Color.White_Platinum)
        self.main_frame.grid(row =1, column=0, sticky ="nsew")
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.main_frame, text = title.title(), font=('DM Sans Medium', 16), fg_color=Color.White_Lotion, corner_radius=5, 
                     width=width*0.4).grid(row=0, column=0, padx=(width*0.05), pady=(height*0.05), sticky="n")
        
        self.info_frame = ctk.CTkFrame(self.main_frame, fg_color=Color.White_Lotion)
        self.info_frame.grid(row = 0, column=1, padx=(0, width*0.05), pady=(height*0.05), sticky="nsew")
        self.info_frame.grid_rowconfigure(0, weight=1)
        
        ctk.CTkLabel(self.info_frame, text="", image=self.pholder).grid(row=0,column=0, rowspan=2, sticky="nsew",padx=(width*0.05,width*0.0015), pady=(height*0.05))
        self.sub_frame =ctk.CTkFrame(self.info_frame, fg_color="transparent")
        self.sub_frame.grid(row=0, column=1, sticky="nsew")
        ctk.CTkLabel(self.sub_frame, text =f'Name: ', font=("DM Sans Medium",14), anchor='e', width=width*0.35).grid(row=0, column=0,sticky="n", pady=(height*0.05,0))
        self.name = ctk.CTkOptionMenu(self.sub_frame, values= name_selection or None, font=("DM Sans Medium", 14), width=width*1.15, height=height*0.225, dropdown_fg_color=Color.White_AntiFlash,  fg_color=Color.White_Platinum,
                                                 text_color=Color.Blue_Maastricht, button_color=Color.Blue_Tufts,)
        self.name.configure(command = lambda _: name_select_callback(self, self.name.get()))
        self.name.grid(row=0, column=1, columnspan=2, sticky="nsew", pady=(height*0.05,0))
        self.name.set('')
        
        ctk.CTkLabel(self.sub_frame, text =f'Date: ', font=("DM Sans Medium",14), anchor='e', width=width*0.35).grid(row=1, column=0,sticky="n", pady=(height*0.05))
        self.first_date_entry = ctk.CTkLabel(self.sub_frame, width=width*1.15,  height=height*0.225, text="Set Date", font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5)
        self.first_date_entry.grid(row=1, column=1, sticky="n", pady=(height*0.05,0)) 
        
        self.first_date_btn = ctk.CTkButton(self.sub_frame, text="", image=self.calendar, height=height*0.225, width=width*0.18,
                                            command=lambda:cctk.tk_calendar(self.first_date_entry, "%s", date_format="numerical", min_date=datetime.datetime.now()))
        self.first_date_btn.grid(row=1,column=2, sticky="w", pady=(height*0.05,0))
        #enable this part when service requires multiple days
        ctk.CTkLabel(self.sub_frame, text ="Scheduled every", font=("DM Sans Medium",12), width=width*0.35).grid(row=2, column=1,sticky="nsew")
        '''self.second_date_entry = ctk.CTkLabel(self.sub_frame, width=width*1.15,  height=height*0.225, text="Set Date", font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5)
        self.second_date_entry.grid(row=3, column=1, sticky="n", pady=(0,height*0.05)) 
        
        self.second_date_btn = ctk.CTkButton(self.sub_frame, text="", image=self.calendar, height=height*0.225, width=width*0.18,
                                            command=lambda:cctk.tk_calendar(self.second_date_entry, "%s", date_format="numerical", min_date=datetime.datetime.strptime(self.first_date_entry._text, '%m-%d-%Y') if not self.first_date_entry._text.startswith("Set") else datetime.datetime.now()))
        self.second_date_btn.grid(row=3,column=2, sticky="w", pady=(0,height*0.05))'''
        period_sv = ctk.StringVar()
        period_sv.trace_add('write', self.period_days_callback)
        self.period_days = ctk.CTkEntry(self.sub_frame, width=width*1.15,  height=height*0.225, font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5, textvariable= period_sv)
        self.period_days.grid(row=3, column=1, sticky="n", pady=(0,height*0.05))
        ctk.CTkLabel(self.sub_frame, text ="Days", font=("DM Sans Medium",12), width=width*0.35).grid(row=3,column=2, sticky="w", pady=(0,height*0.05), padx = (height*0.05, 0))

        insct_sv = ctk.StringVar()
        insct_sv.trace_add('write', self.instance_count_callback)
        ctk.CTkLabel(self.sub_frame, text ="For", font=("DM Sans Medium",12), width=width*0.35).grid(row=4, column=1,sticky="nsew")
        self.instance_count_days = ctk.CTkEntry(self.sub_frame, width=width*1.15,  height=height*0.225, font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Platinum, corner_radius=5, textvariable= insct_sv)
        self.instance_count_days.grid(row=5, column=1, sticky="n", pady=(0,height*0.05))
        ctk.CTkLabel(self.sub_frame, text ="Times", font=("DM Sans Medium",12), width=width*0.35).grid(row=5,column=2, sticky="w", pady=(0,height*0.05), padx = (height*0.05, 0))

    '''functions'''
    def get_data(self, data_format: Literal['metadata', 'tuple']) -> dict | list:
        if data_format == 'metadata':
            return {'name': self.name.get(), 'schedule': self.date.get()}
        elif data_format == 'tuple':
            d_temp = None if self.first_date_entry._text == "Set Date" else datetime.datetime.strptime(self.first_date_entry._text, "%m-%d-%Y").strftime('%Y-%m-%d')
            prd_temp = self.period_days.get()
            ins_ct = self.instance_count_days.get()
            return (self.name.get(), d_temp, prd_temp, ins_ct)
        
    def period_days_callback(self, _ = None, *__):
        txt = self.period_days.get()
        if (not str(txt[-1]).isnumeric()) or len(txt) > 15:
            self.period_days.delete(len(txt)-1, ctk.END)

    def instance_count_callback(self, _ = None, *__):
        txt = self.instance_count_days.get()
        if (not str(txt[-1]).isnumeric()) or len(txt) > 15:
            self.instance_count_days.delete(len(txt)-1, ctk.END)

class pets(ctk.CTkFrame):
    def __init__(self, master: any, length:int, title: str, pets_name: List[str], proceed_command:callable, cancel_command:callable = None, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.grid_propagate(0)
        self.frames: List[pet_info_frame] = []
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_propagate(0)
        self.parent_frame_tab = None
        self.parent_service_dict: dict = {}
        self._title = title
        self.service_icon = ctk.CTkImage(light_image=Image.open("image/services.png"), size=(20,20))
        self._type = database.fetch_data("Select duration_type from service_info_test WHERE service_name = ?", (self._title, ))[0][0]
        self.change_total_val_serv_callback = None
        def cancel_sequence():
            if cancel_command:
                cancel_command()
            self.place_forget()

        def proceed_sequence():
            for fr in self.frames:
                if fr.name.get() == "" or fr.first_date_entry._text == "Set Date":
                    messagebox.showerror("Fail to proceed", "Fill all the required info")
                    return
                if isinstance(fr, pet_period_info_frame):
                    temp: pet_period_info_frame = fr
                    if temp.second_date_entry._text == "Set Date":
                        messagebox.showerror("Fail to proceed", "Fill all the required info")
                        return
                elif isinstance(fr, pet_multiple_period_info_frame):
                    temp: pet_multiple_period_info_frame = fr
                    if temp.period_days.get() == "" or temp.instance_count_days.get() == "":
                        messagebox.showerror("Fail to proceed", "Fill all the required info")
                        return

            original_price = price_format_to_float(self.parent_frame_tab.winfo_children()[1]._text[1:])
            total_price_lbl = self.parent_frame_tab.winfo_children()[3]
            
            quan_list: list = []
            for temp_data in self.get_data():
                if self._type == 1:
                    d2 = datetime.datetime.strptime(temp_data[2], '%Y-%m-%d')
                    d1 = datetime.datetime.strptime(temp_data[1], '%Y-%m-%d')
                    quan_list.append(((d2-d1).days + 1))
                    '''total_price_lbl.configure(text = f"₱{format_price(original_price * ((d2-d1).days + 1))}",
                                            fg_color = "yellow")'''
                elif self._type == 2:
                    count_intsc = temp_data[-1]
                    quan_list.append(count_intsc)
                    '''total_price_lbl.configure(text = f"₱{format_price(original_price * float(count_intsc))}",
                                            fg_color = "yellow")'''
                    
            total_price_lbl.configure(text = f"₱{format_price(original_price * sum(quan_list))}", fg_color = 'yellow')
            frame_spinner: cctk.cctkSpinnerCombo = self.parent_frame_tab.winfo_children()[2].winfo_children()[0]


            if self._type == 1:
                def new_frame_spn_cmd():
                    if self._title in self.parent_service_dict:
                        self.parent_service_dict[self._title] = [] if frame_spinner.value < 1 else self.parent_service_dict[self._title][0: frame_spinner.value]
                def decrease_callback():
                    self.change_total_val_serv_callback(quan_list[-1] * original_price)
                    quan_list.pop()
                    total_price_lbl.configure(text = f"₱{format_price(original_price * sum(quan_list))}", fg_color = 'yellow')
                frame_spinner.configure(command = new_frame_spn_cmd, decrease_callback= decrease_callback)
                self.change_total_val_serv_callback(-original_price * frame_spinner.value)
                self.change_total_val_serv_callback(original_price * sum(quan_list))

            #for modifying the price of the calculated time period
            #need to fix: no effects on total price, their spinner command, partially bugged

            proceed_command(self.get_data())
            self.place_forget()
            
        def update_frames_selection(sender: ctk.CTkOptionMenu, to_remove: str) -> None:
            for i in self.frames:
                if i is not sender:
                    temp = pets_name.copy()
                    temp.pop(temp.index(to_remove))
                    i.name.configure(values = temp)
        #manage the selection of each patient frames to prevent duplicate pets 

        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=Color.White_Lotion)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_propagate(0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        self.top_frame = ctk.CTkFrame(self.main_frame, fg_color=Color.Blue_Yale, corner_radius=0, height=height*0.085)
        self.top_frame.grid(row=0, column=0, sticky="ew")
        
        ctk.CTkLabel(self.top_frame,text="", image=self.service_icon,).pack(side="left", padx=(self._current_width*0.015,0))
        ctk.CTkLabel(self.top_frame, text = f"{self._title}", font = ("DM Sans Medium", 16), anchor='w', text_color="white").pack(side="left", padx=self._current_width * 0.005)
        ctk.CTkButton(self.top_frame, text="X",width=width*0.0225, command=cancel_sequence).pack(side="right", padx=(0,width*0.01),pady=height*0.005)
        
        self.content_frame = ctk.CTkScrollableFrame(self.main_frame, self._current_width *0.5, self._current_height * .8, fg_color ='transparent')
        self.content_frame.grid(row = 1, column = 0, sticky="nsew", padx=(width*0.01,0), pady=(0, height*0.01))
        
        #content frame
        
        for _ in range(length):
            if self._type == 2:
                self.frames.append(pet_multiple_period_info_frame(self.content_frame, f'pet {_ + 1}', name_selection=pets_name, height=height*0.35, name_select_callback= update_frames_selection))
            elif self._type == 1:
                self.frames.append(pet_period_info_frame(self.content_frame, f'pet {_ + 1}', name_selection=pets_name, height=height*0.35, name_select_callback= update_frames_selection))
            elif self._type == 0:
                self.frames.append(pet_info_frame(self.content_frame, f'pet {_ + 1}', name_selection=pets_name, height=height*0.35, name_select_callback= update_frames_selection))

            self.frames[-1].pack(fill = 'x', side = 'top', pady = (0, 5))
        #generate the patient info catalogs, length varies to the given length

        self.bot_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.bot_frame.grid(row = 2, column=0, sticky="nsew")
        
        self.proceed_btn = ctk.CTkButton(self.bot_frame, self._current_width * .15, self._current_height * .08, text='Proceed', command= proceed_sequence, font=("DM Sans Medium", 16),)
        self.proceed_btn.pack(side="right", padx=(0,width*0.025))
        self.cancel_btn = ctk.CTkButton(self.bot_frame, self._current_width * .15, self._current_height * .08, text='Cancel', command=cancel_sequence,
                                         fg_color=Color.Red_Pastel, hover_color=Color.Red_Tulip,font=("DM Sans Medium", 16))
        self.cancel_btn.pack(side="right",  padx=(width*0.025))


    '''functions'''
    def get_data(self) -> list:
        data = []
        for i in self.frames:
            data.append(i.get_data(data_format='tuple'))
        return data
    
    def place(self, service_dict: dict, master_frame: any, change_total_val_serv_callback: callable, **kwargs):
        self.parent_frame_tab = master_frame
        self.parent_service_dict = service_dict
        self.change_total_val_serv_callback = change_total_val_serv_callback
        frame_spinner: cctk.cctkSpinnerCombo = self.parent_frame_tab.winfo_children()[2].winfo_children()[0]
        temp_cmd = frame_spinner._command

        if self._type == 0:
            def new_frame_spn_cmd():
                if self._title in service_dict:
                    service_dict[self._title] = [] if frame_spinner.value < 1 else service_dict[self._title][0: frame_spinner.value]
                temp_cmd()
            frame_spinner.configure(command = new_frame_spn_cmd)
        #for modifying the spinnercombo of the table

        if(self._title in service_dict):
            for i in range(len(service_dict[self._title])):
                self.frames[i].name.set(service_dict[self._title][i][0])
                self.frames[i].name_select_callback(self.frames[i], self.frames[i].name.get())
                d_temp = "Set Date" if service_dict[self._title][i][1] is None else datetime.datetime.strptime(service_dict[self._title][i][1], "%Y-%m-%d").strftime("%m-%d-%Y")
                self.frames[i].first_date_entry.configure(text =  d_temp)

                if self._type == 1:
                    temp: pet_period_info_frame = self.frames[i]
                    snd_temp = "Set Date" if service_dict[self._title][i][2] is None else datetime.datetime.strptime(service_dict[self._title][i][2], "%Y-%m-%d").strftime("%m-%d-%Y")
                    temp.second_date_entry.configure(text = snd_temp)
                elif self._type == 2:
                    temp: pet_multiple_period_info_frame = self.frames[i]
                    temp.period_days.delete(0, ctk.END)
                    temp.period_days.insert(0, service_dict[self._title][i][2])
                    temp.instance_count_days.delete(0, ctk.END)
                    temp.instance_count_days.insert(0, service_dict[self._title][i][3])
        #for reentring the elements based on the type of service
        return super().place(**kwargs)
    
class body(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.state("zoomed")
        self.update()
        self.attributes("-fullscreen", True)

        #pets1 = pets(self, 2, 'test', self.winfo_screenwidth() * .65, self.winfo_screenheight() * .65, fg_color= 'red')
        pets1 = pets(self, 2, 'grooming', ['hello', 'world'], None, None, self.winfo_screenwidth() * .65, self.winfo_screenheight() * .65, fg_color= 'red')
        pets1.place(relx = .5, rely = .5, anchor = 'c')
        
        self.mainloop()

#body()