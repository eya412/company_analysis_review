import pandas as pd
import matplotlib.pyplot as plt

df_revenue = pd.read_csv("../data/revenue.csv")
df_adspend = pd.read_csv("../data/adspend.csv")
df_payout = pd.read_csv("../data/payouts.csv")
############################################################################################
############################ Revenue #########################################################
total_revenue = df_revenue["value_usd"].sum()
print("Total revenue in 2022: ", total_revenue)

# revenue per month
df_revenue_per_month = df_revenue[["event_date", "value_usd"]]
df_revenue_per_month["event_date"] = pd.to_datetime(df_revenue_per_month["event_date"])
df_revenue_per_month["month"] = df_revenue_per_month["event_date"].dt.month
df_revenue_per_month["sum_revenue"] = df_revenue_per_month.groupby("month")[
    "value_usd"
].transform("sum")
df_revenue_per_month = df_revenue_per_month[["month", "sum_revenue"]]
df_revenue_per_month = df_revenue_per_month.drop_duplicates()
df_revenue_per_month.plot(
    x="month", y="sum_revenue", kind="line", title="Revenue per Month"
)
plt.xticks(df_revenue_per_month["month"])
plt.show()
############################################################################################
############################ Adspend ########################################################
total_adspend = df_adspend["value_usd"].sum()
print("Total adspend in 2022: ", total_adspend)
df_adspend_per_month = df_adspend[["event_date", "value_usd"]]
df_adspend_per_month["event_date"] = pd.to_datetime(df_adspend_per_month["event_date"])
df_adspend_per_month["month"] = df_adspend_per_month["event_date"].dt.month
df_adspend_per_month["sum_adspend"] = df_adspend_per_month.groupby("month")[
    "value_usd"
].transform("sum")
df_adspend_per_month = df_adspend_per_month[["month", "sum_adspend"]]
df_adspend_per_month = df_adspend_per_month.drop_duplicates()
df_adspend_per_month.plot(
    x="month", y="sum_adspend", kind="line", title="adspend per Month"
)
plt.xticks(df_adspend_per_month["month"])
plt.show()

############################################################################################
############################ Payouts ########################################################
total_payouts = df_payout["value_usd"].sum()
print("Total payouts in 2022: ", total_payouts)
df_payouts_per_month = df_payout[["event_date", "value_usd"]]
df_payouts_per_month["event_date"] = pd.to_datetime(df_payouts_per_month["event_date"])
df_payouts_per_month["month"] = df_payouts_per_month["event_date"].dt.month
df_payouts_per_month["event_date"].to_list()
df_payouts_per_month["sum_payouts"] = df_payouts_per_month.groupby("month")[
    "value_usd"
].transform("sum")
df_payouts_per_month = df_payouts_per_month[["month", "sum_payouts"]]
df_payouts_per_month = df_payouts_per_month.drop_duplicates()
df_payouts_per_month.plot(
    x="month", y="sum_payouts", kind="line", title="payouts per Month"
)
plt.xticks(df_payouts_per_month["month"])
plt.show()

############################################################################################
############################ Expenses ########################################################
total_expenses = total_adspend + total_payouts
print("Total expenses in 2022: ", total_expenses)

df_merged_expenses = pd.merge(
    df_payouts_per_month, df_adspend_per_month, on="month", how="outer"
)
df_merged_expenses["total_expenses"] = (
    df_merged_expenses["sum_payouts"] + df_merged_expenses["sum_adspend"]
)

df_merged_expenses.plot(
    x="month", y="total_expenses", kind="line", title="expenses per Month"
)
plt.xticks(df_merged_expenses["month"])
plt.show()

############################################################################################
############################ Profit ########################################################

total_profit = total_revenue - total_expenses
print("Total profit in 2022: ", total_profit)
df_merged_profit = pd.merge(
    df_revenue_per_month, df_merged_expenses, on="month", how="outer"
)
df_merged_profit["profit_per_month"] = (
    df_merged_profit["sum_revenue"] - df_merged_profit["total_expenses"]
)
df_merged_profit.plot(
    x="month", y="profit_per_month", kind="line", title="Profit per month"
)
plt.xticks(df_merged_profit["month"])
plt.show()

# get two plots in the same graph
fig, ax = plt.subplots()

df_revenue_per_month.plot(
    x="month",
    y="sum_revenue",
    kind="line",
    title="Revenue and Expenses per Month",
    ax=ax,
)
ax.set_xticks(df_revenue_per_month["month"])

df_merged_expenses.plot(x="month", y="total_expenses", kind="line", ax=ax)
ax.set_xticks(df_merged_expenses["month"])

ax.legend(["Revenue", "Expenses"])

plt.show()

print(df_merged_profit)
