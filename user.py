class user():
    def __init__(self, nama, username, pw):
        self.nama = nama
        self.username = username
        self.__password = pw

    def getPassword(self):
        return self.__password

# objUser = user('qqq','qwe',1312)
# print(objUser.getNama())