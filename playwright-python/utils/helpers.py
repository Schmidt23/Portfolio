def get_user_row(table, searchterm):
    return table.get_by_role("row").filter(
        has_text=searchterm
    )

def get_table_header(table, searchterm):
    return table.get_by_role("columnheader", name=searchterm)