# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1de3ddf0-d4ac-4b8a-ad80-93dc2b519092",
# META       "default_lakehouse_name": "Bronze_Lakehouse",
# META       "default_lakehouse_workspace_id": "9588b3b5-dfbe-4536-b0b1-395a2038b9d2",
# META       "known_lakehouses": [
# META         {
# META           "id": "1de3ddf0-d4ac-4b8a-ad80-93dc2b519092"
# META         },
# META         {
# META           "id": "d1c8878a-fcf4-447f-99b6-a2ce2a618034"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

## Read Bronze UFS Table
df = spark.read.format("delta") \
        .load("abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/1de3ddf0-d4ac-4b8a-ad80-93dc2b519092/Tables/UFS")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

## UFS data transformations

# Drop unused columns
df = df.drop("AtInat_uf")   \
        .drop("UsrCad_uf")  \
        .drop("DataCad_uf")

# Rename columns
df = df.withColumnRenamed("Desc_uf", "UF")              \
        .withColumnRenamed("codIBGE_uf", "UF_COD_IBGE") \
        .withColumnRenamed("Nome_uf", "ESTADO")         \
        .withColumnRenamed("CodNacao_uf", "COD_PAIS")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

## Write table to Silver
df.write.format("delta")            \
    .mode("overwrite")              \
    .option("mergeSchema", "true")  \
    .save("abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/d1c8878a-fcf4-447f-99b6-a2ce2a618034/Tables/UFS")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
