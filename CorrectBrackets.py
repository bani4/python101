data=input()
#() remove
def remove_neighbour(sent):
    sent=sent.replace("()", "")
    a=sent.find('(')
    b=sent.find(')')
    if (b-a)==1 and (a!=-1 and b!=-1):
        return remove_neighbour(sent)
    else:
        return sent
#(())
data=remove_neighbour(data)
if data=="":
    print(True)
else:
    print(False)