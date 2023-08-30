numbers=[34.6,-203.4,44.9,68.3,-12.2,44.6,12.7]
x=[(number) for number in numbers if number>0]
print(x)

#y =[]
#for number in numbers:
  #  if number > 0:
 #       y.append(number)
#print(y)


num =[12,54,33,67,24,89,11,24,47]
y= [(E) for E in num if E%2==0]
print(y)

words=["hello","my","name","is","Sam"]
tup= [(word.upper(), len(word)) for word in words]
print(tup)