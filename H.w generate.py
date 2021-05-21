from tkinter import*
import random


root=Tk()

root.title("My Lucky Friend")
root.geometry("600x600")

alpha_list = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
print(alpha_list)

label_word = Label(root , text = "")

def random_word():
    random_no1 = random.randint(0 , 25)
    random_no2 = random.randint(0 , 25)
    random_no3 = random.randint(0 , 25)
    random_no4 = random.randint(0 , 25)
    random_no5 = random.randint(0 , 25)
    
    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    
    label_word["text"]= random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    
    

bt_name = Button(root,text="Generate word " , fg = "black" , bg = "pink" , command=random_word)
bt_name.place(relx = 0.5 , rely = 0.5 , anchor=CENTER)

root.mainloop()