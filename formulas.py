from sympy import *

# --- Base Classes --- #
class FormulaModel:
    variables = {}
    equations = []

    def __init__(self, **kwargs):
        self.values = kwargs

    def solve(self, target):
        to_solve = self.variables[target]

        # Substitution mapping
        known_values = {self.variables[key]: value for key, value in self.values.items()}

        # Filtering valid equation, if any
        relevant_equations = []
        for equation in self.equations:
            if to_solve in equation.free_symbols:
                invalid_variables = equation.free_symbols - {to_solve}
                if all(variable in known_values for variable in invalid_variables):
                    relevant_equations.append(equation)

        if not relevant_equations:
            return ValueError("Insufficient information given.")

        # Substituting all given values into given equation
        known_values = [equation.subs(known_values) for equation in relevant_equations]

        # Calculation
        solution = solve(known_values[0], to_solve)

        # User-input error handling
        if not solution: # check if no solution
            return ValueError("Insufficient information given.")
        if isinstance(solution, list): # check list output
            solution = solution[0]
        if isinstance(solution, dict): # check dictionary output
            solution = solution[to_solve]
        if hasattr(solution, "free_symbols") and solution.free_symbols: # check symbolic output
            return ValueError("Insufficient information given or desired variable is already known.")

        return solution


class DepreciationMethods:
    def __init__(self, asset_cost, salvage_value, useful_life):
        self.asset_cost = asset_cost
        self.salvage_value = salvage_value
        self.useful_life = useful_life

    def depreciation_expense(self):
        return None


# --- Derived Classes --- #
class FundamentalEquations(FormulaModel):
    variables = {
        "assets": symbols("assets"),
        "liabilities": symbols("liabilities"),
        "equity": symbols("equity"),
        "common_stock": symbols("common_stock"),
        "dividends": symbols("dividends"),
        "revenues": symbols("revenues"),
        "expenses": symbols("expenses")
    }
    equations = [
        Eq(variables["assets"], variables["liabilities"] + variables["equity"]),
        Eq(variables["equity"], variables["common_stock"] + variables["revenues"] - variables["expenses"]- variables["dividends"])
    ]

# creating an object instance test, to be deleted once GUI is completed
test = FundamentalEquations(assets=10000,liabilities=9000,common_stock=10000, revenues=10000, expenses=1000, dividends=100)
print(test.solve("equity"))


class IncomeStatement(FormulaModel):
    def net_sales(self):
        return None

    def cost_of_goods_sold(self):
        return None

    def gross_profit(self):
        return None

    def operating_income(self):
        return None

    def net_income(self):
        return None


class BalanceSheet(FormulaModel):
    def working_capital(self):
        return None

    def asset_book_value(self):
        return None

    def total_equity(self):
        return None


class CashFlow(FormulaModel):
    def free_cash_flow(self):
        return None

    def cash_conversion_cycle(self):
        return None


class ProfitabilityRatios(FormulaModel):
    def profit_margin(self):
        return None

    def gross_margin(self):
        return None

    def return_on_assets(self):
        return None

    def return_on_equity(self):
        return None

    def earnings_per_share(self):
        return None

    def price_to_earnings(self):
        return None


class LiquidityRatios(FormulaModel):
    def current(self):
        return None

    def quick(self):
        return None

    def cash(self):
        return None


class SolvencyRatios(FormulaModel):
    def debt(self):
        return None

    def debt_to_equity(self):
        return None

    def times_interest_earned(self):
        return None

    def equity_multiplier(self):
        return None


class EfficiencyRatios(FormulaModel):
    def inventory_turnover(self):
        return None

    def accounts_receivable_turnover(self):
        return None

    def accounts_payable_turnover(self):
        return None

    def days_sales_in_inventory(self):
        return None

    def days_sales_outstanding(self):
        return None

    def days_payables_outstanding(self):
        return None

    def asset_turnover(self):
        return None


class StraightLine(DepreciationMethods):
    def depreciation_expense(self):
        return None


class DoubleDecliningBalance(DepreciationMethods):
    def depreciation_expense(self):
        return None


class UnitsOfProduction(DepreciationMethods):
    def depreciation_expense(self):
        return None