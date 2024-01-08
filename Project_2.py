import pandas as pd
import matplotlib.pyplot as plt
sa = pd.read_csv("Housing.csv")
print("количество спален в самом дешёвом доме:", sa[sa["price"] == sa["price"].min()]["bedrooms"].min())
print("количество домов, в которых количество спален не больше количества ванных:",
      sa[sa["bedrooms"] <= sa["bathrooms"]].count()["bedrooms"])
print("стоимость самого дешёвого дома с гостевой комнатой:", sa[sa["guestroom"] == "yes"]["price"].min())
print("дома ценой от 5.000.000 или до 2.000.000 денег, с кондиционированием воздуха:",
      sa[sa[(2000000 <= sa["price"]) | (5000000 >= sa["price"])]["airconditioning"]=="yes"].count()["bedrooms"])
x=sa["price"]
y=sa["area"]
plt.plot(x,y)
plt.show()