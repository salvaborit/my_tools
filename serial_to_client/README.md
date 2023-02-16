# Serial-to-Client

Serial-to-Client is a command-line tool that takes a serial code input and displays the corresponding client name from a spreadsheet in CSV format. The tool expects a `control.csv` file in the same directory with column headings `terminal`, `client`, and `serial`. The tool also replaces certain symbols in the input serial code with digits for proper comparison with the data in the spreadsheet. When the input serial code is found in the spreadsheet, the client name is printed on screen. If the serial code is not found, the tool displays "NOT FOUND".
