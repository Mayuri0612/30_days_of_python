def func(text):
    print(text)


msg_template = """Hello {name},
Thank you for joining {website}. We are very happy to 
have you with us.
"""

def format_msg(my_name = "Justin", my_website = "abc.com"):
    my_msg = msg_template.format(name = my_name, website = my_website)
    #print(my_msg)
    return my_msg

names = ['A','B','C','D','E']
for x in names:
    y = format_msg(my_name=x)
    print(y)