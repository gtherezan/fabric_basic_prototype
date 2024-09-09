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
# META           "id": "e7f67786-1874-4a84-b8b8-ea2bbc2d2e21"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ## Notebook para tabela de Vendas (Staging -> Bronze)

# CELL ********************

import datetime
from pyspark.sql.functions import lit

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# PARAMETERS CELL ********************

## Lakehouse ABFS Filepaths
stagingLakehouse =  "abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/e7f67786-1874-4a84-b8b8-ea2bbc2d2e21/"
bronzeLakehouse =   "abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/1de3ddf0-d4ac-4b8a-ad80-93dc2b519092/"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Select the current day Staging folder
stagingFilePath = stagingLakehouse + "Files/"
stagingFileList = notebookutils.fs.ls(stagingFilePath)
stagingFolderList = [i for i in stagingFileList if i.isDir]

for folder in stagingFolderList:
    latestStagingFolder = ""
    currentDay = datetime.date.today().strftime("%Y-%d-%m")
    if folder.name == currentDay: latestStagingFolder = folder.name

stagingFilesCurrDayABFS = stagingFilePath + latestStagingFolder

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def readAvroFile(avroFile):
    df = spark.read.format("avro").load(avroFile)
    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def addProcessedTimeStamp(df):
    currentDateTimeUTC = datetime.datetime.utcnow().strftime("%Y-%d-%m %H:%M")
    df = df.withColumn("processedDateTimeUTC", lit(currentDateTimeUTC))
    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def writeToBronzeLakehouse(df, name):
    bronzeTablePath = bronzeLakehouse + "Tables/"
    bronzeTableFullPathName = bronzeTablePath + name

    df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronzeTableFullPathName)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

for file in notebookutils.fs.ls(stagingFilesCurrDayABFS):
    filePath = file.path
    fileName = file.name.replace(".avro", "")

    df = readAvroFile(file.path)
    df = addProcessedTimeStamp(df)

    writeToBronzeLakehouse(df, fileName)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
