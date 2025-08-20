from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer

class AdConnectorBaseClass:
    def __init__(self):
        self.raw_ous_list = self._get_ous()
        self.raw_groups_list = self._get_groups()

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


def main():
    print('test')
    test = AdConnectorBaseClass()
    ous = test.get_groups()
    print(ous)


if __name__ == "__main__":
    # main()
    pass