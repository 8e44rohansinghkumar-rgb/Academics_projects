email=input("enter your email")
index=email.index("@")
Username=email[0:index]
Domain_name=email[index:]
print(Username,end=" ")
print(Domain_name)