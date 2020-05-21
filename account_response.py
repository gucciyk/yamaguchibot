# -*- coding: utf-8 -*-

class Response:
    with open('trans.txt') as open_file:
        all_data = open_file.read()

    # 各行のリストを作る
    line_list = all_data.splitlines()

    #読み込んだデータを辞書に追加する
    bot_dict = {}

    responce = ""

    for line in line_list:
        orig,trans = line.split(':')
        bot_dict[orig] = trans

        def getResponse(self,text):
        for _dic in self.dic:
            if _dic == text:
                return self.dic[text]
            else:
                return str("該当ありません")

