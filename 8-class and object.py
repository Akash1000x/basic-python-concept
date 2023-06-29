class My_Intro:
    def __init__(self, name, fathers_name, hobbie, address):
        self.name = name
        self.fathers_name = fathers_name
        self.hobbie = hobbie
        self.address = address

    def printing(self):
        print("my name is ", self.name)
        print("my fathers name is ", self.fathers_name)
        print("my hobbie is ", self.hobbie)
        print("my ddress is ", self.address)


A1 = My_Intro("jdfkjhjdfh", "jdfkljaeiefu", "Playing Online games", "palsana block-A")

# print(A1.name)
A1.printing()
