print("有天空，我，你，牛逼")
hao_word = {
    "天空" : "阴暗的低沉",
    "我" : "抬头看天，低头看你",
    "你" : "静默矗立",
    "牛逼": "呀呼"
    }
word = input("输入")
if word in hao_word:
    print("你查询的" + word + "含义")
    print(hao_word[word])
    print(f"{word}的含义：{hao_word[word]}")
else:
    print("无")