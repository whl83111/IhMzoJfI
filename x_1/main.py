from abc import ABCMeta, abstractmethod
from typing import List
from math import factorial

class SmartPhoneStrategyAbstract(object, metaclass=ABCMeta):
    '''智慧型手機抽象類別

    參考 Strategy pattern 實作類似 interface 的抽象類別
    '''
    
    def __init__(self, price: int, camera_count: int, screen_size: int):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    @abstractmethod
    def special_feature(self):
        '''特殊功能'''
        return NotImplemented


class GooglePhoneStrategy(SmartPhoneStrategyAbstract):
    def __init__(self):
        price = 10
        camera_count = 3
        screen_size = 5
        super().__init__(price, camera_count, screen_size)
    
    @staticmethod
    def __filter(num: int) -> int:
        '''篩選偶數且大於 10 的元素'''
        return (num % 2 == 0) and (num > 10)
    
    def special_feature(self, inputList: List[int]) -> List[int]:
        '''輸入一個 int list, 回傳偶數且大於 10 的元素，並由大至小進行排序
        
        例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]
        '''
        return sorted(filter(GooglePhoneStrategy.__filter, inputList), key=int, reverse=True)

class TaiwanPhoneStrategy(SmartPhoneStrategyAbstract):
    def __init__(self):
        price = 20
        camera_count = 1
        screen_size = 3
        super().__init__(price, camera_count, screen_size)

    @staticmethod
    def __FibonacciGenerator() -> int:
        '''斐波那契數列生成器'''
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b
    
    def special_feature(self, inputInt: int) -> int:
        '''輸入一個數字自動回傳 Fibonacci 斐波那契數列的運算結果

        例如: 輸入 33 回傳 3524578
        '''
        generator = TaiwanPhoneStrategy.__FibonacciGenerator()
        output = None
        for _ in range(inputInt):
            output = next(generator)
        return output

class ApplePhoneStrategy(SmartPhoneStrategyAbstract):
    def __init__(self):
        price = 30
        camera_count = 2
        screen_size = 10
        super().__init__(price, camera_count, screen_size)

    def special_feature(self, x: int, y: int) -> int:
        '''輸入2個數字自動運算 p x 取 y 
        
        例如: 輸入(x=5, y=3)  回傳 60
        '''
        return int(factorial(x) / factorial(x - y))

if __name__ == "__main__":
    googlePhone = GooglePhoneStrategy()
    print(googlePhone.special_feature([3, 43, 62, 15, 18, 22]) == [62, 22, 18])
    taiwanPhone = TaiwanPhoneStrategy()
    print(taiwanPhone.special_feature(33) == 3524578)
    applePhone = ApplePhoneStrategy()
    print(applePhone.special_feature(x=5, y=3) == 60)