#string slicling

text = "Kodnest"
print(text[2:2]) #empty

print("Original String:", text)
print("--------------------------------")

# POSITIVE INDEX SLICING
print("Q1:", text[0:4])    
print("Q2:", text[1:5])    
print("Q3:", text[2:7])    
print("Q4:", text[3:6])    
print("Q5:", text[4:7]) 

print("--------------------------------")


# NEGATIVE INDEX SLICING
print("Q6:", text[-4:-1])  
print("Q7:", text[-7:-3])  
print("Q8:", text[-5:-2])  
print("Q9:", text[-6:-4])  
print("Q10:", text[-3:-1]) 

print("--------------------------------")


# MIXED POSITIVE & NEGATIVE
print("Q11:", text[1:-1])  
print("Q12:", text[2:-2])  
print("Q13:", text[0:-3])  
print("Q14:", text[-5:6])  
print("Q15:", text[-4:7]) 

print("--------------------------------")


# EDGE CASES
print("Q16:", text[2:2])   
print("Q17:", text[5:3])   
print("Q18:", text[10:15]) 
print("Q19:", text[-10:3]) 
print("Q20:", text[-2:5])