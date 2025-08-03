from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer
# from pyad.pyadexceptions import InvalidObjectException

class AdConnectorBaseClass:
    def __init__(self):
        try:
            self._defaults = pyad.set_defaults()
        except Exception as e:
            raise(f'ERROR: {e}')
        self.ous_list = self.get_ous()

    def print_def(self):
        current_user = aduser.ADUser.from_cn("Wojciech Guja")
        # print(current_user)

    def get_ous(self):
        _ous = []
        query = adquery.ADQuery()
        query.execute_query(
            attributes=["distinguishedName"],
            where_clause="objectClass = 'organizationalUnit'"
        )

        for row in query.get_results():
            # print(row["distinguishedName"])
            if 'Domain Controllers' not in row["distinguishedName"]:
                _ous.append(row["distinguishedName"])

        return _ous
    
    def print_ous(self):
        print(self._ous_list)

    def create_user(self, username, password, ou_dn, group_dns):
        ou = ADContainer.from_dn(ou_dn)
        user = None
        try:
            user = aduser.ADUser.create(username, ou, password=password)
            print('DODANO NOWEGO UZYTKOWNIKA')
            for group_dn in group_dns:
                group = adgroup.from_dn(group_dn)
                group.add_member(user)
        except Exception as e:
            print(f'ERROR: {e}')

        print(user)

        return user


def main():
    print('test')
    test = AdConnectorBaseClass()
    ous = test.ous_list
    print(ous)
    # test.print_def()

    

if __name__ == "__main__":
    main()