import time
class GestureFilter():
    def __init__(self):
        self.dict = {}
        self.value = None

    def gestureUpdater(self,gesture):
        if gesture != 0:
            # print(self.dict)
            if gesture in list(self.dict.keys()):
                self.dict[gesture] += 1
                return
            self.dict[gesture] = 1
            # print(self.dict)


    def filter(self):
        while True:
            time.sleep(5)
            if len(self.dict) > 0:
                self.value = list(self.dict.keys())[list(self.dict.values()).index(max(list(self.dict.values())))]
                #    print(self.dict)
                self.dict = {}
          
    def getValue(self):
        while True:
            time.sleep(5)
            print(self.value)
