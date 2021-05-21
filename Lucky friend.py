from tkinter import*
import random


root=Tk()

root.title("My Lucky Friend")
root.geometry("600x600")

list_name = ["Avni" , "Tanishka" , "Aahana" , "Bhoomi" , "Yanshi"]
print(list_name)

def random_name():
    random_no = random.randint(0 , 4)
    print(random_no)
    random_name1 = list_name[random_no]
    print("My Lucky Friend is " + random_name1)
    

bt_name = Button(root,text="Who is the lucky friend? " , command=random_name)
bt_name.place(relx = 0.5 , rely = 0.5 , anchor=CENTER)

root.mainloop()