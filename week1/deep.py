true_word=["42","forty two","forty-two"]
user=input("enter:").lower().strip()
if user in true_word:
    print("Yes")
else:
    print("No")
