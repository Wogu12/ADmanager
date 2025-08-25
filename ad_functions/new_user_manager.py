import re
from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer
from ad_functions.ad_connector_base_class import AdConnectorBaseClass
from CTkMessagebox import CTkMessagebox

class NewUserManager(AdConnectorBaseClass):
    def __init__(self):
        super().__init__()
        self.ous_list = self.get_list(self.raw_ous_list)
        self.ous_dict = self.get_dict(self.raw_ous_list)
        self.groups_list = self.get_list(self.raw_groups_list)
        self.groups_dict = self.get_dict(self.raw_groups_list)
        self.mapped_ous = self.get_mapped_dict(self.raw_ous_list)

    def get_list(self, raw_list):
        _list = []
        for item in raw_list:
            _value = item.split(',')[0]
            _value = _value[3:]
            _list.append(_value)

        return _list
    
    def get_dict(self, raw_list):
        _dict = {}

        for item in raw_list:
            _value = item.split(',')[0]
            _value = _value[3:]
            _dict[_value] = item

        return _dict
    
    def get_mapped_dict(self, raw_list):
        _dict = {}
        for item in raw_list:
            parts = [entry.replace("OU=", "") for entry in item.split(",") if entry.startswith("OU=")]
            label = "/".join(reversed(parts))
            _dict[label] = item
        return _dict

    def create_user(self, name, surname, job_title, mail, username, password, ou, groups):
        _full_ou = self.mapped_ous.get(ou, None)
        _ou = ADContainer.from_dn(_full_ou)
        user = None
        _given_groups_list = [g.strip() for g in groups.split(",") if g.strip()]

        try:
            user = aduser.ADUser.create(
                username,
                _ou,
                password=password,
                optional_attributes={
                    "givenName": name,
                    "sn": surname,
                    "displayName": f"{name} {surname}",
                    "mail": mail,
                    "sAMAccountName": username,
                    "title": job_title,
                }
            )
            
            for group in _given_groups_list:
                _full_group = self.groups_dict.get(group, None)
                user.add_to_group(adgroup.ADGroup.from_dn(_full_group))
        except Exception as e:
            print(e)
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
    ous = test.mapped_ous
    print(ous)

    

if __name__ == "__main__":
    # main()
    pass
