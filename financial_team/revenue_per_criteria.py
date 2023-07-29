import matplotlib.pyplot as plt
import pandas as pd

df_revenue = pd.read_csv("../data/revenue.csv")
df_installs = pd.read_csv("../data/installs.csv")
####################################### Revenue by app ##############################
df_revenue_installs = pd.merge(df_revenue, df_installs, on="install_id")

df_revenue_by_app = (
    df_revenue_installs.groupby("app_id")["value_usd"].sum().reset_index()
)
df_revenue_by_app = df_revenue_by_app.sort_values("value_usd", ascending=False)
print(len(df_revenue_by_app))
# get the top 10 rows
df_top10_revenue_by_app = df_revenue_by_app.head(10)

# sum the remaining rows and store it in a new row named "Other"
other_sum = df_revenue_by_app.iloc[10:, :]["value_usd"].sum()
df_other = pd.DataFrame([["Other", other_sum]], columns=["app_id", "value_usd"])

# concatenate the top 10 rows and the "Other" row to create a new dataframe
df_new_revenue_by_app = pd.concat([df_top10_revenue_by_app, df_other])

# reset the index of the new dataframe
df_new_revenue_by_app = df_new_revenue_by_app.reset_index(drop=True)

plt.pie(
    df_new_revenue_by_app["value_usd"],
    labels=df_new_revenue_by_app["app_id"],
    autopct="%1.1f%%",
    startangle=90,
)

plt.title("Revenue by App")
plt.axis("equal")

plt.show()

##################################################################################################################################
############################Revenue by country##################################################################################

df_revenue_by_country = (
    df_revenue_installs.groupby("country_id")["value_usd"].sum().reset_index()
)
df_revenue_by_country = df_revenue_by_country.sort_values("value_usd", ascending=False)

plt.pie(
    df_revenue_by_country["value_usd"],
    labels=df_revenue_by_country["country_id"],
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Revenue by country")

plt.show()

##################################################################################################################################
############################Revenue by network##################################################################################
df_revenue_by_network = (
    df_revenue_installs.groupby("network_id")["value_usd"].sum().reset_index()
)
df_revenue_by_network = df_revenue_by_network.sort_values("value_usd", ascending=False)

plt.pie(
    df_revenue_by_network["value_usd"],
    labels=df_revenue_by_network["network_id"],
    autopct="%1.1f%%",
    startangle=90,
)

plt.title("Revenue by network")
plt.show()

##################################################################################################################################
############################ Avarage revenue per user ##################################################################################
# Load the revenue data into a pandas DataFrame

# Group the revenue data by install_id and calculate the mean revenue for each group
df_revenue_per_user = df_revenue.groupby("install_id")["value_usd"].mean()
average_revenue_per_user = df_revenue_per_user.mean()
print(average_revenue_per_user)
