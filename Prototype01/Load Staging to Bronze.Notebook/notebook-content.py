# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e7f67786-1874-4a84-b8b8-ea2bbc2d2e21",
# META       "default_lakehouse_name": "Staging_Lakehouse",
# META       "default_lakehouse_workspace_id": "9588b3b5-dfbe-4536-b0b1-395a2038b9d2",
# META       "known_lakehouses": [
# META         {
# META           "id": "e7f67786-1874-4a84-b8b8-ea2bbc2d2e21"
# META         },
# META         {
# META           "id": "1de3ddf0-d4ac-4b8a-ad80-93dc2b519092"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

## Read from Staging Area
df = spark.read.format("avro")  \
    .option("header","true")    \
    .load("abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/e7f67786-1874-4a84-b8b8-ea2bbc2d2e21/Files/UFS.avro")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

## Write to RAW as Table
df.write.format("delta").mode("overwrite").option("mergeSchema", "true").save("abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/1de3ddf0-d4ac-4b8a-ad80-93dc2b519092/Tables/UFS")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
