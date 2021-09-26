import linecache
from random import randrange  

num = randrange(59)
particular_line = linecache.getline('quotes.txt', num)
text = str(particular_line)
  
print(text)