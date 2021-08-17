# 類別可以透過 dict 語法存取
class DictDemo:
    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

if __name__ == '__main__':
    dict_demo = DictDemo('h', 170)
    # -----------------------------
    print(dict_demo.dict['h'])
    dict_demo.dict['w'] = 60
    print(dict_demo.dict['w'])
    #-----------------------------
    print(dict_demo['h'])
    dict_demo['w'] = 60
    print(dict_demo['w'])
