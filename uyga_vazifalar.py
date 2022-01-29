# 1. split methodi orqali 5 ta misol keltiring 
ismlar = input("Ismlarni kiriting: ").split(", ")
print(ismlar)

text = "Assalomu alaykum, Mening ismim Hikmatulloh".split(",")
print(text)

print("non,choy,salat".split(", "))

sonlar = input("10 ta son kiriting: ")
sonlar = sonlar.split(", ")
print(sonlar)

bozorlik_royhati = input("Royhatni yozing:").split(", ")
print(bozorlik_royhati)





# 2. 2 ta list hosil qilib ularni birlashtiring
cars_in_gm = ["Jentra", "Lacetti", "Matiz", "Kaptiva", "Spark"]
cars = ["BMW", "Toyota", "Hyundai", "Mers",]
cars.extend(cars_in_gm)
print(cars)

mevalar = ['anor', 'olma', 'banan', 'kivi', 'nok', 'gilos']
sabzavotlar = ['sabzi', 'kartoshka', 'piyoz', 'balgarski', 'baqlajon', 'ko\'k piyoz']
royhat = []
royhat.extend(mevalar)
royhat.extend(sabzavotlar)
print(royhat)


bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
maxsulot = bozorlik.pop(int(input()))
print(f"Men {maxsulot} sotib oldim")
print("Olinmagan maxsulotlar:", bozorlik)


# 3. ismlar ro’yxatini tuzib oxirgi isimning uzunligi qancha ekanligini ekranga chiqaring yani terminal yoki console
ismlar = ["Nodir", 'Aziz', 'Anvar', "Abdulloh", "Muhammad Sodiq"]
print(len(ismlar[-2]))

# 4. listning kopaytmasini toping
my_list = [[],[[10], 50], [[[[23]]]]] 
print(my_list[1][0][0] * my_list[1][1] * my_list[2][0][0][0][0])
