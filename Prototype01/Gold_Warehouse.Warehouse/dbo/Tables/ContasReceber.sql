CREATE TABLE [dbo].[ContasReceber] (

	[NumParcelas] int NULL, 
	[Tipo] varchar(8000) NULL, 
	[NumParcelasGeral] int NULL, 
	[Empresa] int NULL, 
	[Obra] varchar(8000) NULL, 
	[NumVendedor] int NULL, 
	[Data] varchar(8000) NULL, 
	[Valor] float NULL, 
	[Status] int NULL, 
	[EmBanco] int NULL, 
	[Origem] int NULL, 
	[Cliente] int NULL, 
	[DataProrrogacao] varchar(8000) NULL, 
	[JurosParcelas] float NULL, 
	[ComoParcelas] varchar(8000) NULL, 
	[IndiceReajuste] varchar(8000) NULL, 
	[AmortizacaoParcelas] int NULL, 
	[InicioFimParcelas] int NULL, 
	[DataIndiceParcelas] varchar(8000) NULL, 
	[DataJurosParcelas] varchar(8000) NULL, 
	[Capital] varchar(8000) NULL, 
	[TotalParcelas] int NULL, 
	[DataParcelas] varchar(8000) NULL, 
	[ValorResiduo] float NULL, 
	[GrupoIndice] int NULL, 
	[GrupoParcelas] int NULL, 
	[StatusCobranca] varchar(8000) NULL, 
	[CapitalCorrecaoAtraso] varchar(8000) NULL, 
	[CapitalJuros] varchar(8000) NULL, 
	[CapitalCorrecao] varchar(8000) NULL, 
	[CapitalMulta] varchar(8000) NULL, 
	[CapitalJurosAtraso] varchar(8000) NULL, 
	[CapitalAcrescimo] varchar(8000) NULL, 
	[CapitalDesconto] varchar(8000) NULL, 
	[Anexos] int NULL, 
	[CapitalDescontoAntecipado] varchar(8000) NULL, 
	[CapitalTaxaBoleto] varchar(8000) NULL, 
	[ValorTaxaBoleto] float NULL, 
	[NumContrato] int NULL, 
	[OrigemCusto] int NULL, 
	[CobrarMulta] int NULL, 
	[CobrarJurosAtraso] int NULL, 
	[CobrarTaxaAdm] int NULL, 
	[CobrarImposto] int NULL, 
	[CobrarCorrecao] int NULL, 
	[CobrarCPMF] int NULL, 
	[RepassarLocador] int NULL, 
	[ValorDescontoCusto] float NULL, 
	[CapitalDescontoCusto] varchar(8000) NULL, 
	[ValorDescontoImposto] float NULL, 
	[TotalParcelasGrupo] int NULL, 
	[DataCadastro] varchar(8000) NULL, 
	[DataJurosComJuros] int NULL, 
	[Observacoes] varchar(8000) NULL, 
	[DataInicioPeriodoAluguel] varchar(8000) NULL, 
	[CapitalRepasse] varchar(8000) NULL, 
	[NumeroBanco] int NULL, 
	[ContaBanco] varchar(8000) NULL, 
	[NumPCB] int NULL, 
	[DataSegundaJuros] varchar(8000) NULL, 
	[PorcentagemSegundaJuros] float NULL, 
	[CarenciaAtraso] int NULL, 
	[CarenciaAtrasoCorrecao] int NULL, 
	[CobrarJurosProRata] int NULL, 
	[TipoSeguro] int NULL, 
	[CobrarJurosProRataPrimeiroMes] bit NULL, 
	[CapitalDescontoCondicional] varchar(8000) NULL, 
	[NumMDRPreferencial] int NULL, 
	[processedDateTimeUTC] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[ContasReceber] ADD CONSTRAINT UQ_a461ed88_66e4_48de_85bf_d0a8e658beef unique NONCLUSTERED ([Anexos]);