a=input("enter string")
b="aeiouAEIOU"
no_of_vowels=0
no_of_consonants=0
no_of_whitespaces=0
no_of_digit=0
for i in a:
   if i in b:
     no_of_vowels +=1
   elif i.isdigit():
      no_of_digit += 1
   elif i=="\n\t ":
      no_of_whitespaces += 1
   elif i.isalpha():
      no_of_consonants +=1
print(no_of_vowels)
print(no_of_consonants) 
print(no_of_digit)  
print(no_of_whitespaces)   
         
      
      
