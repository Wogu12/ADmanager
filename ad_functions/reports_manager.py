import re
from pyad import *
from pyad import aduser, adquery, adgroup, pyadutils
from pyad.adcontainer import ADContainer
from ad_functions.ad_connector_base_class import AdConnectorBaseClass
# from ad_connector_base_class import AdConnectorBaseClass
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
from datetime import datetime, timedelta
import pandas as pd

class ReportsManager(AdConnectorBaseClass):
    def __init__(self):
        super().__init__()
        self._users_dn = self.users_dict.keys()        

        self.report_df = pd.DataFrame()

    def generate_report(self, state_acc_expires, state_pwd_last_set, state_acc_locked, state_show_disabled_acc, state_last_login, state_passwd_expires):
        for dn in self._users_dn:
            _user_data = self.get_user_info(dn)
            _df = pd.DataFrame([_user_data])
            self.report_df = pd.concat([self.report_df, _df], ignore_index=True)

        if state_acc_expires == 0:
            self.report_df = self.report_df.drop(columns=['Konto wygasa'])
        if state_pwd_last_set == 0:
            self.report_df = self.report_df.drop(columns=['Ostatnia zmiana hasła'])
        if state_acc_locked == 0:
            self.report_df = self.report_df.drop(columns=['Konto zablokowane'])
        if state_show_disabled_acc == 0:
            self.report_df = self.report_df.drop(columns=['Konto wyłączone'])
        if state_last_login == 0:
            self.report_df = self.report_df.drop(columns=['Ostatnie logowanie'])
        if state_passwd_expires == 0:
            self.report_df = self.report_df.drop(columns=['Hasło traci ważność'])

        if not self.report_df.empty:

            filepath = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                title="Zapisz raport jako"
            )

            if filepath:
                self.report_df.to_excel(filepath, index=False)
                CTkMessagebox(title="Sukces", message=f'Raport zapisany: {filepath}')
            else:
                pass
    
    @staticmethod
    def _extract_ou(dn):
        ous = [part[3:] for part in dn.split(",") if part.startswith("OU=")]
        return "/".join(reversed(ous))

    def get_user_info(self, dn):
        _user = {}
        query = adquery.ADQuery()
        query.execute_query(
            attributes=["sn", "givenName", "title", "mail", 'sAMAccountName', 'lastLogon', 'pwdLastSet', 'accountExpires'],
            where_clause=f"distinguishedName = '{dn}'"
        )

        for row in query.get_results():
            _user['Login'] = row['sAMAccountName']
            _user['Imię'] = row['givenName']
            _user['Nazwisko'] = row['sn']
            _user['Dział'] = self._extract_ou(dn)
            _user['Stanowisko'] = row['title']
            _user['E-mail'] = row['mail']

            _last_login = pyadutils.convert_datetime(row['lastLogon'])
            _user['Ostatnie logowanie'] = _last_login - timedelta(hours=9) if _last_login != datetime(1970, 1, 1, 6, 0, 0) else None

            _passwd_last_set = pyadutils.convert_datetime(row['pwdLastSet'])
            _user['Ostatnia zmiana hasła'] = _passwd_last_set - timedelta(hours=9) if _passwd_last_set != datetime(1970, 1, 1, 6, 0, 0) else None

            try:
                _expires_date = pyadutils.convert_datetime(row['accountExpires'])
                _user['Konto wygasa'] = _expires_date - timedelta(hours=9) if _expires_date != datetime(1970, 1, 1, 6, 0, 0) else None
            except:
                _user['Konto wygasa'] = None
            
        _user_obj = adobject.ADObject.from_dn(dn)
        _settings = _user_obj.get_user_account_control_settings()
        _user['Konto wyłączone'] = _settings['ACCOUNTDISABLE']
        _user['Konto zablokowane'] = _settings['LOCKOUT']
        _user['Hasło traci ważność'] = _settings['PASSWORD_EXPIRED']

        return _user
  

def main():
    print('test')
    test = ReportsManager()

if __name__ == "__main__":
    main()
    pass
