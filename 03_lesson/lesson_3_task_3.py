from adress import Adress
from mailing import Mailing

to_adr = Adress ("452862", "Краснохолмский", "Школьная", 2, 25)
from_adr = Adress ("344069", "Ростов-на-Дону", "Оганова", 22, 1)

mail = Mailing (to_adr, from_adr, 150, "CA123466789RU")
print (mail)
