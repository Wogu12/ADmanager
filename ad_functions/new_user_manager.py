from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer
from ad_functions.ad_connector_base_class import AdConnectorBaseClass

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
    
    def create_user(self, username, password, ou, group_dns):
        _full_ou = self._ous_dict.get(ou, None)
        _ou = ADContainer.from_dn(_full_ou)
        user = None

        try:
            user = aduser.ADUser.create(username, _ou, password=password)
            print('DODANO NOWEGO UZYTKOWNIKA')
            for group_dn in group_dns:
                group = adgroup.from_dn(group_dn)
                group.add_member(user)
        except Exception as e:
            print(f'ERROR: {e}')

        return user


def main():
    print('test')
    test = NewUserManager()
    ous = test.ous_dict
    print(ous)

    

if __name__ == "__main__":
    main()
    pass
