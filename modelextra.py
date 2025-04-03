#MODELLO BONUS
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


df = pd.read_excel("C:\\Users\\greta\\OneDrive\\Desktop\\progetto\\Real estate valuation data set.xlsx")

df.columns = [
    "No", "transaction_date", "house_age", "distance_to_MRT",
    "n_convenience", "latitude", "longitude", "price_per_metro"
]

# var dipendente e indipendenti
X_alt = df[["house_age", "distance_to_MRT", "n_convenience"]]
y = df["price_per_metro"]

# modello
model_extra = LinearRegression()
model_extra.fit(X_alt, y)


joblib.dump(model_extra, "model_extra.pkl")