・データの説明
emotional_index：記事p126の「エモさ指数」。アンケートの結果のうちデータに存在する単語のみを抜き出している。
regression：記事p127以降で用いている分析データ。
・プログラムの使い方
①東北大の乾・岡崎研究室
（http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/）
から単語ベクトル（100次元、記事・単語両方入っているもの）をダウンロードし、単語ベクトルの場所（プログラム15行目の"/home/hakobe/natural_language/jawiki.all_vectors.100d.txt"）を適宜書き換える
②好きなアンケート結果を使ってemotional_index的なデータ（n行2列　1列目は単語、2列目は何らかの方法で作った指数）を作り、アンケート結果の場所（プログラム18行目の"/home/hakobe/natural_language/github/emotional_index.csv"）を適宜書き換える
③空っぽのcsvファイルを分析結果書き出し用に用意し、分析結果の場所（プログラム88行目の"/home/hakobe/natural_language/github/regression.csv"）を適宜書き換える
④プログラムを実行！すると分析結果が書き込まれる

君もこれで自然言語処理マスターだ！

・注意
単語ベクトルがバカ重いのでプログラムを動かす場合はメモリが32GB以上必要です。regression.csvを開くだけなら16GBで十分です。
プログラム40・43行目の 873 は、あなたが作ったアンケートのデータ量に応じて書き換えてください。
パスの書き方は環境(Windows,Linux)に合わせて適宜変えること。

　
文責　箱部ルリ（twitter:@gallisana）