from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer

class AdConnectorBaseClass:
    def __init__(self):
        self.raw_ous_list = self._get_ous()
        self.raw_groups_list = self._get_groups()
        self.users_dict = self._get_users_dict()

    def _get_ous(self):
        _ous = []
        query = adquery.ADQuery()
        query.execute_query(
            attributes=["distinguishedName"],
            where_clause="objectClass = 'organizationalUnit'"
        )

        for row in query.get_results():
            if 'Domain Controllers' not in row["distinguishedName"]:
                _ous.append(row["distinguishedName"])

        return _ous
    
    def _get_groups(self):
        _groups = []
        query = adquery.ADQuery()
        query.execute_query(
            attributes=["distinguishedName"],
            where_clause="objectClass = 'group'"
        )

        for row in query.get_results():
            if 'Builtin' not in row["distinguishedName"] and ',CN=Users,' not in row["distinguishedName"]:
                _groups.append(row["distinguishedName"])

        return _groups
    
    def _get_users_dict(self):
        _users = {}
        query = adquery.ADQuery()
        query.execute_query(
            attributes=["distinguishedName", "givenName", "sn"],
            where_clause="objectCategory='person'"
        )

        for row in query.get_results():
            if ',CN=Users,' not in row["distinguishedName"]:
                _full_name = f'{row["givenName"]} {row["sn"]}'
                _users[row["distinguishedName"]] = _full_name

        return _users


def main():
    print('test')
    test = AdConnectorBaseClass()
    ous = test._get_users_dict()
    print(ous)


if __name__ == "__main__":
    # main()
    pass