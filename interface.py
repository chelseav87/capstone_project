import tkinter as tk
from tkinter import ttk
from formulas import *

WIDTH = 500
HEIGHT = 600

formula_classes = {
    "Fundamental Equations": FundamentalEquations,
    "Income Statement": IncomeStatement,
    "Balance Sheet": BalanceSheet,
    "Cash Flow": CashFlow,
    "Profitability Ratios": ProfitabilityRatios,
    "Liquidity Ratios": LiquidityRatios,
    "Solvency Ratios": SolvencyRatios,
    "Efficiency Ratios": EfficiencyRatios
}

depreciation_classes = {
    "Straight-Line": StraightLine,
    "Double-Declining Balance": DoubleDecliningBalance,
    "Units of Production": UnitsOfProduction
}

# Notebook Tab UI
def create_formula_tab(parent_tab, label, formula_group):
    frame = tk.Frame(parent_tab)
    tk.Label(frame, text=label, font=("Helvetica", 12, "bold")).pack(pady=10)
    variables = list(formula_group.variables.keys())

    # Variable to Solve
    tk.Label(frame, text="Solving for:").pack()
    selected_variable = tk.StringVar(value="...")
    options = ttk.OptionMenu(frame, selected_variable, "...", *variables)
    options.pack(pady=5)

    # Input Prompts
    input_row = tk.Frame(frame)
    input_row.pack(pady=15)

    inputted_values = {}

    for variable in variables:
        grid_row = tk.Frame(input_row)
        grid_row.pack(fill="x", pady=2)

        tk.Label(grid_row, text=variable, width=30, anchor="w").pack(side="left")

        entry_row = tk.Entry(grid_row)
        entry_row.pack(side="left", fill="x", expand=True)

        inputted_values[variable] = entry_row

    def calculate():
        target_variable = selected_variable.get()
        values = {}

        for variable_value, entry in inputted_values.items():
            if variable_value == target_variable:
                continue

            text = entry.get().strip()
            if text == "":
                continue

            try:
                values[variable_value] = float(text)
            except ValueError:
                result_label.config(text="Invalid input.")
                return

        try:
            formula = formula_group(**values)
            result = formula.solve(target_variable)
            result_label.config(text=f"{target_variable} = {result:.02f}")
        except:
            result_label.config(text="Insufficient information given.")

    tk.Button(frame, text="Solve", command=calculate).pack(pady=10)

    result_label = tk.Label(frame, text="", font=("Helvetica", 8))
    result_label.pack(pady=10)

    return frame

def create_depreciation_tab(parent_tab):
    frame = tk.Frame(parent_tab)
    tk.Label(frame, text="Depreciation Methods", font=("Helvetica", 12, "bold")).pack(pady=10)
    variables = list(depreciation_classes.keys())

    # Method to Solve
    tk.Label(frame, text="Choose method:").pack()
    selected_method = tk.StringVar(value=variables[0])
    depreciation_methods = depreciation_classes[selected_method.get()]
    options = ttk.OptionMenu(frame, selected_method, "...", *variables)
    options.pack(pady=5)

    # Input Prompts
    input_row = tk.Frame(frame)
    input_row.pack(pady=15)

    inputted_values = {}

    for variable in depreciation_methods.variables.keys():
        grid_row = tk.Frame(input_row)
        grid_row.pack(fill="x", pady=2)

        tk.Label(grid_row, text=variable, width=30, anchor="w").pack(side="left")

        entry_row = tk.Entry(grid_row)
        entry_row.pack(side="left", fill="x", expand=True)

        inputted_values[variable] = entry_row

    def calculate():
        values = {}

        for variable_value, entry in inputted_values.items():
            text = entry.get().strip()
            if text == "":
                result_label.config(text="Insufficient information given.")
                return
            try:
                values[variable_value] = float(text)
            except ValueError:
                result_label.config(text="Invalid input.")
                return

        try:
            if "Year End" in values:
                result = depreciation_methods.depreciation_expense(values["Year End"])
            elif "Units Produced" in values:
                result = depreciation_methods.depreciation_expense(values["Units Produced"])
            else:
                result = depreciation_methods.depreciation_expense()

            result_label.config(text=f"Depreciation Expense = {result:.02f}")
        except:
            result_label.config(text="Insufficient information given.")

    tk.Button(frame, text="Calculate", command=calculate).pack(pady=10)

    result_label = tk.Label(frame, text="", font=("Helvetica", 8))
    result_label.pack(pady=10)

    return frame

# --- GUI Setup --- #
root = tk.Tk()
root.title("Financial Calculator")
root.geometry("500x600")
root.resizable(width=False, height=False)
style = ttk.Style(root)
notebook = ttk.Notebook(root, style='lefttab.TNotebook')
style.configure("lefttab.TNotebook", tabposition="wn")
notebook.pack(fill="both", expand=True)

tab_labels = {}
for tab_name, formula_class in formula_classes.items():
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)
    create_formula_tab(tab, tab_name, formula_class).pack(fill="both", expand=True)

tab_dm = ttk.Frame(notebook)
notebook.add(tab_dm, text="Depreciation Methods")
create_depreciation_tab(tab_dm).pack(fill="both", expand=True)

root.mainloop()