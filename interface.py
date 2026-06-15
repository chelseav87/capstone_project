import tkinter as tk
from tkinter import ttk
from formulas import *

WIDTH = 500
HEIGHT = 500

formula_classes = {
    "Fundamental Equations": FundamentalEquations,
    "Income Statement Formulas": IncomeStatement,
    "Balance Sheet Formulas": BalanceSheet,
    "Cash Flow Formulas": CashFlow,
    "Profitability Ratios": ProfitabilityRatios,
    "Liquidity Ratios": LiquidityRatios,
    "Solvency Ratios": SolvencyRatios,
    "Efficiency Ratios": EfficiencyRatios,
    "Depreciation Methods": None # temp; just different class structure
}

def create_formula_tab(parent_tab, label, formula_group):
    frame = tk.Frame(parent_tab)
    tk.Label(frame, text=label, font=("Helvetica", 12, "bold")).pack(pady=10)

    # Variable to Solve Prompt
    tk.Label(frame, text="Solving for:").pack()
    selected_variable = tk.StringVar(value="...")
    options = ttk.OptionMenu(frame, selected_variable, "...", *list(formula_group.variables.keys()))
    options.pack(pady=5)

    return frame

# --- GUI Setup --- #
root = tk.Tk()
root.title("Financial Calculator")
root.geometry("500x500")
root.resizable(width=False, height=False)
style = ttk.Style(root)
notebook = ttk.Notebook(root, style='lefttab.TNotebook')
style.configure("lefttab.TNotebook", tabposition="wn")
notebook.pack(fill="both", expand=True)

tab_labels = {}
for tab_name, formula_class in formula_classes.items():
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)

    # temp for depreciation methods
    if formula_class is not None:
        create_formula_tab(tab, tab_name, formula_class).pack(fill="both", expand=True)
    else:
        print("depreciation methods here")

root.mainloop()