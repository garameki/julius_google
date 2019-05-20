order to make and to execute   
=============================  
  
(0.1. edit google.txt)  
(0.1. execute bash conv.sh)  
1. edit google.voca  
2. edit google.grammar  
3. execute mkdfa.pl google  
4. execute bash julius-module.sh  
5. execute python3 hear.py  
6. execute python3 answer.py  
  
置く場所  
========  
	~/src/julius_google/  
  
説明  
=====  
	喋りかけると音声で返す  
	マイク付きのUSBカメラでも使える  
	max31856で温度を返すこともできる。  
  
必要なライブラリ  
================  
同じフォルダに以下のフォルダを置いておきます。
	juliusを手に入れてください。  
	  julius-4.4.2.1/  
	juliusの辞書も必要です。  
	  julius-dict/  
  
ls -l 
==============  
別途インストールするディレクトリ  
	#drwxr-xr-x 22 pi pi  4096 11月  5  2018 julius-4.4.2.1  
	#drwxr-xr-x  6 pi pi  4096 11月 17  2016 julius-dict  
説明とライセンス  
	-rw-r--r--  1 pi pi   740  5月 20 17:09 README.md  
	-rw-r--r--  1 pi pi 10425 12月  9 07:02 LICENSE.txt  
実行時に使うファイル(README.md参照)  
	-rw-r--r--  1 pi pi   230 12月  8 23:26 julius-module.sh  
	-rw-r--r--  1 pi pi   745 12月 11 13:34 hear.py  
	-rw-r--r--  1 pi pi  4445  5月 20 13:02 answer.py  
自作の言葉と構文(.vocaは自動生成)  
	-rw-r--r--  1 pi pi   321  5月 20 13:02 google.txt  
	-rw-r--r--  1 pi pi  1649  5月 20 13:02 google.voca  
	-rw-r--r--  1 pi pi    68 12月  9 00:12 google.grammar  
音声認識をスレッド化するライブラリ  
	-rw-r--r--  1 pi pi   972 12月 21 02:44 julius_cli.py  
MAX31856で温度を計測するライブラリ  
	-rw-r--r--  1 pi pi  4392 12月  9 01:07 max31856.py  
シェル  
	-rwxr-x---  1 pi pi   113 12月  8 23:42 conv.sh  
	-rwxr-x---  1 pi pi   172 12月  8 23:45 sgoogle  
	-rwxr-x---  1 pi pi    40 12月  8 22:32 start_google_answer  
	-rwxr-x---  1 pi pi    38 12月  8 22:32 start_google_hear  
	-rwxr-x---  1 pi pi   221 12月  8 23:55 stop_google  
	-rwxr-x---  1 pi pi   154 12月  9 01:07 renewmax  
バージョン管理  
	-rw-r--r--  1 pi pi  2306  5月 20 13:03 CHANGELOG.md  
	-rw-r--r--  1 pi pi     6  5月 20 13:03 VERSION  
  
以下は必要なし  
==============  
pythonライブラリ(自動生成)  
	#drwxr-xr-x  2 pi pi  4096 12月 21 07:38 __pycache__  
音声認識ライブラリ(自動生成)  
	#-rw-r--r--  1 pi pi    72  5月 20 16:57 google.dfa  
	#-rw-r--r--  1 pi pi  1862  5月 20 16:57 google.dict  
	#-rw-r--r--  1 pi pi    34  5月 20 16:57 google.term  
音声認識ライブラリバックアップ(自動生成)  
	#-rw-r--r--  1 pi pi  2088 12月 27 21:21 google.dict.1  
	#-rw-r--r--  1 pi pi    72 12月 27 21:21 google.dfa.1  
	#-rw-r--r--  1 pi pi    34 12月 27 21:21 google.term.1  
よくわからない  
	#-rw-r--r--  1 pi pi     5  5月 20 17:01 hear.txt  
	#-rw-r--r--  1 pi pi   398 12月  8 23:34 google.txt.osoi  
シェルnohupを使ったとときに生成するファイル  
	#-rw-r--r--  1 pi pi     0 12月 27 21:21 t  
	#-rw-r--r--  1 pi pi 27338 12月 27 21:44 tt  
	#-rw-------  1 pi pi  9980 12月  8 22:25 nohup.out  
  
