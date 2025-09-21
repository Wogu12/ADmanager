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

        _user_obj = adobject.ADObject.from_dn(dn[0])
        _settings = _user_obj.get_user_account_control_settings()
        self.user_data['ACCOUNTDISABLE'] = _settings['ACCOUNTDISABLE']

        _user_attributes = aduser.ADUser.from_dn(dn[0])
        _raw_groups = _user_attributes.get_attribute("memberOf")
        _groups_dict = {}
        if len(_raw_groups) > 0:
            _parsed_list = []
            for item in _raw_groups:
                _value = item.split(',')[0]
                _value = _value[3:]
                _parsed_list.append(_value)
                _groups_dict[item] = _value
        else:
            self.user_data['groups'] = None
        self.user_data['groups'] = _groups_dict 
        self.user_data['user_ou'] = self.get_ou(dn[0])       
            
    @staticmethod
    def get_ou(dn):
        return re.sub(r"^CN=[^,]+,", "", dn)

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

    def edit_user_data(self, dn, new_name, new_surname, new_job_title, new_mail, new_ou, to_remove, to_add):
        _user_old_ou = self.get_ou(dn[0])
        _new_ou = self.mapped_ous[new_ou]
        self.edit_basic_data(dn[0], new_name, new_surname, new_job_title, new_mail)
        
        if not not to_remove or not not to_add:
            self.edit_groups(dn[0], to_remove, to_add)
        if _user_old_ou != _new_ou:
            self.edit_ou(dn[0], _new_ou)

        CTkMessagebox(title="Uwaga", message='Dane użytkownika zostały zmienione.')

    def edit_basic_data(self, dn, name, surname, title, mail):
        _user = aduser.ADUser.from_dn(dn)
    
        if name is not None:
            _user.update_attribute("givenName", name)
        if surname is not None:
            _user.update_attribute("sn", surname)
        if title is not None:
            _user.update_attribute("title", title)
        if mail is not None:
            _user.update_attribute("mail", mail)

    def edit_groups(self, dn, to_remove, to_add):
        _user_obj = adobject.ADObject.from_dn(dn)
        cn_to_dn = {raw.split(',')[0][3:]: raw for raw in self.raw_groups_list}

        if to_remove:
            for group in to_remove:
                full_dn = cn_to_dn.get(group)
                if full_dn:
                    group_obj = adgroup.ADGroup.from_dn(full_dn)
                    _user_obj.remove_from_group(group_obj)
        if to_add:
            for group in to_add:
                full_dn = cn_to_dn.get(group)
                if full_dn:
                    group_obj = adgroup.ADGroup.from_dn(full_dn)
                    _user_obj.add_to_group(group_obj)
    
    def edit_ou(self, dn, new_ou):
        _user_obj = adobject.ADObject.from_dn(dn)
        _user_obj.move(adgroup.ADGroup.from_dn(new_ou))


def main():
    print('test')
    test = EditUserManager()
    ous = test.groups_list
    print(ous)

    

# if __name__ == "__main__":
#     main()
#     pass
