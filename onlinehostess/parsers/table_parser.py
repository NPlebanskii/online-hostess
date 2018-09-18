class TableParser():
    @staticmethod
    def parse_table(table):
        return {
            'id': table.id,
            'establishment_id': table.establishment_id,
            'status': table.status,
            'user_id': table.user_id,
            'number': table.number
        }

    @staticmethod
    def parse_tables(tables):
        parsedTables = []
        try:
            for table in tables:
                parsedTables.append(TableParser.parse_table(table))
        finally:
            return parsedTables
