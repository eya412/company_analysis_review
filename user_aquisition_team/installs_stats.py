import pandas as pd
import matplotlib.pyplot as plt

df_installs = pd.read_csv("../data/installs.csv")
# Total installs
print("Total installs : ", len(df_installs))
############# Installs by app #############
df_installs_by_app = df_installs.groupby("app_id")["install_id"].nunique()
df_installs_by_app.plot.bar(figsize=(8, 6))
plt.title("Installs by App")
plt.xlabel("App ID")
plt.ylabel("Number of Installs")
plt.show()

############# Installs by country #############
df_installs_by_country = df_installs.groupby("country_id")["install_id"].nunique()
labels = df_installs_by_country.index.tolist()
values = df_installs_by_country.values.tolist()

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.axis("equal")
plt.title('Install by country')
plt.show()
plt.show()

############# Installs by network #############
df_installs_by_network = df_installs.groupby("network_id")["install_id"].nunique()
labels = df_installs_by_network.index.tolist()
values = df_installs_by_network.values.tolist()
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.axis("equal")
plt.title('Install by network')
plt.show()
