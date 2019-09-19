import re
import math
import speech_recognition as sr
from googletrans import Translator

# Creating custom exception.
class langexxp(Exception):
   def __init__(self, message):
       self.message = message

# choosing the language
try:
   langinp = input('In which language you want to use this calculator?')
   if langinp == "bengali" or langinp == "Bengali":
       language = "bn-IN"
   elif langinp == "hindi" or langinp == "Hindi":
       language = "hi-IN"
   elif langinp == "english" or langinp == "English":
       language = "en"
   else:
       raise langexxp("Choose any above language before proceeding")

except langexxp as e:
   print(e.message)
   exit()

def queryhandling():

   # Handling the search query using the speech recognition technique.
   r = sr.Recognizer()
   with sr.Microphone() as source:
       # listen for 3 seconds and create the ambient noise energy level
       r.adjust_for_ambient_noise(source, duration=4)
       print("\n")
       print("Welcome to the Voice calculator app,Say your query here")
       audio = r.listen(source)
       print("time over")

   try:
       str = r.recognize_google(audio, language=language)
       print(str)

   except:
       pass

   # Handling the search query
   try:
       translator = Translator()
       translations = translator.translate([str], dest='en')
       for translation in translations:
           str = translation.text

       if str:
           new_Str = str.lower()

           # print(new_Str)
           res = new_Str.find("plus")
           res1 = new_Str.find("addition")
           res2 = new_Str.find("summation")
           res3 = new_Str.find("sum")
           res4 = new_Str.find("add")
           res5 = new_Str.find("minus")
           res6 = new_Str.find("substraction")
           res7 = new_Str.find("sub")
           res8 = new_Str.find("multiply")
           res9 = new_Str.find("multiple")
           res10 = new_Str.find("multiplication")
           res20 = new_Str.find("times")
           res11 = new_Str.find("Divide")
           res12 = new_Str.find("Division")
           res13 = new_Str.find("div")
           res14 = new_Str.find("sin")
           res15 = new_Str.find("sine")
           res16 = new_Str.find("cos")
           res17 = new_Str.find("cosine")
           res18 = new_Str.find("tan")
           res19 = new_Str.find("tangent")

           if res >= 0 or res1 >= 0 or res2 >= 0 or res3 >= 0 or res4 >= 0:

               result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', new_Str)
               #print(result)
               c = 0
               for i in result:
                   c = c + float(i)
               print(c)

           elif res5 >= 0 or res6 >= 0 or res7 >= 0:

               result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', new_Str)
               #print(result)
               lis = []
               for i in result:
                   lis.append(float(i))
               # print(lis)
               cc = lis[0] - sum(lis[1:])
               print(cc)

           elif res8 >= 0 or res9 >= 0 or res10 >= 0 or res20 >= 0:

               result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', new_Str)
               #print(result)
               c = 1
               for i in result:
                   c = c * float(i)
               print(c)

           elif res11 >= 0 or res12 >= 0 or res13 >= 0:

               result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', new_Str)
               #print(result)

               lis = []
               for i in result:
                   lis.append(float(i))

               rest_lis = lis[1:]  # removing the first item from the list and then taking all the list
               # print(rest_lis) #Printing the list after removing the first item.
               c = 1
               for i in rest_lis:
                   c = c * i
               # print(c)
               final_res = lis[0] / c
               print(final_res)

           elif res16 >= 0 or res17 >= 0:
               result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', new_Str)
               for i in result:
                   print(i)
                   res = math.cos(float(i))
               print(res)

           elif res14 >= 0 or res15 >= 0:
               result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', new_Str)
               for i in result:
                   res = math.sin(float(i))
               print(res)

           elif res18 >= 0 or res19 >= 0:
               result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', new_Str)
               for i in result:
                   res = math.tan(float(i))
               print(res)
           else:
               print("Search query cannot be found")

   except:
       print("Search query cannot be found")

queryhandling()

while True:
   x=input('Do you want to continue? Yes or No')
   if x =='yes' or x =='Yes' or x =='YES':
       queryhandling()
   else:
       break
