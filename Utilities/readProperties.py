import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getEmailLV():
        email = config.get('Login Page','email')
        return email

    @staticmethod
    def getPassLV():
        password = config.get('Login Page', 'password')
        return password

    @staticmethod
    def getLoginBtnLV():
        logbtn = config.get('Login Page', 'loginBtn')
        return logbtn

    @staticmethod
    def getLPLogo():
        LPlogo = config.get('Login Page', 'landingpagelogo')
        return LPlogo

    @staticmethod
    def getProfileBtn():
        Pbtn = config.get('Landing Page XPATHS', 'ProfileButton')
        return Pbtn
    @staticmethod
    def getSettingBtn():
        Sbtn = config.get('Profile Page XPATHS', 'SettingButton')
        return Sbtn

    @staticmethod
    def getLogout():
        lobtn = config.get('Setting Page', 'LogoutBtn')
        return lobtn

    @staticmethod
    def getLogoutBtn():
        lbtn = config.get('Setting Page', 'LogoutSMbtn')
        return lbtn