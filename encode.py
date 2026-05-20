def encode(msg):
    if not msg:
        return """"""
    result = []
    count = 1
    for i in range(1,len(msg)):
        if msg[i]==msg[i-1]:
            count += 1
        else:
            result.append( msg[i-1]+str(count)) 
            count = 1

    result.append(msg[-1]+str(count))
    return "".join(result)
print(encode("AAAABBCCDA"))