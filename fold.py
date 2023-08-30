from functools import reduce
words=["I ","will ","be ","going ","soon "]
statement = reduce(lambda x,y: x+y, words)
print(statement)
