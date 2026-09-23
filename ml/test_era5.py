import cdsapi

client = cdsapi.Client()

client.retrieve(
    "reanalysis-era5-single-levels",
    {
        "product_type": "reanalysis",
        "variable": [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "total_precipitation",
            "2m_temperature"
        ],
        "year": "2024",
        "month": "01",
        "day": "01",
        "time": [
            "00:00",
            "06:00",
            "12:00",
            "18:00"
        ],
        "area": [
            40.75,
            -74.50,
            40.25,
            -74.00
        ],
        "data_format": "netcdf",
        "download_format": "unarchived"
    },
    "era5_test.nc"
)

print("ERA5 test download successful!")