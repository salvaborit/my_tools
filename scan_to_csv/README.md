# Scan-to-CSV

Scan-to-CSV is a command-line tool that allows you to create a CSV file by entering row names and values. The tool prompts you to enter a file name (without extension) and the row names separated by spaces. You can then enter values for each row, which are written to the CSV file when you confirm them. When you are finished, simply enter 'done' as the value for any row to exit the program.

If a file with the same name already exists, the tool prompts you to confirm overwriting the file. The tool also validates each row value before adding it to the CSV file, allowing you to confirm or reject the value. The tool also provides feedback after each row is added, indicating whether the value was added successfully or not.

To run the tool, simply execute the script in a terminal with Python 3.
