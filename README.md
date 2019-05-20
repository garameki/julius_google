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

