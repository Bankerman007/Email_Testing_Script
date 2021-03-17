"""Needed tools"""
import requests

class ClientEmail:
    """Email class information"""
    def __init__ (self, last_name, first_name,
                first_initial_last_name,
                last_name_first_initial, domain_name):

        self.last_name = last_name
        self.first_name = first_name
        self.first_int = first_initial_last_name
        self.last_initial = last_name_first_initial
        self.domain = domain_name

    def check_first_initial(self):
        """api checking first initial"""
        email_address = self.first_int + self.last_name + self.domain
        response = requests.get("https://isitarealemail.com/api/email/validate",
    params = {'email': email_address})

        status = response.json()['status']
        if status == "valid":
            print("email is valid")
        elif status == "invalid":
            print("email is invalid")
        else:
            print("email was unknown")

    def check_first_name_only(self):
        """api checking first name"""
        email_address = self.first_name + self.domain
        response = requests.get("https://isitarealemail.com/api/email/validate",
    params = {'email': email_address})

        status = response.json()['status']
        if status == "valid":
            print("email is valid")
        elif status == "invalid":
            print("email is invalid")
        else:
            print("email was unknown")

    def check_last_initial(self):
        """api checking last initial"""
        email_address = self.first_name + self.last_initial + self.domain
        response = requests.get("https://isitarealemail.com/api/email/validate",
    params = {'email': email_address})

        status = response.json()['status']
        if status == "valid":
            print("email is valid")
        elif status == "invalid":
            print("email is invalid")
        else:
            print("email was unknown")

name = ClientEmail("carr","brad", "c", "b", "@wirelineinc.com")

ClientEmail.check_first_initial(name)
ClientEmail.check_first_name_only(name)
ClientEmail.check_last_initial(name)
