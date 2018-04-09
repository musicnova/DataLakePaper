"""PySpark module"""
from pyspark.sql import SparkSession
from pyspark import sql
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, TimestampType, IntegerType
from pyspark.sql.functions import unix_timestamp, to_timestamp, col
from pyspark.sql.functions import udf
import re

def get_arr_udf():
  return udf(lambda txt: '' if txt is None else
    ' '.join([re.sub(r"[^a-zа-яё]", "_",
    (txt[i-1] if i - 1 >= 0 else '_').lower() + 
     txt[i].lower() + (txt[i+1] if i + 1 <= len(txt) - 1 else '-').lower())
    for i in range(0, len(txt))]), StringType())
      key_udf = udf(lambda txt: '' if txt is None or len(txt)
      else txt[0].lower(), StringType())

def wfunc(a, b):
    x = set(a.split(' '))
    y = set(b.split(' '))
    sz = len(x.intersection(y))
    szx = len(x)
    szy = len(y)
    return 0.0 if szx + szy == 0 else 1.0 * sz / (szx + szy) 

def get_weight_udf():
    udf(lambda a, b: wfunc(a, b), DoubleType())
 
def create_project():
    print("ok")

if __name__ == "__main__":
    import sys
    create_project()
