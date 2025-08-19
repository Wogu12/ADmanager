import re

from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer
from ad_functions.ad_connector_base_class import AdConnectorBaseClass
from CTkMessagebox import CTkMessagebox

class NewUserManager(AdConnectorBaseClass):
    def __init__(self):
        super().__init__()
        self.ous_list = self.parse_ous()
        self._ous_dict = self.get_ous_dict()

    def parse_ous(self):
        _parsed_ous = []

        for item in self.raw_ous_list:
            _ou = item.split(',')[0]
            _ou = _ou[3:]
            _parsed_ous.append(_ou)

        return _parsed_ous
    
    def get_ous_dict(self):
        _dict = {}

        for item in self.raw_ous_list:
            _ou = item.split(',')[0]
            _ou = _ou[3:]
            _dict[_ou] = item

        return _dict
    
    def create_user(self, name, surname, job_title, mail, username, password, ou, group_dns):
        _full_ou = self._ous_dict.get(ou, None)
        _ou = ADContainer.from_dn(_full_ou)
        user = None

        try:
            user = aduser.ADUser.create(username,
                                        _ou,
                                        password=password,
                                        optional_attributes={"givenName": name,
                                                             "sn": surname,
                                                             "displayName": f"{name} {surname}",
                                                             "mail": mail,
                                                             "sAMAccountName": username,
                                                             "title": job_title,
                                                            }
                                        )
            for group_dn in group_dns:
                group = adgroup.from_dn(group_dn)
                group.add_member(user)                
        except Exception as e:
            _error_code = str(e).split(": ", 1)[0]
            e = re.sub(r'^[^:]+:\s*', '', str(e))
            if _error_code == '0x80071392':
                CTkMessagebox(title="Błąd", message=e)
            else:
                CTkMessagebox(title="Błąd", message=e)
                _user_to_delete = aduser.ADUser(distinguished_name=f'CN={username},{str(_full_ou)}')
                _user_to_delete.delete()

        return user


def main():
    print('test')
    test = NewUserManager()
    ous = test.ous_dict
    print(ous)

    

if __name__ == "__main__":
    main()
    pass
