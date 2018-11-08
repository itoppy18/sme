#!/usr/bin/python3
#coding:utf-8
#Simulator for Magicicadas Extarmination, SME v.3.0.0 source code
#素数ゼミ絶滅シミュレーター
#made by @itoppy18

#メイン関数の定義
#nは初期蝉個体数(nomber)、yは繰り返す回数(years)
def main(n, y):
	#初期化処理
	#①12年ゼミから18年ゼミを同数発生させる
	int(n)
	mcDict = {
							12 : n,
							13 : n,
							14 : n,
							15 : n,
							16 : n,
							17 : n,
							18 : n
						}	
	#②「年」の初期化
	years = 0
	#指定した回数繰り返す
	for i in range(y):
		#mcAll:その年出てきた蝉の合計
		mcAll = 0
		#index:その年出てきた蝉のリスト
		index = []
		years += 1
		for key in mcDict:
			#19年未満であれば何もしない
			if years < 19:
				break
			else:
				#yearsをkeyで割ったあまりを求めることでその年出現するかを判定する
				if years % key == 0:
					#出現すればindexに追加する
					index.append(key)
		#その年出現する蝉の合計を求める
		for i in index:
			mcAll += mcDict[i]
		#蝉を減らす処理
		for key in mcDict:
			#もし出現すれば「割合減少法」により減らす
			#割合減少法：
			#「蝉の個体数が全体の中で占める割合が大きければ、
			#それ以外の蝉と交雑することも少ないだろう」という発想の減少方法。
			#要するに15年ゼミがその年出現した蝉の90%を占めていたら交雑する確率は(100-90=)10%だろう。
			if key in index and mcAll != 0:
				int(mcDict[key])
				mcPer = mcDict[key] / mcAll
				mcDict[key] *= mcPer
				#乗法と除法の繰り返しで蝉の個体数が小数になっている可能性があるため四捨五入して整数化する
				mcDict[key] = round(mcDict[key])
		#年と蝉の個体数を出力して1年分の処理を終了
		print(years)
		print(mcDict)
	#すべて終了したらendと出力して終了
	print("end")

#実行！
main(1000000000000, 10000)
					
