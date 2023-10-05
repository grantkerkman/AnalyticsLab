Sub RunAllSheets()

    Dim ws As Worksheet
    For Each ws In ThisWorkbook.Worksheets
        
        ws.Activate
        Stonks
        
    Next ws

End Sub

Sub Stonks()

'Define variables and parameters
Dim volume As Double
Dim closing_price As Double
Dim opening_price As Double
Dim Summary_table_row As Integer
Dim Max_increase As Double
Dim Max_decrease As Double
Dim Max_volume As Double
lastrow = Cells(Rows.Count, 1).End(xlUp).Row

'Make the headers and static table values appear
cells(1,10).value = "Ticker"
cells(1,11).value = "Yearly Change"
cells(1,12).value = "Percent Change"
cells(1,13).value = "Total Volume"

cells(1,15).value = "Metric"
cells(2,15).value = "Greatest Percent Increase"
cells(3,15).value = "Greatest Percent Decrease"
cells(4,15).value = "Largest Volume"
cells(1,16).value = "Ticker"
cells(1,17).value = "Value"

'Start the counter at the beginning value and initialize values
Summary_table_row = 2
volume = 0
opening_price = Cells(2, 3).Value

'Iterating Functions
For i = 2 To lastrow

'Start volume traded Summation
volume = volume + Cells(i, 7).Value

    If Cells(i, 1).Value <> Cells(i + 1, 1).Value Then

        'Get the Ticker Information
        Cells(Summary_table_row, 10).Value = Cells(i, 1).Value
        Summary_table_row = Summary_table_row + 1

        'Get the Total Volume Traded
        Cells(Summary_table_row - 1, 13).Value = Cells(i, 7).Value
        volume = 0

        'Get Yearly Change and color cells according to logic green = positive and red = negative
        closing_price = Cells(i, 6).Value
        yearly_change = closing_price - opening_price
        change_percent = (yearly_change / opening_price)
        Cells(Summary_table_row - 1, 11).Value = yearly_change
        Cells(Summary_table_row - 1, 12).Value = Format(change_percent, "0.00%")
        opening_price = Cells(i + 1, 3).Value

            If Cells(Summary_table_row - 1, 11).Value > 0 Then
            Cells(Summary_table_row - 1, 11).Interior.ColorIndex = 4
            
            Else
            Cells(Summary_table_row - 1, 11).Interior.ColorIndex = 3
           
           End If
           
    End If

Next i

'Find the Greatest % Increase, Decrease, and Max Volume
Max_increase = WorksheetFunction.Max(Range("L2:L" & lastrow))
Max_increase_ticker = Cells(Application.Match(Max_increase, Range("L2:L" & lastrow), 0) + 1, 10).Value
Cells(2, 16) = Max_increase_ticker
Cells(2, 17) = Format(Max_increase, "0.00%")

Max_decrease = WorksheetFunction.Min(Range("L2:L" & lastrow))
Max_decrease_ticker = Cells(Application.Match(Max_decrease, Range("L2:L" & lastrow), 0) + 1, 10).Value
Cells(3, 16) = Max_decrease_ticker
Cells(3, 17) = Format(Max_decrease, "0.00%")

Max_volume = WorksheetFunction.Max(Range("M2:M" & lastrow))
Max_volume_ticker = Cells(Application.Match(Max_volume, Range("M2:M" & lastrow), 0) + 1, 10).Value
Cells(4, 16) = Max_volume_ticker
Cells(4, 17) = Max_volume

End Sub