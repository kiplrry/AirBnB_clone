#!/usr/bin/python3

class User:
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __str__(self):
        return f"{self.__class__.__dict__}"
    

print(User())