#グローバル変数を定義します
animal = 'cat'
#グローバル変数をプリントします
print("animal:", animal)

def my_funk():
    #ローカル変数を定義します
    vagetable = 'carrot'
    #関数の中でグローバル変数の値をプリントします
    print("animal in my_func:", animal)
    #ローカル変数の値をプリントします。
    print("vagetable in_the_func:", vagetable)

my_func() 
