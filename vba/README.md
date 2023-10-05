# Stock Analysis Tool

This is a simple VBA macro-enabled Excel workbook that allows you to analyze stock data for multiple ticker symbols. The tool calculates various metrics, such as yearly change, percent change, and total volume traded, and highlights positive and negative changes in the data. Additionally, it identifies the stocks with the greatest percent increase, greatest percent decrease, and largest volume.

## Usage

1. **Open the Excel Workbook:** Open the Excel workbook containing your stock data.

2. **Enable Macros:** Ensure that macros are enabled in Excel. You can do this by going to "File" > "Options" > "Trust Center" > "Trust Center Settings" > "Macro Settings" and selecting "Enable all macros."

3. **Run the Analysis:**

    - Press `ALT + F8` to open the "Macro" dialog box.
    - Select `RunAllSheets` and click "Run."

4. **Review the Results:**

    - The tool will populate a summary table with the following columns:
        - Ticker: Ticker symbol for each stock.
        - Yearly Change: The change in stock price over the year.
        - Percent Change: The percentage change in stock price over the year.
        - Total Volume: The total trading volume for the stock.

    - The tool will also highlight the Yearly Change column in green for positive changes and in red for negative changes.

    - Below the summary table, you will find additional information about the stocks with the greatest percent increase, greatest percent decrease, and largest volume.

## How It Works

The tool works by iterating through each worksheet in the Excel workbook and running the `Stonks` subroutine for each sheet. Here's an overview of how the `Stonks` subroutine operates:

- It defines variables and parameters to store and calculate various metrics.

- It initializes the summary table with headers and initializes variables.

- It iterates through the rows of the worksheet, calculating the total volume traded, yearly change, and percent change for each stock.

- It populates the summary table with the calculated values and formats the Yearly Change column based on whether it's positive or negative.

- Finally, it identifies the stocks with the greatest percent increase, greatest percent decrease, and largest volume and displays them below the summary table.

## Customization

You can customize this tool to suit your specific needs. Here are some potential modifications:

- **Additional Metrics:** You can add more metrics to the summary table by modifying the headers and calculations in the `Stonks` subroutine.

- **Date Range:** If your data spans a different time range, you can adjust the logic for yearly change accordingly.

- **Color Coding:** You can customize the colors used to highlight positive and negative yearly changes.

## License

This tool is provided under the MIT License. Feel free to use, modify, and distribute it according to your needs.

---

*Note: This README provides an overview of the stock analysis tool. Please refer to the Excel workbook and VBA code for the complete functionality and implementation details.*
