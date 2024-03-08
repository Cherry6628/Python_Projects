class InvalidIndexError(Exception):
    def __init__(self, index):
        """Invalid Index - Error"""
        self.index = index
        super().__init__(f'Unable to Find an Element at Index {index}')


class InvalidKeyError(Exception):
    def __init__(self, key):
        """Invalid Key - Error"""
        self.key = key
        super().__init__(f'Unable to find the key {key} in the Dictionary')


class SetItemError(Exception):
    def __init__(self):
        """Unable to Set Item - Error"""
        super().__init__(f'Unable to Add/Append/Set the provided in the corresponding Data\nThis may be due to Invalid \
Index')


class Error(Exception):
    def __init__(self, message=""):
        super().__init__(message)