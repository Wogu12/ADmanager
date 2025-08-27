import re
from pyad import *
from pyad import aduser, adquery, adgroup
from pyad.adcontainer import ADContainer
from ad_functions.ad_connector_base_class import AdConnectorBaseClass
# from ad_connector_base_class import AdConnectorBaseClass
from CTkMessagebox import CTkMessagebox
import datetime

class EditUserManager(AdConnectorBaseClass):
    def __init__(self):
        super().__init__()
        self.user_data = {}
        self.groups_list = self.get_list(self.raw_groups_list)

    def get_list(self, raw_list):
        _list = []
        for item in raw_list:
            _value = item.split(',')[0]
            _value = _value[3:]
            _list.append(_value)

        return _list
        
    def get_user_info(self, dn):
        _user = {}
        query = adquery.ADQuery()
        query.execute_query(
            attributes=["sn", "givenName", "title", "mail", 'sAMAccountName'],
            where_clause=f"distinguishedName = '{dn[0]}'"
        )

        for row in query.get_results():
            _user['name'] = row['givenName'] if row['givenName'] is not None else ''
            _user['surname'] = row['sn'] if row['sn'] is not None else ''
            _user['job_title'] = row['title'] if row['title'] is not None else ''
            _user['mail'] = row['mail'] if row['mail'] is not None else ''
            _user['login'] = row['sAMAccountName'] if row['sAMAccountName'] is not None else ''
                
        self.user_data = _user

        user_obj = adobject.ADObject.from_dn(dn[0])
        attr = user_obj.get_user_account_control_settings()
        print(attr['ACCOUNTDISABLE'])
        self.user_data['ACCOUNTDISABLE'] = attr['ACCOUNTDISABLE']

    def get_user_ou(self, dn):
        ...

    def change_passwd(self, dn, password, change_at_logon):
        _user = aduser.ADUser.from_dn(dn[0])
        try:
            _user.set_password(password)
            CTkMessagebox(title="Uwaga", message='Hasło zastało zmienione.')
            if change_at_logon:
                _user.force_pwd_change_on_login()
        except Exception as e:
            e = re.sub(r'^[^:]+:\s*', '', str(e))
            CTkMessagebox(title="Błąd", message=e)

    def unlock_acc(self, dn):
        _user = aduser.ADUser.from_dn(dn[0])
        _user.unlock()
        CTkMessagebox(title="Uwaga", message='Konto zastało odblokowane.')

    def enable_disable_acc(self, dn, option):
        _user_obj = adobject.ADObject.from_dn(dn[0])
        user_obj = adobject.ADObject.from_dn(dn[0])
        attr = user_obj.get_user_account_control_settings()
        if option == 'enable' and attr['ACCOUNTDISABLE']:
            _user_obj.set_user_account_control_setting('ACCOUNTDISABLE', False)
            CTkMessagebox(title="Uwaga", message='Konto zastało włączone.')
        if option == 'disable' and not attr['ACCOUNTDISABLE']:
            _user_obj.set_user_account_control_setting('ACCOUNTDISABLE', True)
            CTkMessagebox(title="Uwaga", message='Konto zastało wyłączone.')

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
    ous = test.groups_list
    print(ous)

    

if __name__ == "__main__":
    main()
    pass
