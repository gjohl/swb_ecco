# Data Sources
Notes on various data sources identified so far.


## UNSD
This is available through the [browser client here]((https://data.un.org/SdmxBrowser/start)). This can be queried manually through the website and the results downloaded to CSV files.

There are two tabs that are relevant to us:
- UNSD Energy Statistics: Public dataset of energy statistics (installed capacity, sector consumption, etc.)
- UNSD Energy Balance: Public dataset of energy balance (production, import, export, etc.)  


## SciGRID 
SciGRID gas is an open-source gas transmission data model for Europe

The SciGRID data and many more sources are listed [here](https://wiki.openmod-initiative.org/wiki/)

## Open Power System Data
A platform for open data of the European power system. 

Data available [here](https://open-power-system-data.org/)

Presumably the time series data will be most relevant to us. (Available [here](https://data.open-power-system-data.org/time_series/))

This has two timestamp columns: `cet_cest_timestamp, utc_timestamp`

It has the following columns, each prefixed by a country code:
```
load_actual_entsoe_transparency
load_forecast_entsoe_transparency
price_day_ahead
solar_capacity
solar_generation_actual
solar_profile
wind_capacity
wind_generation_actual
wind_offshore_capacity
wind_offshore_generation_actual
wind_offshore_profile
wind_onshore_capacity
wind_onshore_generation_actual
wind_onshore_profile
```

The country codes present:
```
['AT', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI', 'FR', 'GB',
 'GR', 'HR', 'HU', 'IE', 'IT', 'LT', 'LU', 'LV', 'ME', 'NL', 'NO', 'PL', 'PT',
 'RO', 'RS', 'SE', 'SI', 'SK', 'UA']
```

## Atlite
Python library for converting weather data (such as wind speeds, solar radiation, temperature and runoff) into power systems data (such as wind power, solar power, hydro power and heating demand time series) See [GitHub page here](https://github.com/PyPSA/atlite)
