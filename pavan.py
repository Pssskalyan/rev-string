#rev str
def rev(s):
  str=""
  for i in s:
    str=i+str
  return str 

s=str(input())
print(rev(s))
  
