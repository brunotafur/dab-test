from pyspark.sql.functions import col

def filter_func(df):
    df2 = df.where(col("trip_distance") < 2)
    return df2