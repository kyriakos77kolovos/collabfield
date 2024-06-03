import re

def extract_sql_from_log(log_file, output_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    sql_statements = []
    sql_pattern = re.compile(r'(INSERT INTO|CREATE TABLE|ALTER TABLE|UPDATE|DELETE FROM).*;')

    for line in lines:
        match = sql_pattern.search(line)
        if match:
            sql_statements.append(match.group())

    with open(output_file, 'w') as file:
        for statement in sql_statements:
            file.write(statement + '\n')

# Extract SQL from development.log and test.log
extract_sql_from_log('development.log', 'recreate_db_development.sql')
extract_sql_from_log('test.log', 'recreate_db_test.sql')
