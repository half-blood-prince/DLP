import tkinter as tk
root = tk.Tk()
root.geometry('500x500')
root.title('Tkinterhub')
options_fm = tk.Frame(root)
count = 0
# Switch Funtion
def switch(indicator_lb,page):

    for child in options_fm.winfo_children():
        if isinstance(child,tk.Label):
            child['bg'] = 'SystemButtonFace'

    indicator_lb['bg'] = '#0097e8'

    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()
    page()

# Home Button
home_btn = tk.Button(options_fm,text='Home', font=('Arial',13),
                     bd=0,fg='#0097e8',activebackground="#0097e8",
                     command=lambda: switch(indicator_lb=home_indicator_lb,
                     page=home_page))
home_btn.place(x=0,y=0,width=125)

# Home Indicator
home_indicator_lb = tk.Label(options_fm,bg='#0097e8')
home_indicator_lb.place(x=22,y=30,width=80,height=2)

# Product Button
product_btn = tk.Button(options_fm,text='Products', font=('Arial',13),
                     bd=0,fg='#0097e8',activebackground="#0097e8",
                     command=lambda: switch(indicator_lb=product_btn_indicator_lb,
                     page=product_page))
product_btn.place(x=125,y=0,width=125)

# Product Indicator
product_btn_indicator_lb = tk.Label(options_fm)
product_btn_indicator_lb.place(x=147,y=30,width=80,height=2)

# Contact Button
contact_btn = tk.Button(options_fm,text='Contact', font=('Arial',13),
                     bd=0,fg='#0097e8',activebackground="#0097e8",
                     command=lambda: switch(indicator_lb=contact_indicator_lb,
                     page=contact_page))
contact_btn.place(x=250,y=0,width=125)

#Contact_Indicator
contact_indicator_lb = tk.Label(options_fm)
contact_indicator_lb.place(x=272,y=30,width=80,height=2)

# About Button
about_btn = tk.Button(options_fm,text='About', font=('Arial',13),
                     bd=0,fg='#0097e8',activebackground="#0097e8",
                     command=lambda: switch(indicator_lb=about_indicator_lb,
                     page=about_page))
about_btn.place(x=375,y=0,width=125)

#About Indicator
about_indicator_lb = tk.Label(options_fm)
about_indicator_lb.place(x=397,y=30,width=80,height=2)


options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=500,height=35)

# Home Page
def home_page():
    home_page_fm = tk.Frame(main_fm)
    # home_page_lb = tk.Label(home_page_fm,text="Home Page",
    #                         font=('Arial',25),fg='#0097e8')
    
    # number_of_inputs=2 # Number of entries required 
    # ref=[] # to store the references 
    # for j in range(number_of_inputs):
    #     l=tk.Label(home_page_fm,text='Entry: '+str(j+1),font=20,fg='blue')
    #     l.grid(row=j,column=0,padx=3)

    #     e = tk.Entry(home_page_fm, font=20,bg='lightyellow') 
    #     e.grid(row=j, column=1,padx=10,pady=3) 

    #     ref.append(e) # store references 
    # def my_check():
    #     my_flag=False
    #     for w in ref:
    #         if(len(w.get())<3):
    #             #print(w.get())
    #             my_flag=True
    #     if(my_flag==False):
    #         l1.config(text="Form can be submitted",fg='green')
    #     else:
    #         l1.config(text="Fill all the entries",fg='red' )
    #     l1.after(3000, lambda: l1.config(text=''))
    # b1=tk.Button(home_page_fm,text='Submit',
    # bg='lightgreen',command=lambda: my_check(),font=18)
    # b1.grid(row=j+1,column=0,padx=3,pady=5)
    # l1=tk.Label(home_page_fm,text='Output here',font=20) # display message
    # l1.grid(row=j+1,column=1)

    # Page 1
    page_1 = tk.Frame(main_fm)
    # page_1_lb = tk.Label(page_1,text="Start Page",font=('Bold',20))    
    number_of_inputs=2 # Number of entries required 
    ref=[] # to store the references 
    for j in range(number_of_inputs):
        l=tk.Label(page_1,text='Entry: '+str(j+1),font=20,fg='blue')
        l.grid(row=j,column=0,padx=3)

        e = tk.Entry(page_1, font=20,bg='lightyellow') 
        e.grid(row=j, column=1,padx=10,pady=3) 

        ref.append(e) # store references 
    def my_check():
        my_flag=False
        for w in ref:
            if(len(w.get())<3):
                #print(w.get())
                my_flag=True
        if(my_flag==False):
            l1.config(text="Form can be submitted",fg='green')
        else:
            l1.config(text="Fill all the entries",fg='red' )
        l1.after(3000, lambda: l1.config(text=''))
    b1=tk.Button(page_1,text='Submit',
    bg='lightgreen',command=lambda: my_check(),font=18)
    b1.grid(row=j+1,column=0,padx=3,pady=5)
    l1=tk.Label(page_1,text='Output here',font=20) # display message
    l1.grid(row=j+1,column=1)
    # page_1_lb.pack()

    page_1.pack(pady=100)

    # Page 2
    page_2 = tk.Frame(main_fm)
    page_2_lb = tk.Label(page_2,text="Second Page",font=('Bold',20))
    page_2_lb.pack()

    # Page 3
    page_3 = tk.Frame(main_fm)
    page_3_lb = tk.Label(page_3,text="Third Page",font=('Bold',20))
    page_3_lb.pack()

    # Page 4
    page_4 = tk.Frame(main_fm)
    page_4_lb = tk.Label(page_4,text="Fifth Page",font=('Bold',20))
    page_4_lb.pack()
    bottom_frame = tk.Frame(main_fm)
    pages = [page_1,page_2,page_3,page_4]
    def move_next_page():
        global count
        if not count > len(pages)-2:
            for p in pages:
                p.pack_forget()
            count+=1
            page = pages[count]
            page.pack(pady=100)
    def move_back_page():
        global count
        if not count ==0:
            for p in pages:
                p.pack_forget()
            count-=1
            page = pages[count]
            page.pack(pady=100)
    back_btn = tk.Button(bottom_frame,text="Back",
                         font=("Bold",12),
                         bg='#1877f2',fg="white",width=8,
                         command=move_back_page)
    back_btn.pack(side=tk.LEFT,padx=10)
    next_btn = tk.Button(bottom_frame,text="Next",
                         font=("Bold",12),
                         bg="#1877f2",fg="white",width=8,
                         command=move_next_page)
    next_btn.pack(side=tk.RIGHT,padx=10)
    bottom_frame.pack(side=tk.BOTTOM,pady=10)
    


    home_page_fm.pack(fill=tk.BOTH,expand=True)

# Product Page
def product_page():
    product_page_fm = tk.Frame(main_fm)
    product_page_lb = tk.Label(product_page_fm,text="Product Page",
                            font=('Arial',25),fg='#0097e8')
    product_page_lb.pack(pady=80)
    product_page_fm.pack(fill=tk.BOTH,expand=True)

# Contact Page
def contact_page():
    contact_page_fm = tk.Frame(main_fm)
    contact_page_lb = tk.Label(contact_page_fm,text="Contact Page",
                            font=('Arial',25),fg='#0097e8')
    contact_page_lb.pack(pady=80)
    contact_page_fm.pack(fill=tk.BOTH,expand=True)

# About Page
def about_page():
    about_page_fm = tk.Frame(main_fm)
    about_page_lb = tk.Label(about_page_fm,text="About Page",
                            font=('Arial',25),fg='#0097e8')
    about_page_lb.pack(pady=80)
    about_page_fm.pack(fill=tk.BOTH,expand=True)
    
main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH,expand=True)

home_page()

root.mainloop()





