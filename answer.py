import subprocess
import julius_cli
import random
from datetime import datetime
import locale
from time import sleep
import os
import codecs
import math
import max31856
max = max31856.Max31856(0,0)

phrases = [
	[["偉人の言葉"],"はい、",4],
	[["日付"],"えーと、",3],
	[["呼んでない"],"すみません",0],
	[["用ない"],"そうですか",0],
	[["わかった"],"どういたしまして",0],
	[["そうか"],"はい",0],
	[["OK"],"どういたしまして、",0],
	[["感謝"],"どういたしまして、",0],
	[["OK","グーグル"],"なにか御用でしょうか？",0],
	[["OK","仮面ライダー"],"わたしは、仮面ライダーではありません。",0],
	[["OK","ワングル"],"わんわん",0],
	[["くだらない"],"くだらなくて、申し訳ありません。",0],
	[["温度"],"少々お待ちください",1],
	[["時刻"],"えーと、",2],
]

def conversation(words):
	global phrases
	for sets in phrases:
		bunsetus = sets[0]
		if len(bunsetus)==len(words):
			flag = True
			for i in range(len(bunsetus)):
				if words[i]==bunsetus[i]:
					pass
				else:
					flag = False
					break
			if flag:
				return True,sets[1],sets[2]
	return False,"",0


def answer(words):
	global max
	print("answer")
	flag,phrase,num = conversation(words)
	if flag:
		cmd = '/home/pi/src/aquestalkpi/AquesTalkPi -s 100 "     {0}" | aplay'.format(phrase)
		#subprocess.check_output(cmd,shell=True)

		print('{0}'.format(phrase))
		os.system(cmd)

		if num == 0:
			pass
		else:
			if num == 1:
				aTemps = max.read()
				sTemp = str(math.floor(aTemps["HJ"]*0.0625+0.0001))
				phrase = "ただいまの部屋の温度は　　"+sTemp+"度です。"
			elif num == 2:
				now = datetime.now()
				hh = now.strftime("%H")
				mm = now.strftime("%M")
				phrase = "ただいまの時刻は   "+hh+"時"+mm+"分です。"
			elif num == 3:
				now = datetime.now()
				MM = now.strftime("%m")
				DD = now.strftime("%d")
				locale.setlocale(locale.LC_TIME,'ja_JP.UTF-8')
				dd = now.strftime("%a")
				if DD == "20":
					DD = "はつか"
				elif DD == "01":
					DD = "ついたち"
				elif DD == "02":
					DD = "ふつか"
				elif DD == "03":
					DD = "みっか"
				elif DD == "04":
					DD = "よっか"
				elif DD == "05":
					DD = "いつか"
				elif DD == "06":
					DD = "むいか"
				elif DD == "07":
					DD = "なのか"
				elif DD == "08":
					DD = "ようか"
				elif DD == "09":
					DD = "ここのか"
				elif DD == "10":
					DD = "とおか"
				elif DD == "09":
					DD = "ここのか"
				elif DD == "09":
					DD = "ここのか"
				elif DD == "19":
					DD = "じゅうくにち"
				elif DD == "29":
					DD = "にじゅうくにち"
				else:
					DD = DD+"にち"

				phrase = "今日は   "+MM+"がつ"+DD+"　"+dd+"曜日です。"
			elif num == 4:
				nn = random.randint(0,4)
				if nn == 0:phrase = "　　　　われ思う、　　ゆえに、　　われあり。　　　　　　　パスカル"
				elif nn == 1:phrase = "　　　　小さな成功の積み重ねだけが、大成功に導いてくれる"
				elif nn == 2:phrase = "　　　　自分を追い込んで、成果を残す。自分にプレッシャーを掛けなさい"
				elif nn == 3:phrase = "　　　　午前中の数分のトレーニングが脳を若返らせる。トレーニングを続けることで、老いた脳から若い脳へ。"
				elif nn == 4:phrase = "　　　　脳にとっての幸福は、学び続け、成長し続け、達成を繰り返すこと。"
			cmd = '/home/pi/src/aquestalkpi/AquesTalkPi -s 100 "　　　{0}" | aplay'.format(phrase)
			print('{0}'.format(phrase))
			os.system(cmd)

		return True
ttBefore = ""
while True:
	tt = os.path.getmtime("hear.txt")
	if(tt != ttBefore):
		ttBefore = tt
		words = []
		for line in codecs.open("hear.txt","r","shift_jis"):
			words.append(line.strip())
		answer(words)
	sleep(1)


