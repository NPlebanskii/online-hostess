class EstablishmentParser():
    @staticmethod
    def parseEstablishments(establishments):
        parsedEstablishments = []
        for establishment in establishments:
            parsedEstablishments.append(EstablishmentParser.
                                        parseEstablishment(establishment))
        return parsedEstablishments

    @staticmethod
    def parseEstablishment(establishment):
        openTime = None
        endTime = None
        if establishment.open_time is not None:
            openTime = establishment.open_time.isoformat(
                timespec='minutes')
        if establishment.end_time is not None:
            endTime = establishment.end_time.isoformat(
                timespec='minutes')
        return {
            'id': establishment.id,
            'name': establishment.name,
            'description': establishment.description,
            'location': establishment.location,
            'open_time': openTime,
            'end_time': endTime,
            'img_url': establishment.img_url
        }
