#  界面
# 顯示結果:
![image](https://user-images.githubusercontent.com/74965449/158995924-9fab6464-6d8f-43c9-ae5f-e1736dcc0a38.png)


## 步驟一:
### 先使用qtdesigner畫出介面
1.將介面儲存成.ui檔 \
2.將.ui檔轉換成.py檔&ensp; 使用語法:pyuic5 -x day7.ui -o UI.py

## 步驟二:
### 把上個步驟做的py檔 拆解成qt,controller,start三個.py檔
1. qt負責介面
2. controller負責&nbsp; 事件觸發
3. start負責執行\
**(注意:類別繼承的地方)**\
參考資料:https://www.wongwonggoods.com/python/pyqt5-7/
