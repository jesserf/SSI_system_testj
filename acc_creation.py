from typing import *
from typing import Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk;
from customcustomtkinter import customcustomtkinter as cctk
from PIL import Image
from Theme import Color

""" class frame2(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self._fg_color ="light grey"
        self.pack_propagate(0)

        self.upperframe = ctk.CTkFrame(self, self._current_width * .95, self._current_height * .85, 0, fg_color='transparent')
        self.upperframe.pack(padx = (self._current_width * .025, self._current_width * .025), pady = (self. _current_height * 0.025, 0))
        self.pack_propagate(0)

        self.left_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.left_frame.pack(side = 'left', padx = (0, self._current_width * .0125))
        self.left_frame.grid_propagate(0)
        ctk.CTkLabel(self.left_frame, text= "Account", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0), pady=(12,0), sticky="w")

        '''ctk.CTkLabel(self.left_frame, text= "Full name", font=("Arial", 15)).grid(row = 1, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.name_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.name_entry.grid(row = 2, column = 0, padx = (7, 0))'''

        ctk.CTkLabel(self.left_frame, text= "Username", font=("Arial", 15)).grid(row = 3, column = 0, padx = (7, 0), pady = (12, 0), sticky = 'w')
        self.usn_option = ctk.CTkOptionMenu(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.usn_option.grid(row = 4, column = 0, padx = (7, 0))
        self.usn_option.set("Select a user")

        ctk.CTkLabel(self.left_frame, text= "Position", font=("Arial", 15)).grid(row = 5, column = 0, padx = (7, 0), pady = (12, 0), sticky = 'w')
        self.selected_role_option = ctk.CTkOptionMenu(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8, state=ctk.DISABLED)
        self.selected_role_option.grid(row = 6, column = 0, padx = (7, 0))
        self.selected_role_option.set("Job Position")

        '''ctk.CTkLabel(self.left_frame, text= "USN", font=("Arial", 15)).grid(row = 5, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.usn_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.usn_entry.grid(row = 6, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Password", font=("Arial", 15)).grid(row = 7, column = 0, padx = (7, 0), pady = (7, 0), sticky = 'w')
        self.pss_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.pss_entry.grid(row = 8, column = 0, padx = (7, 0))'''

        self.right_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.right_frame.pack(side = 'left', padx = (self._current_width * .0125, 0));
        self.right_frame.grid_propagate(0)
        ctk.CTkLabel(self.right_frame, text= "Access Level", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0))

        self.access_lvl_frame = ctk.CTkFrame(self.right_frame, self.right_frame._current_width * .91, self.right_frame._current_height * .91, fg_color='white')
        self.access_lvl_frame.grid(row = 1, column = 0, sticky = 'we', padx = 7, pady = 7)
        self.access_lvl_frame.grid_propagate(0)

        self.access_lvls: List[str] = ['Dashboard', 'Transaction', 'Services', 'Sales', 'Inventory', 'Pet Information', 'Report', 'Users', 'Action Log']
        self.check_boxes: Dict[str, ctk.CTkCheckBox] = {}
        for i in range(len(self.access_lvls)):
            self.check_boxes[self.access_lvls[i]] = ctk.CTkCheckBox(self.access_lvl_frame, self.access_lvl_frame._current_width * .95, 24,
                                                                    text=self.access_lvls[i], state=ctk.DISABLED);
            self.check_boxes[self.access_lvls[i]].grid(row = i, column = 0, padx = 7, pady = 7);
            

        self.accept_button = ctk.CTkButton(self, 140, 50, 12, text="Proceed")
        self.accept_button.pack(anchor = 'e', padx = (0, self._current_width * .025), pady = (self._current_width * .0125))



class frame(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.pack_propagate(0)

        self.upperframe = ctk.CTkFrame(self, self._current_width * .95, self._current_height * .85, 0, fg_color='transparent')
        self.upperframe.pack(padx = (self._current_width * .025, self._current_width * .025), pady = (self. _current_height * 0.025, 0))
        self.pack_propagate(0)

        self.left_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.left_frame.pack(side = 'left', padx = (0, self._current_width * .0125));
        self.left_frame.grid_propagate(0)
        ctk.CTkLabel(self.left_frame, text= "Account Credentials", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Full name", font=("Arial", 15)).grid(row = 1, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.name_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.name_entry.grid(row = 2, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Position", font=("Arial", 15)).grid(row = 3, column = 0, padx = (7, 0), pady = (12, 0), sticky = 'w')
        self.position_option = ctk.CTkOptionMenu(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.position_option.grid(row = 4, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "USN", font=("Arial", 15)).grid(row = 5, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.usn_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.usn_entry.grid(row = 6, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Password", font=("Arial", 15)).grid(row = 7, column = 0, padx = (7, 0), pady = (7, 0), sticky = 'w')
        self.pss_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.pss_entry.grid(row = 8, column = 0, padx = (7, 0))

        self.right_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.right_frame.pack(side = 'left', padx = (self._current_width * .0125, 0));
        self.right_frame.grid_propagate(0)
        ctk.CTkLabel(self.right_frame, text= "Access Level", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0))

        self.access_lvl_frame = ctk.CTkFrame(self.right_frame, self.right_frame._current_width * .91, self.right_frame._current_height * .91, fg_color='white')
        self.access_lvl_frame.grid(row = 1, column = 0, sticky = 'we', padx = 7, pady = 7)
        self.access_lvl_frame.grid_propagate(0)

        self.access_lvls: List[str] = ['Dashboard', 'Transaction', 'Services', 'Sales', 'Inventory', 'Pet Information', 'Report', 'Users', 'Action Log']
        self.check_boxes: Dict[str, ctk.CTkCheckBox] = {}
        for i in range(len(self.access_lvls)):
            self.check_boxes[self.access_lvls[i]] = ctk.CTkCheckBox(self.access_lvl_frame, self.access_lvl_frame._current_width * .95, 24,
                                                                    text=self.access_lvls[i], state=ctk.DISABLED);
            self.check_boxes[self.access_lvls[i]].grid(row = i, column = 0, padx = 7, pady = 7);
            

        self.accept_button = ctk.CTkButton(self, 140, 50, 12, text="Proceed")
        self.accept_button.pack(anchor = 'e', padx = (0, self._current_width * .025), pady = (self._current_width * .0125)) """

""" class body(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.state("zoomed")
        self.update()
        self.attributes("-fullscreen", True)
        self.update()
        width = self.winfo_vrootwidth()
        height = self.winfo_vrootheight()

        self.frame = frame2(self, width * .4, height * .5, 12, fg_color= 'gray')
        self.frame.place(relx = .5, rely = .5, anchor = 'c')

        self.mainloop() """

class frame2(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self._fg_color ="white"
        self.pack_propagate(0)

        self.upperframe = ctk.CTkFrame(self, self._current_width * .95, self._current_height * .85, 0, fg_color='transparent')
        self.upperframe.pack(padx = (self._current_width * .025, self._current_width * .025), pady = (self. _current_height * 0.025, 0))
        self.pack_propagate(0)

        self.left_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.left_frame.pack(side = 'left', anchor='nw', padx = (0, self._current_width * .0125))
        self.left_frame.grid_propagate(0)
        ctk.CTkLabel(self.left_frame, text= "Account", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0), pady=(12,0), sticky="w")

        '''ctk.CTkLabel(self.left_frame, text= "Full name", font=("Arial", 15)).grid(row = 1, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.name_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.name_entry.grid(row = 2, column = 0, padx = (7, 0))'''

        ctk.CTkLabel(self.left_frame, text= "Username", font=("Arial", 15)).grid(row = 3, column = 0, padx = (7, 0), pady = (12, 0), sticky = 'w')
        self.usn_option = ctk.CTkOptionMenu(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.usn_option.grid(row = 4, column = 0, padx = (7, 0))
        self.usn_option.set("Select a user")

        ctk.CTkLabel(self.left_frame, text= "Position", font=("Arial", 15)).grid(row = 5, column = 0, padx = (7, 0), pady = (12, 0), sticky = 'w')
        self.selected_role_option = ctk.CTkOptionMenu(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8, state=ctk.DISABLED)
        self.selected_role_option.grid(row = 6, column = 0, padx = (7, 0))
        self.selected_role_option.set("Job Position")

        '''ctk.CTkLabel(self.left_frame, text= "USN", font=("Arial", 15)).grid(row = 5, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.usn_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.usn_entry.grid(row = 6, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Password", font=("Arial", 15)).grid(row = 7, column = 0, padx = (7, 0), pady = (7, 0), sticky = 'w')
        self.pss_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.pss_entry.grid(row = 8, column = 0, padx = (7, 0))'''

        self.right_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.right_frame.pack(side = 'left', padx = (self._current_width * .0125, 0));
        self.right_frame.grid_propagate(0)
        ctk.CTkLabel(self.right_frame, text= "Access Level", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0))

        self.access_lvl_frame = ctk.CTkFrame(self.right_frame, self.right_frame._current_width * .91, self.right_frame._current_height * .91, fg_color='white')
        self.access_lvl_frame.grid(row = 1, column = 0, sticky = 'we', padx = 7, pady = 7)
        self.access_lvl_frame.grid_propagate(0)

        self.access_lvls: List[str] = ['Dashboard', 'Transaction', 'Services', 'Sales', 'Inventory', 'Pet Information', 'Report', 'Users', 'Action Log']
        self.check_boxes: Dict[str, ctk.CTkCheckBox] = {}
        for i in range(len(self.access_lvls)):
            self.check_boxes[self.access_lvls[i]] = ctk.CTkCheckBox(self.access_lvl_frame, self.access_lvl_frame._current_width * .95, 24,
                                                                    text=self.access_lvls[i], state=ctk.DISABLED);
            self.check_boxes[self.access_lvls[i]].grid(row = i, column = 0, padx = 7, pady = 7);
            

        self.accept_button = ctk.CTkButton(self, 140, 50, 12, text="Proceed")
        self.accept_button.pack(anchor = 'e', padx = (0, self._current_width * .025), pady = (self._current_width * .0125))



class frame(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.pack_propagate(0)

        self.upperframe = ctk.CTkFrame(self, self._current_width * .95, self._current_height * .85, 0, fg_color='transparent')
        self.upperframe.pack(padx = (self._current_width * .025, self._current_width * .025), pady = (self. _current_height * 0.025, 0))
        self.pack_propagate(0)

        self.left_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.left_frame.pack(side = 'left', padx = (0, self._current_width * .0125));
        self.left_frame.grid_propagate(0)
        ctk.CTkLabel(self.left_frame, text= "Account Credentials", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Full name", font=("Arial", 15)).grid(row = 1, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.name_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.name_entry.grid(row = 2, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Position", font=("Arial", 15)).grid(row = 3, column = 0, padx = (7, 0), pady = (12, 0), sticky = 'w')
        self.position_option = ctk.CTkOptionMenu(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8)
        self.position_option.grid(row = 4, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "USN", font=("Arial", 15)).grid(row = 5, column = 0, padx = (7, 0), pady = (24, 0), sticky = 'w')
        self.usn_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.usn_entry.grid(row = 6, column = 0, padx = (7, 0))

        ctk.CTkLabel(self.left_frame, text= "Password", font=("Arial", 15)).grid(row = 7, column = 0, padx = (7, 0), pady = (7, 0), sticky = 'w')
        self.pss_entry = ctk.CTkEntry(self.left_frame, self.left_frame._current_width * .95, self.left_frame._current_height * .075, 8,
                                      state = 'readonly')
        self.pss_entry.grid(row = 8, column = 0, padx = (7, 0))

        self.right_frame = ctk.CTkFrame(self.upperframe, self._current_width * .475, self._current_height * .85, 12, fg_color='transparent');
        self.right_frame.pack(side = 'left', padx = (self._current_width * .0125, 0));
        self.right_frame.grid_propagate(0)
        ctk.CTkLabel(self.right_frame, text= "Access Level", font=("Arial", 25)).grid(row = 0, column = 0, padx = (7, 0))

        self.access_lvl_frame = ctk.CTkFrame(self.right_frame, self.right_frame._current_width * .91, self.right_frame._current_height * .91, fg_color='white')
        self.access_lvl_frame.grid(row = 1, column = 0, sticky = 'we', padx = 7, pady = 7)
        self.access_lvl_frame.grid_propagate(0)

        self.access_lvls: List[str] = ['Dashboard', 'Transaction', 'Services', 'Sales', 'Inventory', 'Pet Information', 'Report', 'Users', 'Action Log']
        self.check_boxes: Dict[str, ctk.CTkCheckBox] = {}
        for i in range(len(self.access_lvls)):
            self.check_boxes[self.access_lvls[i]] = ctk.CTkCheckBox(self.access_lvl_frame, self.access_lvl_frame._current_width * .95, 24,
                                                                    text=self.access_lvls[i], state=ctk.DISABLED);
            self.check_boxes[self.access_lvls[i]].grid(row = i, column = 0, padx = 7, pady = 7);
            

        self.accept_button = ctk.CTkButton(self, 140, 50, 12, text="Proceed")
        self.accept_button.pack(anchor = 'e', padx = (0, self._current_width * .025), pady = (self._current_width * .0125))

class accounts_frame(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        width = self._current_width
        height = self._current_height       
         
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        
        self.search = ctk.CTkImage(light_image=Image.open("image/searchsmol.png"),size=(16,15))
        self.refresh_icon = ctk.CTkImage(light_image=Image.open("image/refresh.png"), size=(20,20))

        self.top_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.top_frame.grid(row=0, column=0, sticky="ew", padx=(width*0.005), pady=(height*0.01,0))
        
        self.search_frame = ctk.CTkFrame(self.top_frame,width=width*0.3, height = height*0.05, fg_color=Color.Platinum)
        self.search_frame.pack(side="left",padx=(0,width*0.005))
        self.search_frame.pack_propagate(0)
        ctk.CTkLabel(self.search_frame,text="Search", font=("DM Sans Medium", 14), text_color="grey", fg_color="transparent").pack(side="left", padx=(width*0.0075,width*0.005))
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Type here...", border_width=0, corner_radius=5, fg_color="white",placeholder_text_color="light grey", font=("DM Sans Medium", 14))
        self.search_entry.pack(side="left", padx=(0, width*0.0025), fill="x", expand=1)
        self.search_btn = ctk.CTkButton(self.search_frame, text="", image=self.search, fg_color="white", hover_color="light grey", width=width*0.005)
        self.search_btn.pack(side="left", padx=(0, width*0.0025))

        self.refresh_btn = ctk.CTkButton(self.top_frame,text="", width=width*0.025, height = height*0.05, image=self.refresh_icon, fg_color="#83BD75", hover_color='#74bc8a')
        self.refresh_btn.pack(side="left")
        
        """
        self.sort_search_frame = ctk.CTkFrame(self.top_frame, height = height*0.05, fg_color="light grey")
        self.sort_search_frame.grid(row=0, column=2,sticky="nw", padx=(width*0.005), pady=(height*0.01))
        self.sort_search_frame.pack_propagate(0)
        ctk.CTkLabel(self.sort_search_frame,text="All", font=("DM Sans Medium", 16), text_color="grey", fg_color="white", width=width*0.08).pack(side="left", padx=(width*0.0075,0))
        self.sort_search_btn = ctk.CTkButton(self.sort_search_frame, text="", fg_color="#0d578f", hover_color="#0d58c1",
                                        width=width*0.02)
        self.sort_search_btn.pack(side="left", padx=(0, 0)) """
        
        self.deactivate_acc_btn = ctk.CTkButton(self.top_frame, height = height*0.05, text="Deactivate Account",fg_color="#ff6464", font=("DM Sans Medium", 14), text_color="white",cursor='hand2')
        self.deactivate_acc_btn.pack(side='right')
        
        self.treeview_frame = ctk.CTkFrame(self, fg_color=Color.White_Platinum, corner_radius=0)
        self.treeview_frame.grid(row=1, column=0, sticky="nsew", padx=(width*0.005), pady=(height*0.01))

        self.account_treeview = cctk.cctkTreeView(self.treeview_frame, height= height*0.735, width=width*0.8025,
                                           column_format=f'/No:{int(width*.025)}-#r/Username:x-tl/FullName:{int(width*.3)}-tr/Role:{int(width*.175)}-tr!30!30',)
        self.account_treeview.pack()
        
        #/No:{int(width*.025)}-#r/PetID:{int(width*.075)}-tc/PetName:x-tl/OwnerName:{int(width*.225)}-tl/ContactNo:{int(width*.165)}-tr/Action:{int(width*.075)}-bD!30!30'

class creation_frame(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        width = self._current_width
        height = self._current_height       
         
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.camera_icon = ctk.CTkImage(light_image=Image.open("image/camera.png"), size=(24,24))
        self.pet_sample_icon = ctk.CTkImage(light_image=Image.open("image/user_icon.png"),size=(150,150)) 
        
        self.top_frame = ctk.CTkFrame(self, fg_color=Color.White_Platinum)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nsw", padx=(width*0.005), pady=(height*0.01))

        self.title_label = ctk.CTkLabel(self.top_frame,text="ACCOUNT CREATION", font=("DM Sans Medium", 14), text_color=Color.Blue_Maastricht, fg_color=Color.White_Lotion , corner_radius=5, width=width*0.15)
        self.title_label.pack(side="left" , padx=(width*0.0025), pady=(height*0.005))

        self.credentials_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.credentials_frame.grid(row=1, column=0, sticky="nsew", padx=(width*0.005,0), pady=(0,height*0.01))
        self.credentials_frame.grid_columnconfigure(1, weight=1)
        self.credentials_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(self.credentials_frame, text= "Credentials", font=("DM Sans Medium", 14), fg_color=Color.White_Platinum, text_color=Color.Blue_Maastricht, width=width*0.1, height=height*0.05, anchor='w', padx=(width*0.025)).grid(row = 0, column = 0, sticky='w')
        self.credential_content_frame = ctk.CTkFrame(self.credentials_frame, fg_color=Color.White_Platinum, corner_radius=0)
        self.credential_content_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
        self.con_sub_frame = ctk.CTkFrame(self.credential_content_frame, fg_color=Color.White_Lotion)
        self.con_sub_frame.pack(fill="both", expand=1, padx=(width*0.005), pady=(height*0.01))
        self.con_sub_frame.grid_columnconfigure(1, weight=1)
        '''PICTURE FRAME'''
        self.picture_frame = ctk.CTkFrame(self.con_sub_frame, fg_color=Color.White_Platinum, width=width*0.135, height=height*0.235)
        self.picture_frame.grid(row=0, column=0, sticky="w", padx=(width*0.005),  pady=(height*0.01))
        self.picture_frame.pack_propagate(0)
        self.acc_pic = ctk.CTkLabel(self.picture_frame, text='', corner_radius=5, image=self.pet_sample_icon)
        self.acc_pic.pack(fill="both",expan=1,padx=(width*0.005), pady=(height*0.01))
        
        self.camera_btn = ctk.CTkButton(self.con_sub_frame,text="", width=width*0.025, height = height*0.05, image=self.camera_icon, fg_color="#83BD75", hover_color='#74bc8a')
        self.camera_btn.grid(row=0, column=1, sticky="sw",  pady=(height*0.01))

        '''FULL NAME ENTRY'''
        self.fullname_frame = ctk.CTkFrame(self.con_sub_frame, fg_color=Color.White_Platinum)
        self.fullname_frame.grid(row=1, column=0, sticky="nsew", columnspan=2, padx=(width*0.005),  pady=(0,height*0.01))
        ctk.CTkLabel(self.fullname_frame, text='Full Name: ', font=("DM Sans Medium", 14), anchor='e', corner_radius=5, width=width*0.075, text_color=Color.Blue_Maastricht).pack(side="left", padx=(width*0.005,0),  pady=(height*0.01))
        self.fullname_entry = ctk.CTkEntry(self.fullname_frame, border_width=0, placeholder_text="Type Here...", placeholder_text_color="light grey", height=height*0.045 ,font=("DM Sans Medium", 14), fg_color=Color.White_Lotion, border_color=Color.Blue_Maastricht)
        self.fullname_entry.pack(side="left", fill="x", expand=1, padx=(0,width*0.005),  pady=(height*0.01))

        '''POSITION ENTRY'''
        self.position_frame = ctk.CTkFrame(self.con_sub_frame, fg_color=Color.White_Platinum)
        self.position_frame.grid(row=2, column=0,  sticky="nsew", columnspan=2, padx=(width*0.005),  pady=(0,height*0.01))
        ctk.CTkLabel(self.position_frame, text='Position: ', font=("DM Sans Medium", 14), anchor='e', corner_radius=5, width=width*0.075, text_color=Color.Blue_Maastricht).pack(side="left", padx=(width*0.005,0),  pady=(height*0.01))
        self.position_entry = ctk.CTkEntry(self.position_frame, border_width=0, placeholder_text="Type Here...", placeholder_text_color="light grey", height=height*0.045 ,font=("DM Sans Medium", 14), fg_color=Color.White_Lotion, border_color=Color.Blue_Maastricht)
        self.position_entry.pack(side="left", fill="x", expand=1, padx=(0,width*0.005),  pady=(height*0.01))

        '''USERNAME ENTRY'''
        self.username_frame = ctk.CTkFrame(self.con_sub_frame, fg_color=Color.White_Platinum)
        self.username_frame.grid(row=3, column=0, sticky="nsew", columnspan=2, padx=(width*0.005),  pady=(height*0.025,height*0.01))
        ctk.CTkLabel(self.username_frame, text='Username: ', font=("DM Sans Medium", 14), anchor='e', corner_radius=5, width=width*0.075, text_color=Color.Blue_Maastricht).pack(side="left", padx=(width*0.005,0),  pady=(height*0.01))
        self.username_entry = ctk.CTkEntry(self.username_frame,  border_width=0, placeholder_text="Type Here...", placeholder_text_color="light grey", height=height*0.045 ,font=("DM Sans Medium", 14), fg_color=Color.White_Lotion, border_color=Color.Blue_Maastricht)
        self.username_entry.pack(side="left", fill="x", expand=1, padx=(0,width*0.005),  pady=(height*0.01))

        '''PASSWORD ENTRY'''
        self.password_frame = ctk.CTkFrame(self.con_sub_frame, fg_color=Color.White_Platinum)
        self.password_frame.grid(row=4, column=0, sticky="nsew", columnspan=2, padx=(width*0.005),  pady=(0, height*0.01))
        ctk.CTkLabel(self.password_frame, text='Password: ', font=("DM Sans Medium", 14), anchor='e', corner_radius=5, width=width*0.075, text_color=Color.Blue_Maastricht).pack(side="left", padx=(width*0.005,0),  pady=(height*0.01))
        self.password_entry = ctk.CTkEntry(self.password_frame, border_width=0, placeholder_text="Type Here...", placeholder_text_color="light grey", height=height*0.045 ,font=("DM Sans Medium", 14), fg_color=Color.White_Lotion, border_color=Color.Blue_Maastricht)
        self.password_entry.pack(side="left", fill="x", expand=1, padx=(0,width*0.005),  pady=(height*0.01))
        

        self.access_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.access_frame.grid(row=1, column=1, sticky="nsew", padx=(width*0.005), pady=(0,height*0.01))
        self.access_frame.grid_columnconfigure(1, weight=1)
        self.access_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(self.access_frame, text= "Access Level", font=("DM Sans Medium", 14), fg_color=Color.White_Platinum, text_color=Color.Blue_Maastricht, width=width*0.1, height=height*0.05, anchor='w', padx=(width*0.025)).grid(row = 0, column = 0, sticky='w')
        self.access_content_frame = ctk.CTkFrame(self.access_frame, fg_color=Color.White_Platinum, corner_radius=0)
        self.access_content_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.access_lvl_frame = ctk.CTkFrame(self.access_content_frame, fg_color=Color.White_Lotion)
        self.access_lvl_frame.pack(fill="both", expand=1, padx=(width*0.005), pady=(height*0.01))
        
        '''CHECKLIST'''
        self.access_lvls: List[str] = ['Dashboard', 'Transaction', 'Services', 'Sales', 'Inventory', 'Pet Information', 'Report', 'Users', 'Action Log']
        self.check_boxes: Dict[str, ctk.CTkCheckBox] = {}
        for i in range(len(self.access_lvls)):
            self.check_boxes[self.access_lvls[i]] = ctk.CTkCheckBox(self.access_lvl_frame, self.access_lvl_frame._current_width * .95, 24, text=self.access_lvls[i], state=ctk.DISABLED, font=("DM Sans Medium", 14));
            self.check_boxes[self.access_lvls[i]].grid(row = i, column = 0, padx=(width*0.0075), pady = (height*0.01));
            
        '''BOTTOM'''
        self.bottom_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.bottom_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=(width*0.005), pady=(0,height*0.01))
        
        self.create_acc_btn = ctk.CTkButton(self.bottom_frame, height = height*0.05, text="Create Account", font=("DM Sans Medium", 14))
        self.create_acc_btn.pack(side='right')

#roles tab
class roles_frame(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        width = self._current_width
        height = self._current_height       
         
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.pet_sample_icon = ctk.CTkImage(light_image=Image.open("image/user_icon.png"),size=(150,150))

        self.account_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.account_frame.grid(row=0, column=0, sticky="nsew", padx=(width*0.005,0), pady=(height*0.01))
        self.account_frame.grid_columnconfigure(0, weight=1)
        self.account_frame.grid_rowconfigure(1, weight=1)
        
        self.left_title_frame = ctk.CTkFrame(self.account_frame, fg_color=Color.White_Platinum, corner_radius=0, width=width*0.265, height=height*0.065,)
        self.left_title_frame.grid(row = 0, column = 0, sticky='nsw')
        self.left_title_frame.pack_propagate(0)
        
        '''USER OPTION'''
        self.usn_option = ctk.CTkOptionMenu(self.left_title_frame, width=width*0.25, height=height*0.045, corner_radius=5, fg_color=Color.White_Lotion, button_color=Color.Blue_Tufts, 
                                            button_hover_color=Color.Blue_Yale, text_color=Color.Blue_Maastricht, font=('DM Sans Medium', 14), dropdown_font=('DM Sans Medium', 12))
        self.usn_option.pack(side="left", fill="x", expand=1, padx=(width*0.005), pady=(height*0.01))
        self.usn_option.set("Select a user")
        
        self.left_sub_frame = ctk.CTkFrame(self.account_frame, fg_color=Color.White_Platinum, corner_radius=0)
        self.left_sub_frame.grid(row = 1, column = 0, sticky='nsew')
        
        self.left_inner_frame = ctk.CTkFrame(self.left_sub_frame, fg_color=Color.White_Lotion)
        self.left_inner_frame.pack(fill="both", expand=1, padx=(width*0.005), pady=(height*0.01))
        self.left_inner_frame.grid_columnconfigure(0, weight=1)
        
        '''PICTURE FRAME'''
        self.picture_frame = ctk.CTkFrame(self.left_inner_frame, fg_color=Color.White_Platinum, width=width*0.135, height=height*0.235)
        self.picture_frame.grid(row=0, column=0, sticky="w", padx=(width*0.005),  pady=(height*0.01))
        self.picture_frame.pack_propagate(0)
        self.acc_pic = ctk.CTkLabel(self.picture_frame, text='', corner_radius=5, image=self.pet_sample_icon)
        self.acc_pic.pack(fill="both",expan=1,padx=(width*0.005), pady=(height*0.01))
       
        '''FULL NAME ENTRY'''
        self.fullname_frame = ctk.CTkFrame(self.left_inner_frame, fg_color=Color.White_Platinum)
        self.fullname_frame.grid(row=1, column=0, sticky="nsew", padx=(width*0.005),  pady=(0,height*0.01))
        ctk.CTkLabel(self.fullname_frame, text='Full Name: ', font=("DM Sans Medium", 14), anchor='e', corner_radius=5, width=width*0.075, text_color=Color.Blue_Maastricht).pack(side="left", padx=(width*0.005,0),  pady=(height*0.01))
        self.fullname_entry = ctk.CTkEntry(self.fullname_frame, border_width=0, placeholder_text="Type Here...", placeholder_text_color="light grey", height=height*0.045 ,font=("DM Sans Medium", 14), fg_color=Color.White_Lotion, border_color=Color.Blue_Maastricht)
        self.fullname_entry.pack(side="left", fill="x", expand=1, padx=(0,width*0.005),  pady=(height*0.01))

        '''POSITION ENTRY'''
        self.position_frame = ctk.CTkFrame(self.left_inner_frame, fg_color=Color.White_Platinum)
        self.position_frame.grid(row=2, column=0,  sticky="nsew", padx=(width*0.005),  pady=(0,height*0.01))
        ctk.CTkLabel(self.position_frame, text='Position: ', font=("DM Sans Medium", 14), anchor='e', corner_radius=5, width=width*0.075, text_color=Color.Blue_Maastricht).pack(side="left", padx=(width*0.005,0),  pady=(height*0.01))
        self.position_entry = ctk.CTkEntry(self.position_frame, border_width=0, placeholder_text="Type Here...", placeholder_text_color="light grey", height=height*0.045 ,font=("DM Sans Medium", 14), fg_color=Color.White_Lotion, border_color=Color.Blue_Maastricht)
        self.position_entry.pack(side="left", fill="x", expand=1, padx=(0,width*0.005),  pady=(height*0.01))

        self.access_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.access_frame.grid(row=0, column=1, sticky="nsew", padx=(width*0.005), pady=(height*0.01))
        self.access_frame.grid_columnconfigure(1, weight=1)
        self.access_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(self.access_frame, text= "Access Level", font=("DM Sans Medium", 14), fg_color=Color.White_Platinum, text_color=Color.Blue_Maastricht, width=width*0.1, height=height*0.05, anchor='w', padx=(width*0.025)).grid(row = 0, column = 0, sticky='w')
        self.access_content_frame = ctk.CTkFrame(self.access_frame, fg_color=Color.White_Platinum, corner_radius=0)
        self.access_content_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.access_lvl_frame = ctk.CTkFrame(self.access_content_frame, fg_color=Color.White_Lotion)
        self.access_lvl_frame.pack(fill="both", expand=1, padx=(width*0.005), pady=(height*0.01))
        
        '''CHECKLIST'''
        self.access_lvls: List[str] = ['Dashboard', 'Transaction', 'Services', 'Sales', 'Inventory', 'Pet Information', 'Report', 'Users', 'Action Log']
        self.check_boxes: Dict[str, ctk.CTkCheckBox] = {}
        for i in range(len(self.access_lvls)):
            self.check_boxes[self.access_lvls[i]] = ctk.CTkCheckBox(self.access_lvl_frame, self.access_lvl_frame._current_width * .95, 24, text=self.access_lvls[i], state=ctk.DISABLED, font=("DM Sans Medium", 14));
            self.check_boxes[self.access_lvls[i]].grid(row = i, column = 0, padx=(width*0.0075), pady = (height*0.01))
             
        self.bottom_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.bottom_frame.grid(row=1, column=0, sticky="nsew", columnspan=2, padx=(width*0.005), pady=(0,height*0.01))
        
        self.update_acc_btn =  ctk.CTkButton(self.bottom_frame, height = height*0.05, text="Update Account", font=("DM Sans Medium", 14))
        self.update_acc_btn.pack(side='right')
        

class deactivated_frame(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.search = ctk.CTkImage(light_image=Image.open("image/searchsmol.png"),size=(16,15))
        self.refresh_icon = ctk.CTkImage(light_image=Image.open("image/refresh.png"), size=(20,20))

        self.top_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=(width*0.005), pady=(height*0.01))

        self.search_frame = ctk.CTkFrame(self.top_frame,width=width*0.3, height = height*0.05, fg_color=Color.Platinum)
        self.search_frame.pack(side="left",padx=(0,width*0.005))
        self.search_frame.pack_propagate(0)
        ctk.CTkLabel(self.search_frame,text="Search", font=("DM Sans Medium", 14), text_color="grey", fg_color="transparent").pack(side="left", padx=(width*0.0075,width*0.005))
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Type here...", border_width=0, corner_radius=5, fg_color="white",placeholder_text_color="light grey", font=("DM Sans Medium", 14))
        self.search_entry.pack(side="left", padx=(0, width*0.0025), fill="x", expand=1)
        self.search_btn = ctk.CTkButton(self.search_frame, text="", image=self.search, fg_color="white", hover_color="light grey", width=width*0.005)
        self.search_btn.pack(side="left", padx=(0, width*0.0025))

        self.refresh_btn = ctk.CTkButton(self.top_frame,text="", width=width*0.025, height = height*0.05, image=self.refresh_icon, fg_color="#83BD75", hover_color='#74bc8a')
        self.refresh_btn.pack(side="left", padx=(0, width*0.005))
        #reactivate button
        self.reactivate_acc_btn = ctk.CTkButton(self.top_frame, width=width*0.08, height = height*0.05, text="Reactivate Account", font=("DM Sans Medium", 14))
        self.reactivate_acc_btn.pack(side="left", padx=(0, width*0.005))

        self.treeview_frame = ctk.CTkFrame(self, fg_color=Color.White_Platinum, corner_radius=0)
        self.treeview_frame.grid(row=1, column=0, sticky="nsew", padx=(width*0.005), pady=(0,height*0.01))

        self.account_treeview = cctk.cctkTreeView(self.treeview_frame, height= height*0.735, width=width*0.8025,
                                           column_format=f'/No:{int(width*.025)}-#r/Username:x-tl/Role:{int(width*.175)}-tr/Reason:{int(width*.3)}-tr!30!30',)
        self.account_treeview.pack()