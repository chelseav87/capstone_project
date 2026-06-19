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
    selected_variable = tk.StringVar(value=variables[0])
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
        if target_variable == "...":
            result_label.config(text="Please select a variable to solve for.")
            return

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
        except IndexError:
            result_label.config(text="Insufficient information given.")

    tk.Button(frame, text="Solve", command=calculate).pack(pady=10)

    result_label = tk.Label(frame, text="", font=("Helvetica", 8))
    result_label.pack(pady=10)

    return frame


def create_depreciation_tab(parent_tab):
    frame = tk.Frame(parent_tab)
    tk.Label(frame, text="Depreciation Methods", font=("Helvetica", 12, "bold")).pack(pady=10)
    methods = list(depreciation_classes.keys())

    # Method to Solve
    tk.Label(frame, text="Choose method:").pack()
    selected_method = tk.StringVar(value=methods[0])
    options = ttk.OptionMenu(frame, selected_method, "...", *methods)
    options.pack(pady=5)

    # Input Prompts
    input_row = tk.Frame(frame)
    input_row.pack(pady=15)

    inputted_values = {}

    variable_names = {
        "Asset Cost": "asset_cost",
        "Salvage Value": "salvage_value",
        "Useful Life": "useful_life",
        "Year End": "year_end",
        "Total Units": "total_units",
        "Units Produced": "units_produced"
    }

    for variable in variable_names.keys():
        grid_row = tk.Frame(input_row)
        grid_row.pack(fill="x", pady=2)

        tk.Label(grid_row, text=variable, width=30, anchor="w").pack(side="left")

        entry_row = tk.Entry(grid_row)
        entry_row.pack(side="left", fill="x", expand=True)

        inputted_values[variable] = entry_row

    def calculate():
        method_name = selected_method.get()
        if method_name == "...":
            result_label.config(text="Please select a depreciation method.")
            return
        method_class = depreciation_classes[method_name]

        values = {}
        for variable_value in variable_names:
            text = inputted_values[variable_value].get().strip()
            if text == "":
                continue
            try:
                values[variable_names[variable_value]] = float(text)
            except ValueError:
                result_label.config(text="Invalid input.")
                return

        try:
            result = None

            # Instantiate Method
            initialize_parameters = method_class.__init__.__code__.co_varnames
            initialize_values = {key: value for key, value in values.items() if key in initialize_parameters}

            method = method_class(**initialize_values)

            # Solve
            if method_name == "Straight-Line":
                result = method.depreciation_expense()
            elif method_name == "Double-Declining Balance":
                result = method.depreciation_expense(int(values["year_end"]))
            elif method_name == "Units of Production":
                result = method.depreciation_expense(values["units_produced"])

            result_label.config(text=f"Depreciation Expense = {result:.02f}")
        except TypeError:
            result_label.config(text="Insufficient information given.")
        except ZeroDivisionError:
            result_label.config(text="Cannot divide by zero.")


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