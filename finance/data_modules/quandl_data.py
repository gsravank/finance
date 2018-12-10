import quandl

quandl.ApiConfig.api_key = "8Urx4Dauxazi_4xTzgoB"

data = quandl.get("NSE/RELIANCE")

print(type(data))
print(data)

data.to_csv('../data/reliance_data.csv')
