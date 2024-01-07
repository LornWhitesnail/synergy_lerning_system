import pandas as pd
data = pd.DataFrame([[1, "Turmeric", 124353, 145, 250], [2, "Pepper", 127633, 100, 400],
                    [3, "Lavender", 120197, 100, 350], [4, "Chamomile", 123044, 100, 200],
                    [5, "Plantain", 127992, 100, 30], [6, "Chanterelle", 133049, 100, 270]],
                    columns=["#", "Product", "index", "weight", "price"])
print(data)
print("")
print(data.head(3))
print("")
print(data.tail(3))
data.to_csv("data.csv")