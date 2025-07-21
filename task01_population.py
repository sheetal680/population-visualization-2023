import matplotlib.pyplot as plt

countries = ["India", "China", "USA", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh"]
populations = [1428627663, 1425887337, 339996563, 277534122, 240485658, 216422446, 223804632, 172954319]

plt.figure(figsize=(12, 6))
bars = plt.bar(countries, populations, color='skyblue')
plt.title("Population by Country (2023)", fontsize=16)
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)

for bar, pop in zip(bars, populations):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{pop//10**6}M',
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(populations, bins=5, color='orange', edgecolor='black')
plt.title("Histogram: Distribution of Population Sizes (2023)", fontsize=16)
plt.xlabel("Population Range")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.show()
