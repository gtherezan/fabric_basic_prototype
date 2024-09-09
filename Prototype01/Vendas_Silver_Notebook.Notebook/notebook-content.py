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
# META           "id": "1de3ddf0-d4ac-4b8a-ad80-93dc2b519092"
# META         },
# META         {
# META           "id": "d1c8878a-fcf4-447f-99b6-a2ce2a618034"
# META         },
# META         {
# META           "id": "e7f67786-1874-4a84-b8b8-ea2bbc2d2e21"
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
df = spark.read.format("delta").load("abfss://9588b3b5-dfbe-4536-b0b1-395a2038b9d2@onelake.dfs.fabric.microsoft.com/1de3ddf0-d4ac-4b8a-ad80-93dc2b519092/Tables/Vendas")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

renamedCols = {
    "Empresa_ven": "Empresa",
    "Obra_Ven": "Obra",
    "Num_Ven": "Numero",
    "Contrato_Ven": "Contrato",
    "Vendedor_Ven": "Vendedor",
    "Cliente_Ven": "Cliente",
    "ValorTot_Ven": "ValorTotal",
    "Juros_Ven": "Juros",
    "Multa_Ven": "Multa",
    "Desconto_Ven": "Desconto",
    "User_Ven": "Usuario",
    "IntExt_Ven": "InternoExterno",
    "Data_Ven": "Data",
    "Status_Ven": "Status",
    "UserStatus_Ven": "UsuarioStatus",
    "Acrescimo_Ven": "Acrescimo",
    "PlanoIndexador_Ven": "PlanoIndexador",
    "JurContrato_ven": "JurosContrato",
    "Adiantamento_ven": "Adiantamento",
    "StatusEscritura_Ven": "StatusEscritura",
    "StatusCobranca_Ven": "StatusCobranca",
    "VlrCorretagem_Ven": "ValorCorretagem",
    "VlrLiberarCorretor_Ven": "ValorLiberarCorretor",
    "ReajusteAnual_Ven": "ReajusteAnual",
    "GerarResiduo_Ven": "GerarResiduo",
    "CarenciaAtraso_Ven": "CarenciaAtraso",
    "RetroagirIdx_Ven": "RetroagirIndice",
    "DataBaseResiduo_Ven": "DataBaseResiduo",
    "CorrecaoAtr_Ven": "CorrecaoAtraso",
    "CorrecaoProRata_Ven": "CorrecaoProRata",
    "Anexos_ven": "Anexos",
    "DataCessao_Ven": "DataCessao",
    "DataCancel_Ven": "DataCancelamento",
    "CodDvg_Ven": "CodigoDVG",
    "NumFin_Ven": "NumeroFinanciamento",
    "AniversarioContr_Ven": "AniversarioContrato",
    "CobrarTaxaBol_Ven": "CobrarTaxaBoleto",
    "DataCad_Ven": "DataCadastro",
    "AlmoxCentral_Ven": "AlmoxarifadoCentral",
    "ObraFiscal_Ven": "ObraFiscal",
    "TipoVenda_Ven": "TipoVenda",
    "DiaRepasse_Ven": "DiaRepasse",
    "ValProvisaoCurto_Ven": "ValorProvisaoCurtoPrazo",
    "ValProvisaoLongo_Ven": "ValorProvisaoLongoPrazo",
    "CapProvisaoCurto_Ven": "CapitalProvisaoCurtoPrazo",
    "CapProvisaoLongo_Ven": "CapitalProvisaoLongoPrazo",
    "CarenciaAtrasoCorrecao_ven": "CarenciaAtrasoCorrecao",
    "AntecipaCorrecao_ven": "AnteciparCorrecao",
    "CobrarJurosRecPosChave_ven": "CobrarJurosRecebimentoPosChave",
    "DataIniContrato_Ven": "DataInicioContrato",
    "DataFimContrato_Ven": "DataFimContrato",
    "TipoFianca_ven": "TipoFianca",
    "Txt1Fianca_ven": "Texto1Fianca",
    "Txt2Fianca_ven": "Texto2Fianca",
    "Txt3Fianca_ven": "Texto3Fianca",
    "DataFianca_ven": "DataFianca",
    "ValFianca_ven": "ValorFianca",
    "NomeSegIncendio_ven": "NomeSeguradoraIncendio",
    "ApoliceSegIncendio_ven": "ApoliceSeguradoraIncendio",
    "ValSegIncendio_ven": "ValorSeguradoraIncendio",
    "DataVencSegIncendio_ven": "DataVencimentoSeguradoraIncendio",
    "MultaFracionada_ven": "MultaFracionada",
    "AntecipaJurosLinear_ven": "AnteciparJurosLinear",
    "ValDescontoImposto_ven": "ValorDescontoImposto",
    "PeriodoMesReajuste_ven": "PeriodoMesReajuste",
    "HistLanc_ven": "HistoricoLancamento",
    "HistLancRec_ven": "HistoricoLancamentoRecebimento",
    "HistLancJurosCorrecao_ven": "HistoricoLancamentoJurosCorrecao",
    "ZerarCorrecaoNegativa_ven": "ZerarCorrecaoNegativa",
    "JuroAtrasoMensal_ven": "JurosAtrasoMensal",
    "CorrecaoCrescente_ven": "CorrecaoCrescente",
    "SPEDPisCofins_ven": "SPEDPisCofins",
    "CorrecaoAtrasoPerson_ven": "CorrecaoAtrasoPersonalizada",
    "ContratoCEF_ven": "ContratoCEF",
    "Atividade_ven": "Atividade",
    "ValProvisaoCurtoBaixa_ven": "ValorProvisaoCurtoPrazoBaixa",
    "ValProvisaoLongoBaixa_ven": "ValorProvisaoLongoPrazoBaixa",
    "ValProvisaoCurtoCessao_ven": "ValorProvisaoCurtoPrazoCessao",
    "ValProvisaoLongoCessao_ven": "ValorProvisaoLongoPrazoCessao",
    "CapProvisaoCurtoBaixa_ven": "CapitalProvisaoCurtoPrazoBaixa",
    "CapProvisaoLongoBaixa_ven": "CapitalProvisaoLongoPrazoBaixa",
    "HistLancBaixaProvisao_ven": "HistoricoLancamentoBaixaProvisao",
    "Validador_ven": "Validador",
    "JurosAnual_ven": "JurosAnual",
    "PeriodoMesJuros_ven": "PeriodoMesJuros",
    "ValPrestServico_ven": "ValorPrestacaoServico",
    "AnteciparCorrecaoProxPer_ven": "AnteciparCorrecaoProximoPeriodo",
    "RET_ven": "RET",
    "NumRet_ven": "NumeroRET",
    "NumCsf_ven": "NumeroCSF",
    "UtilizarDescUltimaParc_ven": "UtilizarDescontoUltimaParcela"
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
df.write.format("delta").mode("overwrite").save(silverLakehouse + "Vendas")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
