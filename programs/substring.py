txt = raw_input()
m_txt = raw_input()
count = 0
length = len(txt)-(len(txt)%len(m_txt))
for i in range(length):
    if m_txt == txt[i:(len(m_txt)+i)]:
        count += 1
    else:
        pass
print count