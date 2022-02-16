special_char = ['!','@','#','$','%','^','&','*','(',')','+','-']

keye = input('informe a senha: ')
missing_size = 6 - len(keye)
missing_char = 4

control = 0

for i in list(keye):
    if '0' <= i <= '9':
        if(control & 1)!=1:
            control = control|1
            missing_char -= 1
            
    elif 'a' <= i <= 'z':
        if(control & 2)!=2:
            control = control|2
            missing_char -= 1
            
    elif 'A' <= i <= 'Z':
        if(control & 4)!=4:
            control = control|4
            missing_char -= 1
            
    elif i in special_char:
        if(control & 8)!=8:
            control = control|8
            missing_char -= 1
            
    if missing_char == 0:
        break
    
if missing_size > 0 and missing_size > missing_char:
        missing_char = missing_size
        
print(missing_char)
