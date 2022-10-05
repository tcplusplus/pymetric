import time
from src.speed import Speed, MpS

class TestProfiling:
    '''
    pytest to check how fast our library is
    '''
    def test_creation_speed_of_metrics(self) -> None:
        before = time.time()
        for _ in range(100000):
            _ = Speed(3.0, MpS)
        total_create = time.time() - before
        before = time.time()
        for _ in range(100000):
            _ = 3.0
        total_number = time.time() - before
        ratio = total_create / total_number
        print(f'Creating Metrics is {ratio:1}x slower')

    def test_adding_speed_of_metrics(self) -> None:
        speed = Speed(3.0, MpS)
        before = time.time()
        for _ in range(100000):
            _ = speed + speed
        total_create = time.time() - before
        before = time.time()
        for _ in range(100000):
            _ = 3.0 + 3.0
        total_number = time.time() - before
        ratio = total_create / total_number
        print(f'Adding Metrics is {ratio:1}x slower')
