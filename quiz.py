


from tkinter import *
from PIL import ImageTk,Image
import random
import time

questions=[
    "Q.1 With which does the power to extend or restrict the jurisdiction of the High Court rest?",
    "Q.2 ‘Gobar gas’ contains mainly which gas?",
    "Q.3 Which is the biggest Public Sector undertaking in the country?",
    "Q.4 Which rocks is transformed into marble?",
    "Q.5 Which ‘Englishmen was fellow of Gandhiji in South Africa?",
    "Q.6 By which number the quality of gasoline’ sample is determined?",
    "Q.7 Due to bite of mad dog the disease hydrophobia is caused by which virus?",
    "Q.8 Who appoints the Chief Election Commissioner of India?",
    "Q.9 What is the principal reason for the formation of metamorphic rocks?",
    "Q.10 Who said “I therefore want freedom immediately, this very night, before dawn if it can be had”?",
]

answers_choice=[
    ["With the Parliament","With the Legislative","With the Council of Minister","With the Rajya Sabha"],
    ["Methane","Hydrogen","Oxygen","Silicon"],
    ["Buses","IT Sector","Railways","Banking Sector"],
    ["Grenite","Black stone","Red stone","Limestone"],
    ["John delton","Polak","Washington","Trumph"],
    ["By its octane number ","Iodine Value","Cetaine Number","Mass density"],
    ["Dengue","Chinkengunia","Cancer","Rabies virus"],
    ["Prime Minister","Deputy Minister","President ","Chief Minister"],
    ["Extreme pressure ad heat","Extreme heat and pressure","Extreme heat","Extreme pressure"],
    ["Mahatma Gandhi","Jawahar Lal Nehru","Ravindra Nath Tagore","Bal Gangadhar Tilak"],
]

user_answer=[]

answers=[0,0,2,3,1,0,3,2,1,0]

indexes=[]

def gen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
            
def showresult(score):
    lbl2.destroy()
    lbl1.destroy()
    next_btn.destroy()
    label_Question.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    
    labelimage=Label(
        root,
        width=300,
        height=300,
        background="#ffffff",
        border=0
        
    )
    labelimage.pack()
    
    labelresulttext=Label(
        root,
        font=("Consolas",20),
        background="#ffffff"
    )
    labelresulttext.pack()
    
    if score>=20:
        img=ImageTk.PhotoImage(Image.open("excellent.png"))
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.config(text="You are excellent,Perfect score")
    
    elif(score>=10 and score <20):
        img=ImageTk.PhotoImage(Image.open("good.png"))
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.config(text="You can be better next time")
    else:
        img=ImageTk.PhotoImage(Image.open("sad.png"))
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.config(text="You should work hard")
    

def calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x]==answers[i]:
            score=score+5
        x+=1
    
    showresult(score)
    label_score=Label(root,text="You Have Scored : "+str(score),font=("Comic sans MS",18,"bold"),background="#ffffff")
    label_score.pack()
        
            
            
ques=1
def selected():
    global radio_var,user_ansewer,label_Question,r1,r2,r3,r4,ques,next_btn
    x=radio_var.get()
    user_answer.append(x)
    radio_var.set(-1)
    if ques<5:
        #show next question
        label_Question.config(text=questions[indexes[ques]])
        r1['text']=answers_choice[indexes[ques]][0]
        r2['text']=answers_choice[indexes[ques]][1]
        r3['text']=answers_choice[indexes[ques]][2]
        r4['text']=answers_choice[indexes[ques]][3]
        ques+=1
        countDown()
    else:
        calc()
            
            
            
def startquiz():
    global label_Question,r1,r2,r3,r4,next_btn
    global lbl1,lbl2
    lbl2 = Label(text="Time Remaining : ",font=("Times",18),background="#ffffff")
    lbl2.pack(pady=(40,0))
    lbl1 = Label(font=("Times",18),background="#ffffff")
    lbl1.pack()
    label_Question=Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas",16),
        width=500,
        wraplength=400,
        justify="center",
        background="#ffffff",
    )
    label_Question.pack(pady=(100,40))
    
    global radio_var
    radio_var=IntVar()
    radio_var.set(-1)
    
    r1=Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times",14),
        value=0,
        variable=radio_var,
        background="#ffffff",
        
    )
    r1.pack()
    
    r2=Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times",14),
        value=1,
        variable=radio_var,
        background="#ffffff",

    )
    r2.pack()
    
    r3=Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times",14),
        value=2,
        variable=radio_var,
        background="#ffffff",
    )
    r3.pack()
    
    r4=Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times",14),
        value=3,
        variable=radio_var,
        background="#ffffff",
    )
    r4.pack()
    
    next_btn=Button(root,text="Next",width=10,height=1,background="#ffee58",font=("Consolas",18),relief=FLAT,border=0,command=selected)
    next_btn.pack(pady=(40,0))
    
    countDown()
    
    
    

def start():
    Labeltext.destroy()
    label_img.destroy()
    label_inst.destroy()
    label_rules.destroy()
    btn_start.destroy()
    gen()
    startquiz()
     
def countDown():
    global lbl1
    for k in range(180, 0, -1):
        lbl1["text"] = k
        root.update()
        time.sleep(1)

        
root=Tk()
root.title("Quizee")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

img1=ImageTk.PhotoImage(Image.open("q3.png"))
label_img=Label(root,image=img1,width=220,height=160,background="#ffffff",border=0)
label_img.pack(pady=(40,0))

Labeltext=Label(root,text="Quiz App",font=("Comic sans MS",24,"bold"),background="#ffffff")
Labeltext.pack(pady=(20,0))


btn_start=Button(root,text="START",width=10,height=1,background="#ffee58",font=("Consolas",18),relief=FLAT,border=0,command=start)
btn_start.pack(pady=(30,10))


label_inst=Label(root,text="Read The Rules And\nClick Once You Are Ready",background="#ffffff",font=("Consolas",14),justify="center")
label_inst.pack(pady=(10,90))

label_rules=Label(
    root,
    text="This Quiz contains 10 questions\nYou will get 180 seconds to solve a question\nOnce you select a option that will be your final choice\nHence think before you select",
    width=100,
    font=("Times",15),
    background="#212121",
    foreground="#ffee58"  
)
label_rules.pack()

root.mainloop()


# 
# 

# In[ ]:




