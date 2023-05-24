import streamlit as st

def generate_create_table_sql(database_name, column_names, column_types):
    sql = f"CREATE DATABASE {database_name};\n\n"
    sql += f"USE {database_name};\n\n"
    sql += "CREATE TABLE your_table_name (\n"

    for i in range(len(column_names)):
        column_name = column_names[i]
        column_type = column_types[i]
        sql += f"    {column_name} {column_type},\n"

    sql = sql.rstrip(",\n") + "\n);"

    return sql

def main():
    st.title("Database Creation SQL Generator")
    st.write("Enter the details below to generate SQL code for creating a database.")

    # Database name input
    database_name = st.text_input("Enter the database name:")

    # Column details input
    num_columns = st.number_input("Enter the number of columns:", min_value=1, value=1, step=1)

    column_names = []
    column_types = []

    for i in range(num_columns):
        column_name = st.text_input(f"Enter the name for column {i+1}:")
        column_type = st.text_input(f"Enter the type for column {i+1}:")

        column_names.append(column_name)
        column_types.append(column_type)

    if st.button("Generate SQL"):
        sql = generate_create_table_sql(database_name, column_names, column_types)
        st.code(sql, language='sql')

    # Data insertion option
    st.write("Enter the data to be inserted into the table.")
    data_values = []

    for i in range(num_columns):
        column_data = st.text_input(f"Enter data for column '{column_names[i]}' (separated by commas):")
        column_values = [value.strip() for value in column_data.split(",")]
        data_values.append(column_values)

    if st.button("Insert Data"):
        if any(len(column_values) != len(data_values[0]) for column_values in data_values):
            st.warning("Number of values entered for each column is not consistent.")
        else:
            insert_sql = f"INSERT INTO %a ({', '.join(column_names)}) VALUES\n" %(database_name)

            for i in range(len(data_values[0])):
                row_values = [f"'{data_values[j][i]}'" for j in range(num_columns)]
                row_sql = f"({', '.join(row_values)}),\n" if i < len(data_values[0]) - 1 else f"({', '.join(row_values)});"
                insert_sql += row_sql

            st.code(insert_sql, language='sql')

if __name__ == "__main__":
    main()
