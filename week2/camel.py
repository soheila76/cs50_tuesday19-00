user=input("enter camelcase:").strip()
print("snack_case:",end="")
for i in user:
    if i.islower():
        print(i,end="")
    elif i.isupper():
        print("_",i.lower(),end="",sep="")

print()
