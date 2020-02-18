#日付と日時を取得するライブラリ(標準機能)
import datetime as dt

def function(thisyear, today, oprn):
    newyear = dt.datetime(thisyear, 1, 1)
    print('---------------------------------------------')
    if oprn==1:
        #timedeltaはdatetimeライブラリのうるう年を考慮した便利な奴
        print(today + dt.timedelta(days=7))
    
    elif oprn==2:
        print(today + dt.timedelta(days=30))

    elif oprn==3:
        print(today + dt.timedelta(days=365))

    elif oprn==4:
        calc = today - newyear + dt.timedelta(days=1)
        #.をつけて抜き取りたい要素を書くと抜き取れる
        print(calc.days)
    
    else:
        print('無効な識別コードです。')

######################################################
#実行した時点の日時を取得
today = dt.datetime.today()
print('=============================================')
print('実行年月日時分秒:',today)
print('=============================================')

#todayから年の部分を抜き取り
thisyear = today.year

print('''知りたい項目の識別コードを入力
 1週間後の日付: 1
 30日後の日付: 2
 1年後(365日後)の日付: 3
''',str(thisyear) + '年1月1日から何日目か: 4')
oprn = input('>>')
oprn = int(oprn)

#ユーザ関数functionに値を投げ込み
#ちなみにclassの中のdefはメソッドという
#ユーザ関数に出力
function(thisyear, today, oprn)