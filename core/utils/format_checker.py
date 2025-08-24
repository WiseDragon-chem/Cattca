class FormatChecker:

    @staticmethod
    def is_valid_variable_name(variable_name: str) -> bool:
        if len(variable_name) == 0:
            return False
        if not variable_name[0].isalpha():
            return False
        for char in variable_name:
            if not char.isalnum():
                return False
        return True