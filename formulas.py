from sympy import *

# --- Base Classes --- #
class FormulaModel:
    variables = {}
    equations = []

    def __init__(self, **kwargs):
        self.values = kwargs

    def solve(self, target):
        to_solve = self.variables[target]

        known_values = {self.variables[key]: value for key, value in self.values.items()}

        relevant_equations = []
        for equation in self.equations:
            if to_solve in equation.free_symbols:
                invalid_variables = equation.free_symbols - {to_solve}
                if all(variable in known_values for variable in invalid_variables):
                    relevant_equations.append(equation)

        known_values = [equation.subs(known_values) for equation in relevant_equations]
        solution = solve(known_values[0], to_solve)

        if isinstance(solution, list):
            solution = solution[0]
        if isinstance(solution, dict):
            solution = solution[to_solve]
        return solution


class DepreciationMethods:
    def __init__(self, asset_cost, salvage_value, useful_life):
        self.asset_cost = float(asset_cost)
        self.salvage_value = float(salvage_value)
        self.useful_life = float(useful_life)

    def depreciation_expense(self, **kwargs):
        return None


# --- Derived Classes --- #
class FundamentalEquations(FormulaModel):
    variables = {
        "Assets": symbols("assets"),
        "Liabilities": symbols("liabilities"),
        "Equity": symbols("equity"),
        "Common Stock": symbols("common_stock"),
        "Dividends": symbols("dividends"),
        "Revenues": symbols("revenues"),
        "Expenses": symbols("expenses")
    }
    equations = [
        Eq(variables["Assets"], variables["Liabilities"] + variables["Equity"]),
        Eq(variables["Equity"], variables["Common Stock"] + variables["Revenues"] - variables["Expenses"]- variables["Dividends"])
    ]


class IncomeStatement(FormulaModel):
    variables = {
        "Net Income": symbols("net_income"),
        "Net Sales": symbols("net_sales"),
        "Gross Sales": symbols("gross_sales"),
        "Gross Profit": symbols("gross_profit"),
        "Sales Return": symbols("sales_return"),
        "Sales Allowances": symbols("sales_allowances"),
        "Sales Discounts": symbols("sales_discounts"),
        "Cost of Goods Sold": symbols("cost_of_goods_sold"),
        "Purchases": symbols("purchases"),
        "Beginning Inventory": symbols("beginning_inventory"),
        "Ending Inventory": symbols("ending_inventory"),
        "Operating Income": symbols("operating_income"),
        "Operating Expenses": symbols("operating_expenses"),
        "Revenues": symbols("revenues"),
        "Expenses": symbols("expenses")
    }
    equations = [
        Eq(variables["Net Sales"], variables["Gross Sales"] - variables["Sales Return"] - variables["Sales Allowances"] - variables["Sales Discounts"]),
        Eq(variables["Cost of Goods Sold"], variables["Beginning Inventory"] + variables["Purchases"] - variables["Ending Inventory"]),
        Eq(variables["Gross Profit"], variables["Net Sales"] - variables["Cost of Goods Sold"]),
        Eq(variables["Operating Income"], variables["Gross Profit"] - variables["Operating Expenses"]),
        Eq(variables["Net Income"], variables["Revenues"] - variables["Expenses"])
    ]


class BalanceSheet(FormulaModel):
    variables = {
        "Working Capital": symbols("working_capital"),
        "Additional Paid Capital": symbols("additional_paid_capital"),
        "Asset Cost": symbols("asset_cost"),
        "Asset Book Value": symbols("asset_book_value"),
        "Accumulated Depreciation": symbols("accumulated_depreciation"),
        "Current Assets": symbols("current_assets"),
        "Current Liabilities": symbols("current_liabilities"),
        "Total Equity": symbols("total_equity"),
        "Retained Earnings": symbols("retained_earnings"),
        "Common Stock": symbols("common_stock"),
        "Treasury Stock": symbols("treasury_stock")
    }
    equations = [
        Eq(variables["Working Capital"], variables["Current Assets"] - variables["Current Liabilities"]),
        Eq(variables["Asset Book Value"], variables["Asset Cost"] - variables["Accumulated Depreciation"]),
        Eq(variables["Total Equity"], variables["Common Stock"] + variables["Retained Earnings"] + variables["Additional Paid Capital"] - variables["Treasury Stock"])
    ]


class CashFlow(FormulaModel):
    variables = {
        "Free Cash Flow": symbols("free_cash_flow"),
        "Operating Cash Flow": symbols("operating_cash_flow"),
        "Capital Expenditures": symbols("capital_expenditures"),
        "Cash Conversion Cycle": symbols("cash_conversion_cycle"),
        "Days Inventory Outstanding": symbols("days_inventory_outstanding"),
        "Days Sales Outstanding": symbols("days_sales_outstanding"),
        "Days Payable Outstanding": symbols("days_payable_outstanding")
    }
    equations = [
        Eq(variables["Free Cash Flow"], variables["Operating Cash Flow"] - variables["Capital Expenditures"]),
        Eq(variables["Cash Conversion Cycle"], variables["Days Inventory Outstanding"] + variables["Days Sales Outstanding"] - variables["Days Payable Outstanding"])
    ]


class ProfitabilityRatios(FormulaModel):
    variables = {
        "Net Income": symbols("net_income"),
        "Net Sales": symbols("net_sales"),
        "Gross Profit": symbols("gross_profit"),
        "Gross Margin": symbols("gross_margin"),
        "Profit Margin": symbols("profit_margin"),
        "Return On Assets": symbols("return_on_assets"),
        "Return On Equity": symbols("return_on_equity"),
        "Earnings Per Share": symbols("earnings_per_share"),
        "Price to Earning Ratio": symbols("price_to_earning_ratio"),
        "Average Total Assets": symbols("average_total_assets"),
        "Average Stockholders Equity": symbols("average_stockholders_equity"),
        "Preferred Dividends": symbols("preferred_dividends"),
        "Market Price Per Share": symbols("market_price_per_share"),
        "Weighted Average Common Shares": symbols("weighted_average_common_shares"),
    }
    equations = [
        Eq(variables["Profit Margin"], (variables["Net Income"] / variables["Net Sales"]) * 100),
        Eq(variables["Gross Margin"], (variables["Gross Profit"] / variables["Net Sales"]) * 100),
        Eq(variables["Return On Assets"], (variables["Net Income"] / variables["Average Total Assets"]) * 100),
        Eq(variables["Return On Equity"], (variables["Net Income"] / variables["Average Stockholders Equity"]) * 100),
        Eq(variables["Earnings Per Share"], (variables["Net Income"] - variables["Preferred Dividends"]) / variables["Weighted Average Common Shares"]),
        Eq(variables["Price to Earning Ratio"], variables["Market Price Per Share"] / variables["Earnings Per Share"])
    ]


class LiquidityRatios(FormulaModel):
    variables = {
        "Current Ratio": symbols("current_ratio"),
        "Current Assets": symbols("current_assets"),
        "Current Liabilities": symbols("current_liabilities"),
        "Quick Ratio": symbols("quick_ratio"),
        "Cash Ratio": symbols("cash_ratio"),
        "Cash": symbols("cash"),
        "Cash Equivalents": symbols("cash_equivalents"),
        "Accounts Receivables": symbols("accounts_receivables"),
        "Marketable Securities": symbols("marketable_securities"),
    }
    equations = [
        Eq(variables["Current Ratio"], variables["Current Assets"] / variables["Current Liabilities"]),
        Eq(variables["Quick Ratio"], (variables["Cash"] + variables["Marketable Securities"] + variables["Accounts Receivables"]) / variables["Current Liabilities"]),
        Eq(variables["Cash Ratio"], (variables["Cash"] + variables["Cash Equivalents"]) / variables["Current Liabilities"])
    ]


class SolvencyRatios(FormulaModel):
    variables = {
        "Total Assets": symbols("total_assets"),
        "Total Liabilities": symbols("total_liabilities"),
        "Total Equity": symbols("total_equity"),
        "Debt Ratio": symbols("debt_ratio"),
        "Debt to Equity Ratio": symbols("debt_to_equity_ratio"),
        "Times Interest Earned": symbols("times_interest_earned"),
        "Equity Multiplier": symbols("equity_multiplier"),
        "Income Before Interest & Taxes": symbols("income_before_interest_and_taxes"),
        "Interest Expense": symbols("interest_expense")
    }
    equations = [
        Eq(variables["Debt Ratio"], (variables["Total Liabilities"] / variables["Total Assets"]) * 100),
        Eq(variables["Debt to Equity Ratio"], (variables["Total Liabilities"] / variables["Total Equity"]) * 100),
        Eq(variables["Times Interest Earned"], variables["Income Before Interest & Taxes"] / variables["Interest Expense"]),
        Eq(variables["Equity Multiplier"], variables["Total Assets"] / variables["Total Equity"])
    ]


class EfficiencyRatios(FormulaModel):
    variables = {
        "Asset Turnover": symbols("asset_turnover"),
        "Inventory Turnover": symbols("inventory_turnover"),
        "Accounts Receivable Turnover": symbols("accounts_receivable_turnover"),
        "Accounts Payable Turnover": symbols("accounts_payable_turnover"),
        "Days Sales in Inventory": symbols("days_sales_in_inventory"),
        "Days Sales Outstanding": symbols("days_sales_outstanding"),
        "Days Payables Outstanding": symbols("days_payables_outstanding"),
        "Cost of Goods Sold": symbols("cost_of_goods_sold"),
        "Net Sales": symbols("net_sales"),
        "Net Credit Sales": symbols("net_credit_sales"),
        "Average Inventory": symbols("average_inventory"),
        "Average Accounts Receivable": symbols("average_accounts_receivable"),
        "Average Accounts Payable": symbols("average_accounts_payable"),
        "Average Total Assets": symbols("average_total_assets")
    }
    equations = [
        Eq(variables["Inventory Turnover"], variables["Cost of Goods Sold"] / variables["Average Inventory"]),
        Eq(variables["Accounts Receivable Turnover"], variables["Net Credit Sales"] / variables["Average Accounts Receivable"]),
        Eq(variables["Accounts Payable Turnover"], variables["Cost of Goods Sold"] / variables["Average Accounts Payable"]),
        Eq(variables["Days Sales in Inventory"], 365 / variables["Inventory Turnover"]),
        Eq(variables["Days Sales Outstanding"], 365 / variables["Accounts Receivable Turnover"]),
        Eq(variables["Days Payables Outstanding"], 365 / variables["Accounts Payable Turnover"]),
        Eq(variables["Asset Turnover"], variables["Net Sales"] / variables["Average Total Assets"])
    ]


class StraightLine(DepreciationMethods):
    variables = {
        "Asset Cost": float,
        "Salvage Value": float,
        "Useful Life": int
    }

    def depreciation_expense(self):
        return (self.asset_cost - self.salvage_value) / self.useful_life


class DoubleDecliningBalance(DepreciationMethods):
    variables = {
        "Asset Cost": float,
        "Salvage Value": float,
        "Useful Life": int,
        "Year End": int
    }

    def depreciation_expense(self, year_end):
        double_declining_rate = 2 / self.useful_life
        book_value = self.asset_cost * ((1-double_declining_rate) ** (year_end - 1))
        return book_value * double_declining_rate


class UnitsOfProduction(DepreciationMethods):
    variables = {
        "Asset Cost": float,
        "Salvage Value": float,
        "Useful Life": int,
        "Total Units": int,
        "Units Produced": int
    }

    def __init__(self, asset_cost, salvage_value, useful_life, total_units):
        super().__init__(asset_cost, salvage_value, useful_life)
        self.total_units = total_units

    def depreciation_expense(self, units_produced):
        depreciation_per_unit = (self.asset_cost - self.salvage_value) / self.total_units
        return depreciation_per_unit * units_produced
