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

silverLakehouse = "abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/d1c8878a-fcf4-447f-99b6-a2ce2a618034/Tables/"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Load ContasReceber table
df = spark.read.format("delta").load("abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/1de3ddf0-d4ac-4b8a-ad80-93dc2b519092/Tables/ContasReceberHist")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

renamedCols = {
    "NumVhist_prc": "NumHistorico",
    "NumParc_Prc": "NumParcelas",
    "Tipo_Prc": "Tipo",
    "NumParcGer_Prc": "NumParcelasGeral",
    "Empresa_prc": "Empresa",
    "Obra_Prc": "Obra",
    "NumVend_prc": "NumVendedor",
    "Data_Prc": "Data",
    "Valor_Prc": "Valor",
    "Status_Prc": "Status",
    "EmBanco_Prc": "EmBanco",
    "Origem_Prc": "Origem",
    "Cliente_Prc": "Cliente",
    "DataPror_Prc": "DataProrrogacao",
    "JurosParc_Prc": "JurosParcelas",
    "ComoParc_Prc": "ComoParcelas",
    "IdxReaj_Prc": "IndiceReajuste",
    "AmortParc_Prc": "AmortizacaoParcelas",
    "BegEndParc_Prc": "InicioFimParcelas",
    "DtIdxParc_Prc": "DataIndiceParcelas",
    "DtJurParc_Prc": "DataJurosParcelas",
    "Cap_Prc": "Capital",
    "TotParc_Prc": "TotalParcelas",
    "DtParc_Prc": "DataParcelas",
    "ValorResiduo_Prc": "ValorResiduo",
    "GrupoIdx_Prc": "GrupoIndice",
    "GrupoParc_Prc": "GrupoParcelas",
    "StatusCbr_Prc": "StatusCobranca",
    "CapCorrecaoAtr_Prc": "CapitalCorrecaoAtraso",
    "CapJuros_Prc": "CapitalJuros",
    "CapCorrecao_Prc": "CapitalCorrecao",
    "CapMulta_Prc": "CapitalMulta",
    "CapJurosAtr_Prc": "CapitalJurosAtraso",
    "CapAcrescimo_Prc": "CapitalAcrescimo",
    "CapDesconto_Prc": "CapitalDesconto",
    "Anexos_Prc": "Anexos",
    "CapDescontoAntec_Prc": "CapitalDescontoAntecipado",
    "CapTaxaBol_prc": "CapitalTaxaBoleto",
    "ValorTaxaBol_prc": "ValorTaxaBoleto",
    "NumCtp_prc": "NumContrato",
    "OrigemCusta_prc": "OrigemCusto",
    "CobrarMulta_prc": "CobrarMulta",
    "CobrarJurosAtr_prc": "CobrarJurosAtraso",
    "CobrarTxAdm_prc": "CobrarTaxaAdm",
    "CobrarImposto_prc": "CobrarImposto",
    "CobrarCorrecao_prc": "CobrarCorrecao",
    "CobrarCPMF_prc": "CobrarCPMF",
    "RepassarLocador_prc": "RepassarLocador",
    "ValDescontoCusta_prc": "ValorDescontoCusto",
    "CapDescontoCusta_prc": "CapitalDescontoCusto",
    "ValDescontoImposto_prc": "ValorDescontoImposto",
    "TotParcGrupo_prc": "TotalParcelasGrupo",
    "DataCad_Prc": "DataCadastro",
    "DtJurosComJuros_Prc": "DataJurosComJuros",
    "Obs_Prc": "Observacoes",
    "DataIniPeriodoAluguel_prc": "DataInicioPeriodoAluguel",
    "CapRepasse_Prc": "CapitalRepasse",
    "NumeroBanco_prc": "NumeroBanco",
    "ContaBanco_prc": "ContaBanco",
    "NumPcb_prc": "NumPCB",
    "DataSegJuros_prc": "DataSegundaJuros",
    "PorcSegJuros_prc": "PorcentagemSegundaJuros",
    "CarenciaAtraso_prc": "CarenciaAtraso",
    "CarenciaAtrasoCorrecao_prc": "CarenciaAtrasoCorrecao",
    "CobrarJurosProRata_prc": "CobrarJurosProRata",
    "TipoSeguro_prc": "TipoSeguro",
    "CobrarJurosProRataPrimeiroMes_prc": "CobrarJurosProRataPrimeiroMes",
    "CapDescontoCondicional_prc": "CapitalDescontoCondicional",
    "Renegociada_prc": "Renegociada",
    "NumMdrPreferencial_prc": "NumMDRPreferencial"
}

# Renomear as colunas
for old_name, new_name in renamedCols.items():
    df = df.withColumnRenamed(old_name, new_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Write to Silver lakehouse
df.write.format("delta").mode("overwrite").save(silverLakehouse + "ContasReceberHist")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
