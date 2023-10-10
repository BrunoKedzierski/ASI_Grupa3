from ucimlrepo import fetch_ucirepo
mushroom = fetch_ucirepo(id=73)

X = mushroom.data.features
y = mushroom.data.targets

# metadata 
print(mushroom.metadata)

# variable information