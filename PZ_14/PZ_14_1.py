#10 работа
# https://www.formget.com/wp-content/uploads/2014/06/style1.png

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Contact Form")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#e0e0e0")


tk.Label(root, text="Contact Form", font=("Arial", 18, "bold"), bg="#e0e0e0").pack(padx=40, pady=(20, 0), anchor="w")
tk.Label(root, text="Please fill all entries.", font=("Arial", 10), bg="#e0e0e0").pack(padx=40, pady=(0, 5), anchor="w")


tk.Frame(root, bg="white", height=1).pack(fill=tk.X, padx=40, pady=(0, 15))


frame_name = tk.Frame(root, bg="#e0e0e0")
frame_name.pack(fill=tk.X, padx=40, pady=10)
tk.Label(frame_name, text="Name:", font=("Arial", 11, 'bold'), bg="#e0e0e0").pack(side=tk.LEFT)
ttk.Entry(frame_name, width=26, font=("Arial", 11)).pack(side=tk.RIGHT, padx=(10, 0))


frame_email = tk.Frame(root, bg="#e0e0e0")
frame_email.pack(fill=tk.X, padx=40, pady=10)
tk.Label(frame_email, text="Email:", font=("Arial", 11, 'bold'), bg="#e0e0e0").pack(side=tk.LEFT)
ttk.Entry(frame_email, width=26, font=("Arial", 11)).pack(side=tk.RIGHT, padx=(10, 0))


frame_message = tk.Frame(root, bg="#e0e0e0")
frame_message.pack(fill=tk.X, padx=(30,40), pady=10)
tk.Label(frame_message, text="Message:", font=("Arial", 11, 'bold'), bg="#e0e0e0").pack(side=tk.LEFT)
tk.Text(frame_message, width=26, height=6, font=("Arial", 11), wrap=tk.WORD, bg="white").pack(side=tk.RIGHT, padx=(10, 0))


frame_subject = tk.Frame(root, bg="#e0e0e0")
frame_subject.pack(fill=tk.X, padx=40, pady=10)
tk.Label(frame_subject, text="Subject:", font=("Arial", 11, 'bold'), bg="#e0e0e0").pack(side=tk.LEFT)
ttk.Combobox(frame_subject, values=["Product Inquiry"], state="readonly", width=24, font=("Arial", 11)).pack(side=tk.RIGHT, padx=(10, 0))


style = ttk.Style()
style.configure("Send.TButton", font=("Arial", 11, "bold"), padding=5)
ttk.Button(root, text="Send", style="Send.TButton", width=15).pack(pady=20)

root.mainloop()
