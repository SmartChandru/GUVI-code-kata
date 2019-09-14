def int_to_roman(num):
  val = [10, 9, 5, 4, 1]
  syb = ["X", "IX", "V", "IV","I"]
  res = ''
  i = 0
  while  num > 0:
    for _ in range(num // val[i]):
      roman_num += syb[i]
      num -= val[i]
      i += 1
  return res

def roman_to_int(s):
  rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  int = 0
  for i in range(len(s)):
    if s[i] not in rom.keys():
      return -1
    if i > 0 and rom[s[i]] > rom[s[i - 1]]:
      int += rom[s[i]] - 2 * rom[s[i - 1]]
      #print(rom[s[i]],rom[s[i - 1]],s[i],i,int," *")
    else:
      int += rom[s[i]]
      #print(rom[s[i]],rom[s[i - 1]],s[i],i,int," *")
  return int

r= input()
n= roman_to_int(r)
print(n)
