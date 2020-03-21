from datetime import datetime

d = input()

res = datetime.strptime(d, '%m %d %Y')

print(res.strftime('%A').upper())
