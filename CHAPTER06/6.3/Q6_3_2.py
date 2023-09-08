class Square(Rectangle):
    """正方形"""

    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"


# インスタンスを作って実行
s1 = Square(4)
s1.show_attributes()
