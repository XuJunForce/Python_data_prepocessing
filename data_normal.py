import pandas as pd

# file_path = "your_path"
# data = pd.read_csv(file_path)

data = pd.DataFrame(
    {
        'A': [1, 2, 3],
        'B': ['A', 'B', 'C'],
        'C': [7, 10, 90]

    }
)
numeric_features = data.dtypes[data.dtypes != object].index
print(f"numer_features = {numeric_features}")
data_normal = data[numeric_features].apply(lambda x: (x - x.mean()) / (x.std()), axis=1)
data_normal = data_normal[numeric_features].fillna(0)
print(data_normal.head())
