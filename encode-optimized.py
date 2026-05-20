def encode(msg):
    result = []
    count = 0
    if not msg:
        return """"""
    for i in range(len(msg)):
        if msg[i] == msg[i-1]:
            count +=1
        else:
            result.append(msg[i-1]+str(count))
            count = 1
            
    result.append(msg[-1]+str(count))
    return " ".join(result)

obj1 = encode("AAAABBCCDA")
print(obj1)
        
