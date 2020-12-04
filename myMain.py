class myMainClass():
    """ text """
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def myFunc(self):
        return self.a + self.b



if __name__ == "__main__":
    mymain = myMainClass(3,5)
    print(f"Add:{mymain.myFunc()}")
