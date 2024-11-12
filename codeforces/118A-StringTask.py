def deleteVowelsAndAddPoints(string):
  def isVowel(char):
    return char.lower() in "aoyeui"
  
  newString = ""
  for char in string:
    if not isVowel(char):
      newString += "." + char.lower()

  return newString

string = input()
print(deleteVowelsAndAddPoints(string))