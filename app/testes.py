from datetime import date
from random import randint


dataSeed=date.today()
range=9
novaData = date.fromordinal(dataSeed.toordinal() + randint(-range, range))  # hoje + 45 dias</pre>
print(novaData)

dataord = date.toordinal(novaData)

print(dataord)
dataord += 5
print(date.fromordinal(dataord))


print(1145/365)




