import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
selected_columns = content[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

x = selected_columns["Mortality rate, infant (per 1,000 live births)"]
y = selected_columns["GDP per capita (constant 2010 US$)"]

plt.scatter(x, y, color="red")
# fig, ax = plt.subplots()
# ax.plot(selected_columns)
plt.xlabel("GDP per Capita")
plt.ylabel("Mortality rate")
plt.show()
