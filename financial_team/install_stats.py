import pandas as pd
import matplotlib.pyplot as plt

# df_revenue = pd.read_csv("../data/revenue.csv")
df_installs = pd.read_csv("../data/installs.csv")
df_adspend = pd.read_csv("../data/adspend.csv")
# df_payout = pd.read_csv("../data/payouts.csv")
total_ad_spend = df_adspend["value_usd"].sum()


total_installs = df_installs["install_id"].nunique()

cost_per_install = total_ad_spend / total_installs

print("The cost per install is:", cost_per_install)
