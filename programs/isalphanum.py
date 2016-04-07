# Enter your code here. Read input from STDIN. Print output to STDOUT
txt1 = raw_input()
txt = list(txt1)
num = False
alpha = False
lower = False
alpha_num = False
for i in txt:
    if i.isdigit():
        num = True
        break
alpha_bet = [x for x in txt if x.isalpha()]
if txt1.isalnum():
    alpha_num = True
if txt1.isalpha():
    for i in alpha_bet:
        if i.islower():
            lower = True
        else:
            upper = False
            
print txt1.isalnum()
print txt1.isalpha()
print num
print
print upper