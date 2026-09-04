from datetime import datetime

# %y 年，%Y 年，%m 月，%d 日，%H 时，%M 分，%S 秒
now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print(now)