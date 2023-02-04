import json
def get_used_username():
    try:
        fp= open('username.json','r',encoding='utf8')
        return json.load(fp)
    except FileNotFoundError:
        #if can't find this file,make sure return a FAUSE
        return 0

def get_new_username():
    username=input("what's your name?\n")
    fp=open('username.json','w',encoding='utf8')
    json.dump(username,fp)
    return username

def confirm(username):
    print("is "+username+" your name?[y/n]")
    in_result=input()
    if(in_result=='y'):
        print("hello!"+ username)
        return None
    elif(in_result=='n'):
        username=get_new_username()
        print("hello!"+username)
    else:
        #if the input is illegal
        #reuse this function until the user give a right input
        print("warn input!\n")
        confirm(username)

def greet_user():
    username=get_used_username()
    #if haven't done this before,the function get_new_username will return 0
    if(username):
        confirm(username)
    else:
        username=get_new_username()
        print("hello!"+username)
#start running!
greet_user()