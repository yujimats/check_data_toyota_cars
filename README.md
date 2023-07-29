# できること  
Kaggleで公開されているデータセットを確認。  
以下リンク先からダウンロードしたファイルを確認する。  
https://www.kaggle.com/datasets/occultainsights/toyota-cars-over-20k-labeled-images  

# 手順
## Dockerコンテナを立ち上げる  
[/docker/README.md](/docker/README.md)に従い、Dockerイメージのビルドとコンテナの立ち上げを行う。  

## 実行  
コンテナ内で、以下実行する。  
```
python3 check_data.py
```

## 結果の確認  
`output`フォルダに`dataset_toyota_cars.csv`が保存され、結果が確認できる。  
クラス名ごとのクラス数が確認できる。  
```file: dataset_toyota_cars.csv
dir_name,file_count
4runner,946
alphard,64
avalon,497
avanza,63
avensis,167
aygo,109
camry,2246
celica,101
corolla,2311
corona,70
crown,77
estima,32
etios,74
fortuner,254
hiace,75
highlander,1119
hilux,435
innova,121
iq,27
matrix,63
mirai,57
previa,44
prius,1039
rav4,1786
revo,162
rush,23
sequoia,166
sienna,652
soarer,48
starlet,48
supra,173
tacoma,1318
tundra,1035
venza,122
verso,112
vios,141
vitz,102
yaris,844
```

# 参考  
こちらにもまとめているので参照してください。  
https://qiita.com/YujiMatsu/items/5c0d425f4d55a7010a98  
