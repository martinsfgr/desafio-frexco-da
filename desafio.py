import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_excel("Dados.xlsx", engine="openpyxl")

model = ARIMA(df["Vendas"], order=(2, 1, 1))
model_fit = model.fit()
demand_forecast = round(model_fit.forecast(steps=5), 2)

print("A previsão de demanda do item nos próximos cinco dias segue a seguinte ordem:")

for i in range(1, len(demand_forecast)+1):
    print(f"{i}º dia - R${list(demand_forecast)[i-1]}")
