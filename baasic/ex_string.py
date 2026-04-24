#   CONVERT A STRING TO UPPER CASE

message='python programming is interesting'
upper_case=message.upper()
print(upper_case)



#REMOVE WHITESPACE FROM A STRING

msg=' Python is  amazing! '
stripped_msg=msg.strip()
print(stripped_msg)


#FIND THE POSITION OF A SUBSTRING

ms='Python is an amazing programming language'
position=ms.find('amazing')
print(position)



#CONNCATENATE  TWO STRINGS

str1='Hello'
str2=' world'
result=(str1+ str2)
print(result)

#CLACULATE THE LENGTH OF A STRING

mg='Learning Python is fun!'
length=len(mg)
print(f"length of the message is: {length}")

#REPLACE A WPRD IN A STRING

m='i love programming in java'
updated_msg=m.replace("java","Python")
print(updated_msg)


#CREATE AND PRINT A MULTI-LINE STRING

me='''Python is a powerful programming language,
it is easy to learn
it is widly used in data science,web development, and more.'''
print(me)


#SLICE A STRING TO EXTRACT SUBSTRINGS

mes='Python is an amazing language!'
part1='Pyhton'
part2='amazing language!'
part3='is'
print("part1:",part1)
print("part2:",part2)
print("part3:",part3)


#EXTRACT DATE COMPONENTS FROM A STRING 
date='2024-10-16'
year=date[0:4]
month=date[5:7]
day=date[8:10]
print("year:",year)
print("month:",month)
print("day:",day)



#SPLIT AND JOIN STRINGS

sentence='Python is a versatile programming language'
words_list=sentence.split()
hyphenated_sentence=('-'.join(words_list))
print("List of words:",words_list)
print("Hyphenated sentence:",hyphenated_sentence)


#SPLIT FULL NAME AND JOIN WITH INITIALS
full_name='Jhon Michael Doe'
name_parts=full_name.split()
first_name=name_parts[0]
middle_initial=name_parts[1][0] + "."
last_name=name_parts[2][0] + "."
initials_name=first_name + " " +middle_initial + " " +last_name
print("Name parts:",name_parts)
print("Formatted name with initials:",initials_name)

