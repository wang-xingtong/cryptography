cipher = "NUFECMWBYUJMBIQGYNBYWIXY"

for k in range(1, 26):
    result = ""
    for char in cipher:
       
        if 'A' <= char <= 'Z':
            
            new_ord = ord(char) - k
           
            if new_ord < ord('A'):
                new_ord += 26
            result += chr(new_ord)
        else:
            
            result += char
    
    print(f"k={k:<2d} : {result}")