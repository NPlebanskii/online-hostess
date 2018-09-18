class EstablishmentParser():
    @staticmethod
    def parse_establishments(establishments):
        parsed_establishments = []
        try:
            for establishment in establishments:
                parsed_establishments.append(
                    EstablishmentParser.parse_establishment(establishment))
        finally:
            return parsed_establishments

    @staticmethod
    def parse_establishment(establishment):
        from parsers.table_parser import TableParser
        try:
            openTime = establishment.open_time.isoformat(
                timespec='minutes')
        except Exception:
            openTime = None
        try:
            endTime = establishment.end_time.isoformat(
                timespec='minutes')
        except Exception:
            endTime = None
        tables = []
        try:
            for table in establishment.tables:
                tables.append(TableParser.parse_table(table))
        finally:
            return {
                'id': establishment.id,
                'name': establishment.name,
                'description': establishment.description,
                'location': establishment.location,
                'open_time': openTime,
                'end_time': endTime,
                'img_url': establishment.img_url,
                'tables': tables
            }
