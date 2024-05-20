# Sofi Spreadsheet Parser

This simple Flask application allows you to import a csv of your Sofi collection (using `sspreadsheet`). It will then
parse the csv and display the data in a table. You can choose which columns to display and sort the data by any column.
You also have the option to filter the data with certain filters and get the associated card codes.

## Installation
First, clone the repository:
```bash
git clone
cd sofi-spreadsheet-parser
```

Then, install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
To run the application, simply run the following command:

```bash
python app.py
```