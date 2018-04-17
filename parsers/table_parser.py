class TableParser():
    @staticmethod
    def parseTable(table):
        return {
            'id': table.id,
            'establishment_id': table.establishment_id,
            'status': table.status,
            'user_id': table.user_id,
            'number': table.number
        }

    @staticmethod
    def parseTables(tables):
        parsedTables = []
        for table in tables:
            parsedTables.append(TableParser.parseTable(table))
        return parsedTables
