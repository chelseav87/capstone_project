from sympy import *

field_error = ValueError("Insufficient information given.")

# --- Base Classes --- #
class FormulaModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class DepreciationMethods:
    def __init__(self, asset_cost, salvage_value, useful_life):
        self.asset_cost = asset_cost
        self.salvage_value = salvage_value
        self.useful_life = useful_life

    def depreciation_expense(self):
        return None


# --- Derived Classes --- #
class FundamentalEquations(FormulaModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.values = kwargs

    def accounting_equation(self, to_solve):
        assets, liabilities, equity = symbols("assets, liabilities, equity")
        accounting_equation = Eq(assets, liabilities + equity)

        known_values = {symbols(key): value for key, value in self.values.items()}
        solution = solve(accounting_equation.subs(known_values), symbols(to_solve))

        if not solution:
            return field_error

        return f"${solution[0]:.02f}"

    def accounting_expanded_equation(self):
        return field_error

# creating an object instance test, to be deleted once GUI is completed
test = FundamentalEquations(liabilities=1000, equity=9000)
print(test.accounting_equation("assets"))


class IncomeStatement(FormulaModel):
    def net_sales(self):
        return field_error

    def cost_of_goods_sold(self):
        return field_error

    def gross_profit(self):
        return field_error

    def operating_income(self):
        return field_error

    def net_income(self):
        return field_error


class BalanceSheet(FormulaModel):
    def working_capital(self):
        return field_error

    def asset_book_value(self):
        return field_error

    def total_equity(self):
        return field_error

class CashFlow(FormulaModel):
    def free_cash_flow(self):
        return field_error

    def cash_conversion_cycle(self):
        return field_error


class ProfitabilityRatios(FormulaModel):
    def profit_margin(self):
        return field_error

    def gross_margin(self):
        return field_error

    def return_on_assets(self):
        return field_error

    def return_on_equity(self):
        return field_error

    def earnings_per_share(self):
        return field_error

    def price_to_earnings(self):
        return field_error


class LiquidityRatios(FormulaModel):
    def current(self):
        return field_error

    def quick(self):
        return field_error

    def cash(self):
        return field_error


class SolvencyRatios(FormulaModel):
    def debt(self):
        return field_error

    def debt_to_equity(self):
        return field_error

    def times_interest_earned(self):
        return field_error

    def equity_multiplier(self):
        return field_error


class EfficiencyRatios(FormulaModel):
    def inventory_turnover(self):
        return field_error

    def accounts_receivable_turnover(self):
        return field_error

    def accounts_payable_turnover(self):
        return field_error

    def days_sales_in_inventory(self):
        return field_error

    def days_sales_outstanding(self):
        return field_error

    def days_payables_outstanding(self):
        return field_error

    def asset_turnover(self):
        return field_error


class StraightLine(DepreciationMethods):
    def depreciation_expense(self):
        return field_error


class DoubleDecliningBalance(DepreciationMethods):
    def depreciation_expense(self):
        return field_error


class UnitsOfProduction(DepreciationMethods):
    def depreciation_expense(self):
        return field_error