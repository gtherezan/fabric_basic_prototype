CREATE TABLE dbo.Calendar
(
    DateValue DATE,
    Year INT,
    StartOfYear VARCHAR(20),
    EndOfYear VARCHAR(20),
    Month INT,
    StartOfMonth VARCHAR(20),
    EndOfMonth VARCHAR(20),
    DaysInMonth INT,
    Day INT,
    DayName VARCHAR(20),
    DayOfWeek INT,
    MonthName VARCHAR(20),
    Quarter INT,
    StartOfQuarter VARCHAR(20),
    EndOfQuarter VARCHAR(20)
);

DECLARE @StartDate DATE = '2023-01-01';
DECLARE @EndDate DATE = '2023-01-31';
WHILE @StartDate <= @EndDate
BEGIN
  INSERT INTO dbo.Calendar (
    DateValue, Year, StartOfYear, EndOfYear,
    Month, StartOfMonth, EndOfMonth, DaysInMonth, MonthName,
    Day, DayName, DayOfWeek,
    Quarter, StartOfQuarter, EndOfQuarter
  )
  VALUES (
    @StartDate,
    YEAR(@StartDate), -- Year
    DATEFROMPARTS(YEAR(@StartDate), 1, 1), -- StartOfYear
    DATEFROMPARTS(YEAR(@StartDate), 12, 31), -- EndOfYear
    MONTH(@StartDate), -- Month
    DATEFROMPARTS(YEAR(@StartDate), MONTH(@StartDate), 1), -- StartOfMonth
    EOMONTH(@StartDate), -- EndOfMonth
    DAY(EOMONTH(@StartDate)), -- DaysInMonth
    DATENAME(MONTH, @StartDate), -- MonthName
    DAY(@StartDate), -- Day
    DATENAME(WEEKDAY, @StartDate), -- DayName
    (DATEPART(weekday, @StartDate) + 5) % 7 + 1, -- DayOfWeek
    DATEPART(QUARTER, @StartDate), -- Quarter
    CAST(DATEADD(QUARTER, DATEDIFF(QUARTER, 0, @StartDate), 0) AS DATE), -- StartOfQuarter
    EOMONTH(DATEFROMPARTS(YEAR(@StartDate), DATEPART(QUARTER, @StartDate) * 3, 1)) -- EndOfQuarter
  );
 
  SET @StartDate = DATEADD(day, 1, @StartDate);
END;