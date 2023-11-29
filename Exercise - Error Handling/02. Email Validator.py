import re
class NameTooShortError(Exception):
    def __init__(self, message):
        self.message = message


class MustContainAtSymbolError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidDomainError(Exception):
    def __init__(self, message):
        self.message = message


def validate(string):
    symbol = "@"
    if symbol not in string:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, domain = string.split("@")
        extension = re.findall(r"\.[a-z]{1,}", domain)
        allowed_extensions = ['.com', '.bg', '.net', '.org']
        if len(name) < 5:
            raise NameTooShortError("Name must be more than 4 characters")
        if extension[0] not in allowed_extensions:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            print("Email is valid")

while True:

    email = input()

    if email == "End":
        break
    try:
        validate(email)
    except NameTooShortError as error:
        raise error
    except MustContainAtSymbolError as error:
        raise error
    except InvalidDomainError as error:
        raise error
