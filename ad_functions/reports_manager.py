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

    def generate_report(self):
        for dn in self._users_dn:
            _user_data = self.get_user_info(dn)
            _df = pd.DataFrame([_user_data])
            self.report_df = pd.concat([self.report_df, _df], ignore_index=True)
        print(self.report_df)

        if not self.report_df.empty:

            filepath = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                title="Zapisz raport jako"
            )

            if filepath:
                self.report_df.to_excel(filepath, index=False)
                print(f"Raport zapisany: {filepath}")
    
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
            _user['login'] = row['sAMAccountName']
            _user['name'] = row['givenName']
            _user['surname'] = row['sn']
            _user['ou'] = self._extract_ou(dn)
            _user['job_title'] = row['title']
            _user['mail'] = row['mail']

            _last_login = pyadutils.convert_datetime(row['lastLogon'])
            _user['last_login'] = _last_login - timedelta(hours=9) if _last_login != datetime(1970, 1, 1, 6, 0, 0) else None

            _passwd_last_set = pyadutils.convert_datetime(row['pwdLastSet'])
            _user['passwd_last_set'] = _passwd_last_set - timedelta(hours=9) if _passwd_last_set != datetime(1970, 1, 1, 6, 0, 0) else None

            try:
                _expires_date = pyadutils.convert_datetime(row['accountExpires'])
                _user['account_expires'] = _expires_date - timedelta(hours=9) if _expires_date != datetime(1970, 1, 1, 6, 0, 0) else None
            except:
                _user['account_expires'] = None
            
        _user_obj = adobject.ADObject.from_dn(dn)
        _settings = _user_obj.get_user_account_control_settings()
        _user['ACCOUNTDISABLE'] = _settings['ACCOUNTDISABLE']
        _user['LOCKOUT'] = _settings['LOCKOUT']
        _user['PASSWORD_EXPIRED'] = _settings['PASSWORD_EXPIRED']

        return _user
  

def main():
    print('test')
    test = ReportsManager()

if __name__ == "__main__":
    main()
    pass
