from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession
from dab_test import main
from transformation_functions import transform
from pyspark.sql import Row
from datetime import datetime, date

'''spark = DatabricksSession.builder.remote(
  host       = f"",
  token      = "",
  cluster_id = ""
).getOrCreate()'''
spark = SparkSession.builder.getOrCreate()

def test_main():
    df = spark.createDataFrame([
        Row(tpep_pickup_datetime=date(2000, 1, 1), tpep_dropoff_datetime=date(2000, 1, 1), trip_distance=4.0, fare_amount=15.0, pickup_zip=1, dropoff_zip=2),
        Row(tpep_pickup_datetime=date(2000, 1, 1), tpep_dropoff_datetime=date(2000, 1, 1), trip_distance=1.1, fare_amount=15.0, pickup_zip=1, dropoff_zip=2),
        Row(tpep_pickup_datetime=date(2000, 1, 1), tpep_dropoff_datetime=date(2000, 1, 1), trip_distance=1.0, fare_amount=15.0, pickup_zip=1, dropoff_zip=2),
        Row(tpep_pickup_datetime=date(2000, 1, 1), tpep_dropoff_datetime=date(2000, 1, 1), trip_distance=5.0, fare_amount=15.0, pickup_zip=1, dropoff_zip=2),
    ])
    #df = spark.read.table("samples.nyctaxi.trips")

    df = transform.filter_func(df)
    max_value = df.agg({"trip_distance": "max"}).collect()[0][0]
    assert max_value < 2, f"Not all values in column trip_distance are less than 2. Max value found: {max_value}"


