import re
from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer
from ad_functions.ad_connector_base_class import AdConnectorBaseClass
# from ad_connector_base_class import AdConnectorBaseClass
from CTkMessagebox import CTkMessagebox

class EditUserManager(AdConnectorBaseClass):
    def __init__(self):
        super().__init__()
        self.user_data = {}
        
    def get_user_info(self, cn):
        # print('start get_user_info()')
        # print(cn)
        _user = {}
        query = adquery.ADQuery()
        query.execute_query(
            attributes=["sn", "givenName", "title", "mail"],
            where_clause=f"distinguishedName = '{cn[0]}'"
        )

        for row in query.get_results():
            _user['name'] = row['givenName']
            # print(_user['name'])
            _user['surname'] = row['sn']
            # print(_user['surname'])
            _user['job_title'] = row['title']
            # print(_user['job_title'])
            _user['mail'] = row['mail']
            # print(_user['mail'])
            # if 'Builtin' not in row["distinguishedName"] and ',CN=Users,' not in row["distinguishedName"]:
                # _groups.append(row["distinguishedName"])
                
        # print(_user)    
        # print('end get_user_info()')
        self.user_data = _user

    # def get_list(self, raw_list):
    #     _list = []
    #     for item in raw_list:
    #         _value = item.split(',')[0]
    #         _value = _value[3:]
    #         _list.append(_value)

    #     return _list
    
    # def get_dict(self, raw_list):
    #     _dict = {}

    #     for item in raw_list:
    #         _value = item.split(',')[0]
    #         _value = _value[3:]
    #         _dict[_value] = item

    #     return _dict

    # def create_user(self, name, surname, job_title, mail, username, password, ou, groups):
    #     _full_ou = self.ous_dict.get(ou, None)
    #     _ou = ADContainer.from_dn(_full_ou)
    #     user = None
    #     _given_groups_list = [g.strip() for g in groups.split(",") if g.strip()]

    #     try:
    #         user = aduser.ADUser.create(
    #             username,
    #             _ou,
    #             password=password,
    #             optional_attributes={
    #                 "givenName": name,
    #                 "sn": surname,
    #                 "displayName": f"{name} {surname}",
    #                 "mail": mail,
    #                 "sAMAccountName": username,
    #                 "title": job_title,
    #             }
    #         )
            
    #         for group in _given_groups_list:
    #             _full_group = self.groups_dict.get(group, None)
    #             user.add_to_group(adgroup.ADGroup.from_dn(_full_group))
    #     except Exception as e:
    #         print(e)
    #         _error_code = str(e).split(": ", 1)[0]
    #         e = re.sub(r'^[^:]+:\s*', '', str(e))
    #         if _error_code == '0x80071392':
    #             CTkMessagebox(title="Błąd", message=e)
    #         else:
    #             CTkMessagebox(title="Błąd", message=e)
    #             _user_to_delete = aduser.ADUser(distinguished_name=f'CN={username},{str(_full_ou)}')
    #             _user_to_delete.delete()

    #     return user


def main():
    print('test')
    test = EditUserManager()
    ous = test.get_user_info('CN=Jacek Gula,OU=Kadry,DC=contoso,DC=com')
    print(ous)

    

if __name__ == "__main__":
    main()
    pass
