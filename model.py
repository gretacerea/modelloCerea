#SVILUPPO DEL MODELLO
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib


df = pd.read_excel("C:\\Users\\greta\\OneDrive\\Desktop\\progetto\\Real estate valuation data set.xlsx")


df.columns = [
    "No", "transaction_date", "house_age", "distance_to_MRT",
    "n_convenience", "latitude", "longitude", "price_per_metro"
]

# var dipendente e indipendenti
X = df[["latitude", "longitude"]]
y = df["price_per_metro"]

#test e train test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#creazione modello
model = LinearRegression()
model.fit(X_train, y_train)
joblib.dump(model, "model_latlong.pkl")