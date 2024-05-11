user=input("enter : ").strip().lower().split(".")
application=["zip","pdf"]
image=["png","gif"]

if user[-1] in application:
    print(f"application/{user[-1]}")
elif user[-1] in image :
    print(f"image/{user[-1]}")
elif user[-1] == "txt":
    print("text/plain")
elif user[-1] == "jpg" or user[-1]=="jpeg":
    print("image/jpeg")
else:
    print("application/octet-stream")
