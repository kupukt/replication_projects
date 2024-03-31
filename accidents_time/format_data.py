# %%
import polars as pl
import pins
# %%
# dat = pl.read_csv("Motor_Vehicle_Collisions_-_Crashes_20240124.csv")\
#     .with_columns(
#         pl.col("CRASH DATE").str.to_date("%m/%d/%Y").alias("date"),
#         pl.col("CRASH TIME").str.to_time("%H:%M").alias("time"),
#         pl.concat_str(["CRASH DATE","CRASH TIME"], separator=" ")\
#             .str.to_datetime("%m/%d/%Y %H:%M").alias("date_time"))

# dat.write_parquet("ny_crashes.parquet", compression="zstd", compression_level=15)
# %%
dat = pl.read_parquet("ny_crashes.parquet")
# %%
# Now we want to create two visuals: the number of chrashes per hour and one that shows the number of injuries per day

#%%
boroughdat = dat.fill_null("Unknown")
#%%
rates = boroughdat\
.with_columns(
    pl.col("date_time").dt.truncate("1h").alias("hour_floor"))\
    .group_by("hour_floor", "BOROUGH")\
    .agg(
        pl.sum("NUMBER OF PERSONS INJURED").alias("injured_total"),
        pl.col("BOROUGH").count().alias("accident_count")
    )\
    

# %%
rates_day = boroughdat\
.with_columns(
    pl.col("date_time").dt.truncate("1d").alias("day_floor"))\
    .group_by("day_floor", "BOROUGH")\
    .agg(
        pl.sum("NUMBER OF PERSONS INJURED").alias("injured_total"),
        pl.col("BOROUGH").count().alias("accident_count")
    )\
    .with_columns(pl.col("day_floor").dt.weekday().alias("weekday"))
# %%
from lets_plot import *
LetsPlot.setup_html()

ggplot(rates_day.sort("weekday"), aes(x= "weekday", y = "accident_count")) + geom_boxplot() + facet_wrap(facets= "BOROUGH") + scale_x_discrete()


# %%

