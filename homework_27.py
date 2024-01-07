import pandas as pd
sa = pd.read_csv("Customers.csv")
df = sa
ans = sa[(sa["Income"] < 30000) & (sa["Age"] > 30)]
art = sa[(sa["Profession"] == "Lawyer") & (sa["Work Experience"] > 5)]
print(ans, art)