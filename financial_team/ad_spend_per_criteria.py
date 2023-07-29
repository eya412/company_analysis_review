import pandas as pd
import matplotlib.pyplot as plt

df_adspend = pd.read_csv("../data/adspend.csv")


############################################################################################
############################ Adspend by country ############################################

adspend_by_country = df_adspend.groupby("country_id")["value_usd"].sum().reset_index()
# print(adspend_by_country)

plt.pie(
    adspend_by_country["value_usd"],
    labels=adspend_by_country["country_id"],
    autopct="%1.1f%%",
)
plt.title("Ad Spend by Country")
plt.show()
############################################################################################
############################ Adspend by network ############################################
adspend_by_network = df_adspend.groupby("network_id")["value_usd"].sum().reset_index()

plt.pie(
    adspend_by_network["value_usd"],
    labels=adspend_by_network["network_id"],
    autopct="%1.1f%%",
)
plt.title("Ad spend by network")
plt.show()
