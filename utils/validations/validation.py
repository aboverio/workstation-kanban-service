class Validation:
    @staticmethod
    def not_empty(val, field):
        if len(val) <= 0 or val is None:
            return {
                field: f'{field} cannot be empty!'
            }

    @staticmethod
    def username(val, field):
        if len(val) <= 0 or val is None:
            return {
                field: f'{field} cannot be empty!'
            }
        elif len(val) < 6:
            return {
                field: f'{field} must be at least 6 characters in length!'
            }
