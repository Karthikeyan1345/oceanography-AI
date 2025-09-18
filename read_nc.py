import xarray as xr

file_path = r"C:\Projects\SIH\indian_ocean\1999\10\19991021_prof.nc"

ds=xr.open_dataset(file_path,engine="netcdf4")

# print(ds)

# print(ds.data_vars.keys())


temp=ds["TEMP"].isel(N_PROF=0)


# print(temp)
print(temp.values)



# pip install psycopg2-binary sqlalchemy xarray pandas



