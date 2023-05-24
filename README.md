# Database Creation SQL Generator

#### This project is a simple tool developed using Python and Streamlit to generate SQL code for creating a database. It allows users to define the database name, column names, and column types, and generates the corresponding SQL code for creating the database and table.
# Features

    Database Creation: The tool prompts the user to enter the desired database name.
    Column Details: Users can input the number of columns they want to create and provide the name and type for each column.
    Generate SQL: Upon clicking the "Generate SQL" button, the tool generates the SQL code for creating the specified database and table. The generated SQL code includes the CREATE DATABASE, USE, and CREATE TABLE statements.
    Data Insertion: Users can enter data to be inserted into the table. For each column, the user can input data separated by commas. The tool validates that the number of values entered for each column is consistent.
    Generate Insert SQL: By clicking the "Insert Data" button, the tool generates the SQL code for inserting the provided data into the table. The generated SQL code includes the INSERT INTO statement and the corresponding values.
    
![Screenshot 2023-05-24 at 18-14-36 database · Streamlit](https://github.com/faramarzzareian/database_code_generator/assets/5400662/0324fc99-0448-4058-be7f-b95aa5b291dc)

# Usage

    Run the script in a Python environment.
    The Streamlit application will launch in a browser window.
    Enter the desired database name in the text input.
    Specify the number of columns to create using the number input field.
    For each column, provide the name and type in the respective text inputs.
    Click the "Generate SQL" button to generate the SQL code for creating the database and table.
    Enter data for each column separated by commas.
    Click the "Insert Data" button to generate the SQL code for inserting the data into the table.
    The generated SQL code will be displayed, which you can copy and use in your preferred database management system.

###### Please note that the generated SQL code assumes the database name will be used as the table name. Modify the CREATE TABLE statement if you wish to use a different table name.

####### Feel free to modify and enhance this tool to suit your specific requirements. Happy coding!
