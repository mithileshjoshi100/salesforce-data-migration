### -ACCENTURE CONFIDENTIAL-
### Type: Source Code
###
### Copyright (c) 2023, ACCENTURE
### All Rights Reserved.
###
### This unpublished material is proprietary to ACCENTURE. The methods and
### techniques described herein are considered trade secrets and/or
### confidential. Reproduction or distribution, in whole or in part, is
### forbidden except by express written permission of ACCENTURE.


import customtkinter
from tkinter import filedialog, Tk
import os
from pathlib import Path
import app.gui.magic_strings as ms
import app.gui.call_api as call_api

def main():
    def execute_script():
        option1 = script_menu.get()
        option2 = object_menu.get()
        call_api._call(option1,option2)


    def show_log_folder():
        root = Tk()
        root.withdraw()
        print(os.path.dirname(__file__))
        logs_path = Path(os.path.dirname(__file__)).parent.parent
        logs_path = os.path.join(logs_path,'logs')
        print(logs_path)
        root.filename = filedialog.askopenfilename(
            initialdir=logs_path, title="You Logs files are hear",
            filetypes=[("Text Files", "*.log")])
        print(root.filename)
        print('open logs')


    def show_files_folder():
        root = Tk()
        root.withdraw()
        print(os.path.dirname(__file__))
        files_path = Path(os.path.dirname(__file__)).parent.parent
        files_path = os.path.join(files_path,'data')
        root.filename = filedialog.askopenfilename(
            initialdir=files_path, title="You Data files are hear",
            filetypes=[("Text Files", "*.csv")])
        print(root.filename)
        print('open logs')
        print('show files')


    def script_menu_callback(choice):
        if choice == ms.script_options[1]:
            print('changed to a')
            object_menu.configure(values=ms.extraction_objects)
            
        if choice == ms.script_options[2]:
            print('changed to b')
            object_menu.configure(values=ms.insertion_objects)
            

        
    APP_NAME = ms.APP_NAME
    customtkinter.set_default_color_theme(ms.THEME)
    customtkinter.set_appearance_mode(ms.MODE)

    app = customtkinter.CTk()
    app.geometry(ms.DEFAULT_SIZE)
    app.grid_rowconfigure(( 1), weight=1)
    app.grid_columnconfigure((0), weight=1)

    title_frame = customtkinter.CTkFrame(app, width=800, height=100)
    title_frame.grid(
        row=0, column=0, padx=10, pady=10,columnspan=2, sticky="nsew")

    title_textbox = customtkinter.CTkLabel(
        title_frame, text=APP_NAME, font=(ms.FONT_NAME, 50))
    title_textbox.place(relx=0.5, rely=0.5, anchor="center")

    left_frame = customtkinter.CTkFrame(app, width=200, height=500)
    left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    
    for i,val in enumerate(ms.text_lst):
        text_ = customtkinter.CTkLabel(
        left_frame, text=f"{i}. {val}\n", font=(ms.FONT_NAME, 16),
        justify='left'
        )
        text_.grid(row=i,column=0,sticky="w")

    home_frame = customtkinter.CTkFrame(app, width=400, height=500)
    home_frame.grid(row=1, column=1,padx=10, pady=10, sticky="nsew")

    home_frame.grid_rowconfigure((0, 1), weight=1)
    home_frame.grid_columnconfigure(0, weight=1)

    program_frame = customtkinter.CTkFrame(home_frame, width=400, height=200)
    program_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    program_frame.grid_rowconfigure(3, weight=1)
    program_frame.grid_columnconfigure(1, weight=1)

    script_menu_label = customtkinter.CTkLabel(
        program_frame, text=ms.SELECT_SCRIPT_LABEL, font=(ms.FONT_NAME, 16))
    script_menu_label.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="E")
    script_menu = customtkinter.CTkOptionMenu(
        program_frame, values=ms.script_options, command=script_menu_callback)
    script_menu.grid(
        row=1, column=1, padx=(10, 50), pady=(10, 10), sticky="nsew")

    object_menu_label = customtkinter.CTkLabel(
        program_frame, text=ms.SELECT_OBJECT_LABEL, font=("Consolas", 16))
    object_menu_label.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="E")
    object_menu = customtkinter.CTkOptionMenu(
        program_frame, values=ms.default_objects)
    object_menu.grid(
        row=2, column=1, padx=(10, 50), pady=(10, 10), sticky="nsew")

    execute_btn = customtkinter.CTkButton(
        program_frame, text=ms.RUN_SCRIPT_BTN, command=execute_script)
    execute_btn.grid(row=3, column=1, padx=10, pady=(10, 10), sticky="W")

    output_fream = customtkinter.CTkFrame(home_frame, width=400, height=100)
    output_fream.grid(row=1, column=0,padx=10, pady=10, sticky="nsew")

    show_btn_fream = customtkinter.CTkFrame(home_frame, width=400, height=10)
    show_btn_fream.grid(row=2, column=0, sticky="nsew")
    show_btn_fream.grid_columnconfigure((0, 1), weight=1)
    show_btn_fream.grid_rowconfigure(0, weight=1)

    b1 = customtkinter.CTkFrame(show_btn_fream, width=200, height=100)
    b1.grid(row=0, column=0, sticky="nsew")
    b2 = customtkinter.CTkFrame(show_btn_fream, width=200, height=100)
    b2.grid(row=0, column=1, sticky="nsew")

    show_logsbutton = customtkinter.CTkButton(
        b1, text=ms.SHOW_LOGS_BTN, command=show_log_folder)
    show_logsbutton.place(relx=0.5, rely=0.5, anchor="center")
    show_filesbutton = customtkinter.CTkButton(
        b2, text=ms.SHOW_FILES_BTN, command=show_files_folder)
    show_filesbutton.place(relx=0.5, rely=0.5, anchor="center")

    app.mainloop()



