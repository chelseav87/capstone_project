# --- Base Classes --- #
class FormulaGroup:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class DepreciationMethods:
    def __init__(self):
        pass

    def depreciation_expense(self):
        pass


# --- Derived Classes --- #
class FundamentalEquations(FormulaGroup):
    def accounting_equation(self):
        return None

    def accounting_expanded_equation(self):
        return None


class IncomeStatement(FormulaGroup):
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


class BalanceSheet(FormulaGroup):
    def working_capital(self):
        return None

    def asset_book_value(self):
        return None

    def total_equity(self):
        return None

class CashFlow(FormulaGroup):
    def free_cash_flow(self):
        return None

    def cash_conversion_cycle(self):
        return None


class ProfitabilityRatios(FormulaGroup):
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


class LiquidityRatios(FormulaGroup):
    def current(self):
        return None

    def quick(self):
        return None

    def cash(self):
        return None


class SolvencyRatios(FormulaGroup):
    def debt(self):
        return None

    def debt_to_equity(self):
        return None

    def times_interest_earned(self):
        return None

    def equity_multiplier(self):
        return None


class EfficiencyRatios(FormulaGroup):
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