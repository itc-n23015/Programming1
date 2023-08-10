def make_circle_area_fuc(pi = 3.14):
    '''円の面積を計算する関数を作る'''

    def circle_area(radius):
        '''円の面積を計算する'''

        return radius * radius * pi

    return circle_area

# pi が 初期設定 (3.14) のとき
circle_area_default = make_circle_area_func()
# pi が 3.1415926535 のとき
circle_area_precise = make_circle_Area_func(pi = 3.1415926535)

type(circle_area_default), type(circle_area_precise)
