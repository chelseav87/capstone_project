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
        if not solution:
            return ValueError("Insufficient information given or desired variable is already known.")
        if isinstance(solution, list):
            solution = solution[0]
        if isinstance(solution, dict):
            solution = solution[to_solve]
        if hasattr(solution, "free_symbols") and solution.free_symbols:
            return ValueError("Insufficient information given or desired variable is already known.")

        return solution


class DepreciationMethods:
    def __init__(self, asset_cost, salvage_value, useful_life):
        self.asset_cost = asset_cost
        self.salvage_value = salvage_value
        self.useful_life = useful_life

    def depreciation_expense(self, **kwargs):
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


class IncomeStatement(FormulaModel):
    variables = {
        "net_income": symbols("net_income"),
        "net_sales": symbols("net_sales"),
        "gross_sales": symbols("gross_sales"),
        "gross_profit": symbols("gross_profit"),
        "sales_return": symbols("sales_return"),
        "sales_allowances": symbols("sales_allowances"),
        "sales_discounts": symbols("sales_discounts"),
        "cost_of_goods_sold": symbols("cost_of_goods_sold"),
        "purchases": symbols("purchases"),
        "beginning_inventory": symbols("beginning_inventory"),
        "ending_inventory": symbols("ending_inventory"),
        "operating_income": symbols("operating_income"),
        "operating_expenses": symbols("operating_expenses"),
        "revenues": symbols("revenues"),
        "expenses": symbols("expenses")
    }
    equations = [
        Eq(variables["net_sales"], variables["gross_sales"] - variables["sales_return"] - variables["sales_allowances"] - variables["sales_discounts"]),
        Eq(variables["cost_of_goods_sold"], variables["beginning_inventory"] + variables["purchases"] - variables["ending_inventory"]),
        Eq(variables["gross_profit"], variables["net_sales"] - variables["cost_of_goods_sold"]),
        Eq(variables["operating_income"], variables["gross_profit"] - variables["operating_expenses"]),
        Eq(variables["net_income"], variables["revenues"] - variables["expenses"])
    ]


class BalanceSheet(FormulaModel):
    variables = {
        "working_capital": symbols("working_capital"),
        "additional_paid_capital": symbols("additional_paid_capital"),
        "asset_cost": symbols("asset_cost"),
        "asset_book_value": symbols("asset_book_value"),
        "accumulated_depreciation": symbols("accumulated_depreciation"),
        "current_assets": symbols("current_assets"),
        "current_liabilities": symbols("current_liabilities"),
        "total_equity": symbols("total_equity"),
        "retained_earnings": symbols("retained_earnings"),
        "common_stock": symbols("common_stock"),
        "treasury_stock": symbols("treasury_stock")
    }
    equations = [
        Eq(variables["working_capital"], variables["current_assets"] - variables["current_liabilities"]),
        Eq(variables["asset_book_value"], variables["asset_cost"] - variables["accumulated_depreciation"]),
        Eq(variables["total_equity"], variables["common_stock"] + variables["retained_earnings"] + variables["additional_paid_capital"] - variables["treasury_stock"])
    ]


class CashFlow(FormulaModel):
    variables = {
        "free_cash_flow": symbols("free_cash_flow"),
        "operating_cash_flow": symbols("operating_cash_flow"),
        "capital_expenditures": symbols("capital_expenditures"),
        "cash_conversion_cycle": symbols("cash_conversion_cycle"),
        "days_inventory_outstanding": symbols("days_inventory_outstanding"),
        "days_sales_outstanding": symbols("days_sales_outstanding"),
        "days_payable_outstanding": symbols("days_payable_outstanding")
    }
    equations = [
        Eq(variables["free_cash_flow"], variables["operating_cash_flow"] - variables["capital_expenditures"]),
        Eq(variables["cash_conversion_cycle"], variables["days_inventory_outstanding"] + variables["days_sales_outstanding"] - variables["days_payable_outstanding"])
    ]


class ProfitabilityRatios(FormulaModel):
    variables = {
        "net_income": symbols("net_income"),
        "net_sales": symbols("net_sales"),
        "gross_profit": symbols("gross_profit"),
        "profit_margin": symbols("profit_margin"),
        "gross_margin": symbols("gross_margin"),
        "return_on_assets": symbols("return_on_assets"),
        "return_on_equity": symbols("return_on_equity"),
        "earnings_per_share": symbols("earnings_per_share"),
        "price_to_earning_ratio": symbols("price_to_earning_ratio"),
        "average_total_assets": symbols("average_total_assets"),
        "average_stockholders_equity": symbols("average_stockholders_equity"),
        "preferred_dividends": symbols("preferred_dividends"),
        "market_price_per_share": symbols("market_price_per_share"),
        "weighted_average_common_shares": symbols("weighted_average_common_shares"),
    }
    equations = [
        Eq(variables["profit_margin"], (variables["net_income"] / variables["net_sales"]) * 100),
        Eq(variables["gross_margin"], (variables["gross_profit"] / variables["net_sales"]) * 100),
        Eq(variables["return_on_assets"], (variables["net_income"] / variables["average_total_assets"]) * 100),
        Eq(variables["return_on_equity"], (variables["net_income"] / variables["average_stockholders_equity"]) * 100),
        Eq(variables["earnings_per_share"], (variables["net_income"] - variables["preferred_dividends"]) / variables["weighted_average_common_shares"]),
        Eq(variables["price_to_earning_ratio"], variables["market_price_per_share"] / variables["earnings_per_share"])
    ]


class LiquidityRatios(FormulaModel):
    variables = {
        "current_ratio": symbols("current_ratio"),
        "current_assets": symbols("current_assets"),
        "current_liabilities": symbols("current_liabilities"),
        "quick_ratio": symbols("quick_ratio"),
        "cash_ratio": symbols("cash_ratio"),
        "cash": symbols("cash"),
        "cash_equivalents": symbols("cash_equivalents"),
        "accounts_receivables": symbols("accounts_receivables"),
        "marketable_securities": symbols("marketable_securities"),
    }
    equations = [
        Eq(variables["current_ratio"], variables["current_assets"] / variables["current_liabilities"]),
        Eq(variables["quick_ratio"], (variables["cash"] + variables["marketable_securities"] + variables["accounts_receivables"]) / variables["current_liabilities"]),
        Eq(variables["cash_ratio"], (variables["cash"] + variables["cash_equivalents"]) / variables["current_liabilities"])
    ]


class SolvencyRatios(FormulaModel):
    variables = {
        "total_assets": symbols("total_assets"),
        "total_liabilities": symbols("total_liabilities"),
        "total_equity": symbols("total_equity"),
        "debt_ratio": symbols("debt_ratio"),
        "debt_to_equity_ratio": symbols("debt_to_equity_ratio"),
        "times_interest_earned": symbols("times_interest_earned"),
        "equity_multiplier": symbols("equity_multiplier"),
        "income_before_interest_and_taxes": symbols("income_before_interest_and_taxes"),
        "interest_expense": symbols("interest_expense")
    }
    equations = [
        Eq(variables["debt_ratio"], (variables["total_liabilities"] / variables["total_assets"]) * 100),
        Eq(variables["debt_to_equity_ratio"], (variables["total_liabilities"] / variables["total_equity"]) * 100),
        Eq(variables["times_interest_earned"], variables["income_before_interest_and_taxes"] / variables["interest_expense"]),
        Eq(variables["equity_multiplier"], variables["total_assets"] / variables["total_equity"])
    ]


class EfficiencyRatios(FormulaModel):
    variables = {
        "asset_turnover": symbols("asset_turnover"),
        "inventory_turnover": symbols("inventory_turnover"),
        "accounts_receivable_turnover": symbols("accounts_receivable_turnover"),
        "accounts_payable_turnover": symbols("accounts_payable_turnover"),
        "days_sales_in_inventory": symbols("days_sales_in_inventory"),
        "days_sales_outstanding": symbols("days_sales_outstanding"),
        "days_payables_outstanding": symbols("days_payables_outstanding"),
        "cost_of_goods_sold": symbols("cost_of_goods_sold"),
        "net_sales": symbols("net_sales"),
        "net_credit_sales": symbols("net_credit_sales"),
        "average_inventory": symbols("average_inventory"),
        "average_accounts_receivable": symbols("average_accounts_receivable"),
        "average_accounts_payable": symbols("average_accounts_payable"),
        "average_total_assets": symbols("average_total_assets")
    }
    equations = [
        Eq(variables["inventory_turnover"], variables["cost_of_goods_sold"] / variables["average_inventory"]),
        Eq(variables["accounts_receivable_turnover"], variables["net_credit_sales"] / variables["average_accounts_receivable"]),
        Eq(variables["accounts_payable_turnover"], variables["cost_of_goods_sold"] / variables["average_accounts_payable"]),
        Eq(variables["days_sales_in_inventory"], 365 / variables["inventory_turnover"]),
        Eq(variables["days_sales_outstanding"], 365 / variables["accounts_receivable_turnover"]),
        Eq(variables["days_payables_outstanding"], 365 / variables["accounts_payable_turnover"]),
        Eq(variables["asset_turnover"], variables["net_sales"] / variables["average_total_assets"]),
    ]


class StraightLine(DepreciationMethods):
    def depreciation_expense(self):
        return f"{((self.asset_cost - self.salvage_value) / self.useful_life):.02f}"


class DoubleDecliningBalance(DepreciationMethods):
    def depreciation_expense(self, year_end):
        double_declining_rate = 2 / self.useful_life
        book_value = self.asset_cost * ((1-double_declining_rate) ** (year_end - 1))
        return f"{(book_value * double_declining_rate):.02f}"


class UnitsOfProduction(DepreciationMethods):
    def __init__(self, asset_cost, salvage_value, useful_life, total_units):
        super().__init__(asset_cost, salvage_value, useful_life)
        self.total_units = total_units

    def depreciation_expense(self, units_produced):
        depreciation_per_unit = (self.asset_cost - self.salvage_value) / self.total_units
        return f"{(depreciation_per_unit * units_produced):.02f}"
