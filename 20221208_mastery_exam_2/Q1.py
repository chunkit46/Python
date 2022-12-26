class Clock:
    def __init__(self, initial_time: str):
        self.hr = int(initial_time[:2])
        self.min = int(initial_time[3:])

    def forward(self, minutes: int):
        self.min += minutes
        self.hr += self.min // 60
        self.hr %= 12
        self.min %= 60

    def rewind(self, minutes: int):
        self.min -= minutes
        while self.min < 0:
            self.hr -= 1
            self.min += 60
        while self.hr < 0:
            self.hr += 12

    def get_hour(self) -> int:
        return self.hr

    def get_minute(self) -> int:
        return self.min

    def reset(self):
        self.hr = 0
        self.min = 0


### Clock ###
clock = Clock('02:05')
assert (clock.get_hour()==2)
assert (clock.get_minute()==5)
clock.forward(3726)
assert (clock.get_hour()==4)
assert (clock.get_minute()==11)
clock.reset()
assert (clock.get_hour()==0)
assert (clock.get_minute()==0)
clock.forward(3219)
assert (clock.get_hour()==5)
assert (clock.get_minute()==39)
clock.rewind(3551)
assert (clock.get_hour()==6)
assert (clock.get_minute()==28)
clock.rewind(900)
assert (clock.get_hour()==3)
assert (clock.get_minute()==28)
clock.rewind(656)
assert (clock.get_hour()==4)
assert (clock.get_minute()==32)
clock.rewind(2157)
assert (clock.get_hour()==4)
assert (clock.get_minute()==35)
clock.forward(1675)
assert (clock.get_hour()==8)
assert (clock.get_minute()==30)
clock.forward(2534)
assert (clock.get_hour()==2)
assert (clock.get_minute()==44)
clock.rewind(1670)
assert (clock.get_hour()==10)
assert (clock.get_minute()==54)
clock = Clock('11:35')
assert (clock.get_hour()==11)
assert (clock.get_minute()==35)
clock.reset()
assert (clock.get_hour()==0)
assert (clock.get_minute()==0)
clock.forward(2842)
assert (clock.get_hour()==11)
assert (clock.get_minute()==22)
clock.forward(3356)
assert (clock.get_hour()==7)
assert (clock.get_minute()==18)
clock.reset()
assert (clock.get_hour()==0)
assert (clock.get_minute()==0)
clock.forward(3777)
assert (clock.get_hour()==2)
assert (clock.get_minute()==57)
clock.rewind(3072)
assert (clock.get_hour()==11)
assert (clock.get_minute()==45)
clock.forward(1016)
assert (clock.get_hour()==4)
assert (clock.get_minute()==41)
clock.forward(4937)
assert (clock.get_hour()==2)
assert (clock.get_minute()==58)
clock.forward(4637)
assert (clock.get_hour()==8)
assert (clock.get_minute()==15)
clock.forward(1368)
assert (clock.get_hour()==7)
assert (clock.get_minute()==3)