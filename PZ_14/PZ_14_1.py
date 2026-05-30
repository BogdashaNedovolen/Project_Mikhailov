# 10 работа

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Contact Form")
root.geometry("400x500")
root.resizable(False, False)



frm_main = tk.Frame(root, bg="#e0e0e0", padx=20, pady=20)
frm_main.pack(fill=tk.BOTH, expand=True)



lbl_title = tk.Label(
    frm_main,
    text="Contact Form",
    font=("Arial", 18, "bold"),
    bg="#e0e0e0"
)
lbl_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))



lbl_subtitle = tk.Label(
    frm_main,
    text="Please fill all entries.",
    font=("Arial", 10),
    bg="#e0e0e0"
)
lbl_subtitle.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))



sep = tk.Frame(frm_main, bg="white", height=1)
sep.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 15))



lbl_name = tk.Label(frm_main, text="Name:", font=("Arial", 11), bg="#e0e0e0")
lbl_name.grid(row=3, column=0, sticky="w", pady=5)

ent_name = ttk.Entry(frm_main, width=35, font=("Arial", 11))
ent_name.grid(row=3, column=1, pady=5, padx=(5, 0))



lbl_email = tk.Label(frm_main, text="Email:", font=("Arial", 11), bg="#e0e0e0")
lbl_email.grid(row=4, column=0, sticky="w", pady=5)

ent_email = ttk.Entry(frm_main, width=35, font=("Arial", 11))
ent_email.grid(row=4, column=1, pady=5, padx=(5, 0))



lbl_message = tk.Label(frm_main, text="Message:", font=("Arial", 11), bg="#e0e0e0")
lbl_message.grid(row=5, column=0, sticky="nw", pady=5)

txt_message = tk.Text(
    frm_main,
    width=35,
    height=6,
    font=("Arial", 11),
    wrap=tk.WORD,
    bg="white"
)
txt_message.grid(row=5, column=1, pady=5, padx=(5, 0))



lbl_subject = tk.Label(frm_main, text="Subject:", font=("Arial", 11), bg="#e0e0e0")
lbl_subject.grid(row=6, column=0, sticky="w", pady=5)

subject_var = tk.StringVar(value="Product Inquiry")
cmb_subject = ttk.Combobox(
    frm_main,
    textvariable=subject_var,
    values=["Product Inquiry"],
    state="readonly",
    width=32,
    font=("Arial", 11)
)
cmb_subject.grid(row=6, column=1, pady=5, padx=(5, 0))



btn_send = ttk.Button(frm_main, text="Send", style="Send.TButton", width=15)
btn_send.grid(row=7, column=0, columnspan=2, pady=20)



style = ttk.Style()
style.configure(
    "Send.TButton",
    font=("Arial", 11, "bold"),
    padding=5
)

root.mainloop()
