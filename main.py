import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./sample.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# cvtColor : 画像の色空間(色)の変更を行う関数。
# cvtColorについて : https://kuroro.blog/python/7IFCPLA4DzV8nUTchKsb/
# 第一引数 : 多次元配列(numpy.ndarray)
# 第二引数 : 変更前の画像の色空間(色)と、変更後の画像の色空間(色)を示す定数を設定。
# cv2.COLOR_BGR2GRAY : BGR(Blue, Green, Red)形式の色空間(色)を持つ画像をグレースケール画像へ変更する。
# グレースケールとは? : https://www.shinkohsha.co.jp/blog/monochrome-shirokuro-grayscale/
# 戻り値 : 多次元配列(numpy.ndarray)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sobel関数 : Sobelフィルタを用いて、画像の輝度勾配(エッジ)を検出するために利用する関数。
# 第一引数 : 多次元配列(numpy.ndarray)
# 第二引数 : 出力画像のビット深度を指定。
# 第三引数 : 横方向Sobelフィルタを利用する回数。1回とする。
# 第四引数 : 縦方向Sobelフィルタを利用する回数。0回とする。
# 第五引数 : カーネルサイズ。3 x 3のカーネルを生成する。
# 戻り値 多次元配列(numpy.ndarray)
img = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', img)
