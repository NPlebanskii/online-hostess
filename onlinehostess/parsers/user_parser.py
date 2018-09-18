class UserParser():
    @staticmethod
    def parse_user(user):
        return {
            'user_id': user.id,
            'email': user.email,
            'admin': user.admin,
            'registered_on': user.registered_on.replace(microsecond=0).
            isoformat(),
            'first_name': user.first_name,
            'last_name': user.last_name
        }
