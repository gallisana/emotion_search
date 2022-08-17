import numpy as np
import pandas as pd
from sklearn import linear_model
import csv
import gensim

clf = linear_model.LinearRegression()
#単語ベクトルの読み込み
##ここが一番時間がかかる。
##自分でプログラムを動かす場合は東北大の乾・岡崎研究室のwebサイトから単語ベクトルをダウンロードすること。

print("開始")
model = gensim.models.KeyedVectors.load_word2vec_format("/home/hakobe/natural_language/jawiki.all_vectors.100d.txt", binary=False)

#アンケート結果の読み込み
with open(r"/home/hakobe/natural_language/github/emotional_index.csv" ,encoding='utf-8-sig') as f:
    csv_data = csv.reader(f)
    eet_data = [ e for e in csv_data]
    f.close()

#単語ベクトルから単語を抽出
##分析結果は最終的に1511782行2列のデータになる。
##1列目に単語、2列目に予測値が入る。
##なぜ1511782個かといえば、東北大の単語ベクトルに存在するデータが1511782個だから。
##1列目に書くために単語ベクトルから単語を1511782個抽出している。

A = model.wv.most_similar(positive=["情緒"], topn=1511781)
pre_wordlist = [str("空白") for i in range(1511782)]
for i in range(1511781):
    pre_wordlist[i] = A[i][0]
pre_wordlist[1511781] = "情緒"

#分析用のデータ（873行102列）の作成
##873はアンケートの答えのうち単語ベクトルに存在する単語の数。
##プログラムを自分で動かす場合はアンケート結果の数に応じて書き換えること。
##102は　単語　エモさ指数　100次元のベクトル で構成されている。

merged_data = [[0 for i in range(102)] for j in range(873)]
vector = "a"

for i in range(873):
    try:
        vector = model[eet_data[i][0]]
        for j in range(100):
            merged_data[i][0] = eet_data[i][0]
            merged_data[i][1] = eet_data[i][1]
            merged_data[i][j + 2] = vector[j]
    except KeyError:
        eet_data[i][0] = str("##"+str(eet_data[i][0])+ "##")
        for j in range(100):
            merged_data[i][0] = eet_data[i][0]
            merged_data[i][1] = eet_data[i][1]
            merged_data[i][j + 2] = vector[j]

df = pd.DataFrame(merged_data)

#回帰分析の実行
feature_name = ["word","emo_point",'vector1', 'vector2', 'vector3', 'vector4', 'vector5', 'vector6', 'vector7', 'vector8', 'vector9', 'vector10', 'vector11', 'vector12', 'vector13', 'vector14', 'vector15', 'vector16', 'vector17', 'vector18', 'vector19', 'vector20', 'vector21', 'vector22', 'vector23', 'vector24', 'vector25', 'vector26', 'vector27', 'vector28', 'vector29', 'vector30', 'vector31', 'vector32', 'vector33', 'vector34', 'vector35', 'vector36', 'vector37', 'vector38', 'vector39', 'vector40', 'vector41', 'vector42', 'vector43', 'vector44', 'vector45', 'vector46', 'vector47', 'vector48', 'vector49', 'vector50', 'vector51', 'vector52', 'vector53', 'vector54', 'vector55', 'vector56', 'vector57', 'vector58', 'vector59', 'vector60', 'vector61', 'vector62', 'vector63', 'vector64', 'vector65', 'vector66', 'vector67', 'vector68', 'vector69', 'vector70', 'vector71', 'vector72', 'vector73', 'vector74', 'vector75', 'vector76', 'vector77', 'vector78', 'vector79', 'vector80', 'vector81', 'vector82', 'vector83', 'vector84', 'vector85', 'vector86', 'vector87', 'vector88', 'vector89', 'vector90', 'vector91', 'vector92', 'vector93', 'vector94', 'vector95', 'vector96', 'vector97', 'vector98', 'vector99', 'vector100']
df.columns = feature_name
W = df.drop(columns = "word")
X = W.drop(columns = "emo_point")
Y = df["emo_point"]
clf.fit(X,Y)

intercept = clf.intercept_
wordlist = []
answer = []

#873単語から導き出した予測を全単語(1511782個)に当てはめる

for i in range(len(pre_wordlist)):
    wordlist.append(pre_wordlist[i])

for i in range(len(wordlist)):
    value = intercept
    word = wordlist[i]
    vector = model.wv[word]
    for j in range (100):
        value  +=  vector[j] * clf.coef_[j]
    answer.append([word,value])

answer_sorted = sorted(answer, reverse=True, key=lambda x: x[1])

#当てはめた結果をregression.csvに書き込む
##プログラムを自分で動かす場合は先んじて結果書き込み用のcsvを作っておくこと。
with open(r"/home/hakobe/natural_language/github/regression.csv" ,encoding='utf-8-sig', mode = "w") as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(answer_sorted)
    f.close()

