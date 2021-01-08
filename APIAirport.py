import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
CODE = ''
xmlUrl = 'http://openapi.airport.co.kr/service/rest/AirportCodeList/getAirportCodeList'
#?ServiceKey=인증키&pageNo=1'
My_API_Key = unquote('b5397ju6M5FpatzJeuNtcJ8jFUDyUWmMNEXo%2FcFEevJvGH9EDPYPlGtgwCDo58Gwkdp74onhUBpvmyTMS12PZw%3D%3D')


#입력 함수 정의
def insert_text():
    messagebox.showinfo(title='검색 시작', message='검색을 시작합니다. 이 창을 닫은 후 검색이 완료될 때까지 잠시만 기다려 주십시오.\n검색 중 조작시 오류가 발생하거나 시스템이 멈출 수 있습니다.')
    findvalue = 0
    CODE = ins.get()
    
    find_code = CODE
    for pgnoi in range(136) :
        queryParams = '?' + urlencode(
            {
                quote_plus('ServiceKey') : My_API_Key,
                quote_plus('pageNo') : pgnoi

            }
        )

        response = requests.get(xmlUrl+queryParams).text.encode('utf-8')
        xmlobj = bs4.BeautifulSoup(response,'lxml-xml')
        
        for item in xmlobj.items:
            cityKor = item.find('cityKor')
            code = item.find('cityCode')
            cityEng = item.find('cityEng')
            if find_code==code.get_text():
                resultCode.configure(bg='#3700B3',fg='white',text='검색된 공항/도시입니다.\nThis is the result airport/city\n'+'\n검색한 공항 코드(Code that you find.) : '+code.get_text()+'\n'+'한국어 공항/도시명 : '+cityKor.get_text()+'\n'+'English Airport/City Name: '+cityEng.get_text())
                findvalue=1
                break
    
        if findvalue==1:
            break
        else:
            resultCode.configure(bg='#3700B3',fg='white',text='해당 코드명의 공항을 찾을 수 없습니다.\nAirport Not Found')
            #messagebox.showinfo(title='코드명 없음', message='해당 코드명의 공항이 없습니다.')
#tk
window = tk.Tk()
window.configure(background='#6200EE')

Lbl = tk.Label(window,justify='left',bg='#6200EE',fg='white',text="수하물 발송 전 공항 코드가 올바른지 확인해 보세요.\nThis is IATA airport code finder.\nPlease input IATA code.")
Lbl.grid(row=0,column=0)
#Lbl.pack()

ins = tk.Entry(window)
ins.grid(row=1,column=0)
#ins.pack()

insBtn = tk.Button(window, text="확인",command=insert_text,relief="solid",bg="#2980B9",fg="white")
insBtn.grid(row=1,column=1)
#insBtn.pack()

resultCode = tk.Label(window,text="")
resultCode.grid(row=2,column=0)
#resultCode.pack()

copyrightlbl = tk.Label(window,justify='left',bg='#6200EE',fg='white',text="본 프로그램의 저작권은 제작자에게 있으며, 공항 정보 API의 저작권은 한국공항공사에 있습니다. \nAPI 활용 및 저작권 규정은 한국공항공사 및 대한민국 정부의 규정에 따릅니다.")
copyrightlbl.grid(row=3,column=0)
#copyrightlbl.pack()

isBtn = tk.Button(window, text="이용약관")
isBtn.grid(row=4,column=0)
#isBtn.pack()

infoBtn = tk.Button(window, text="프로그램 정보")
infoBtn.grid(row=4,column=1)
#infoBtn.pack()

#tk end
window.mainloop()
