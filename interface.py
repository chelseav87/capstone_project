import tkinter as tk
from tkinter import ttk
from formulas import *

WIDTH = 500
HEIGHT = 500

# --- GUI Setup --- #
root = tk.Tk()
root.title("Financial Calculator")
root.geometry("500x500")
root.resizable(width=False, height=False)
style = ttk.Style(root)

tk.Label(root, text=f"Financial Calculator", font=("Helvetica", 12, "bold")).pack(pady=5)

# --- Notebook Tabs --- #
notebook = ttk.Notebook(root, style='lefttab.TNotebook')
style.configure("lefttab.TNotebook", tabposition="wn")

def create_tabs(width, height):
    tab_text = {
        "Fundamental Equations": "fe",
        "Income Statement": "is",
        "Balance Sheet": "bs",
        "Cash Flow": "cf",
        "Profitability Ratios": "pr",
        "Liquidity Ratios": "lr",
        "Solvency Ratios": "sr",
        "Efficiency Ratios": "er",
        "Depreciation Methods": "dm"
    }

    tab_labels = {}
    for key, value in tab_text.items():
        frame = ttk.Frame(notebook, width=width, height=height)
        notebook.add(frame, text=key)
        tab_labels[key] = frame

    return tab_labels

tabs = create_tabs(WIDTH, HEIGHT)

notebook.pack()

root.mainloop()