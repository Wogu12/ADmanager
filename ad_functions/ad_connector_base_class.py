from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer
# from pyad.pyadexceptions import InvalidObjectException

class AdConnectorBaseClass:
    def __init__(self):
        self.raw_ous_list = self._get_ous()

    def print_def(self):
        current_user = aduser.ADUser.from_cn("Wojciech Guja")
        # print(current_user)

    def _get_ous(self):
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
    
    def get_groups(self):
        ...


def main():
    print('test')
    test = AdConnectorBaseClass()
    ous = test.get_ous()
    print(ous)
    # test.print_def()

    

if __name__ == "__main__":
    # main()
    pass