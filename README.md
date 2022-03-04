#  
# 顯示結果:
![dd6418e86fe4e408e208795275c1b6a2 1](https://user-images.githubusercontent.com/74965449/153378244-f4eaf577-3fa1-4e6b-b258-c6d0d56cb5f4.gif)


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
