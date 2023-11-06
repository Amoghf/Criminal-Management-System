from tkinter import*
from tkinter import ttk   #style feel
from PIL import Image, ImageTk

import mysql.connector
from tkinter import messagebox


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='CriminalManagementSystem'  # Modify the database name
        )
        self.cursor = self.conn.cursor()
class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x400')
        self.root.title('CMS Login')

        self.username = StringVar()
        self.password = StringVar()

        frame = Frame(self.root, bg='white')
        frame.place(x=150, y=100, width=300, height=200)

        title = Label(frame, text='Welcome to CMS', font=('times new roman', 20, 'bold'), bg='white', fg='blue')
        title.grid(row=0, columnspan=2, pady=20)

        lbl_user = Label(frame, text='Username:', font=('times new roman', 12, 'bold'), bg='white')
        lbl_user.grid(row=1, column=0, pady=10)
        txt_user = Entry(frame, textvariable=self.username, font=('times new roman', 12))
        txt_user.grid(row=1, column=1)

        lbl_pass = Label(frame, text='Password:', font=('times new roman', 12, 'bold'), bg='white')
        lbl_pass.grid(row=2, column=0, pady=10)
        txt_pass = Entry(frame, textvariable=self.password, font=('times new roman', 12), show='*')
        txt_pass.grid(row=2, column=1)

        btn_login = Button(frame, text='Login', command=self.login, font=('times new roman', 12, 'bold'), bg='blue', fg='white')
        btn_login.grid(row=3, columnspan=2, pady=10)



class Criminal:
    def __init__(self,root):
        self.root=root #root=window
        self.root.geometry('1530x790+0+0') #dimension of my window
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        
        #varaibles
        
        self.var_case_id=StringVar() 
        self .var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()  # all of them are added to entry feild

        #title
        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)
        
        #logo:
        img_logo=Image.open('images/logo.png')
        img_logo = img_logo.resize((60, 60), Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,height=60)
        
        
        #images frame
        
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=150)
        
        #images in frame
        img1 = Image.open('images/1.jpg')
        img1 = img1.resize((540, 160), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)

        img2 = Image.open('images/2.jpg')
        img2 = img2.resize((540, 160), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)  # Adjust the x position

        img3 = Image.open('images/3.jpg')
        img3 = img3.resize((540, 160), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1080, y=0, width=540, height=160)  # Adjust the x position

        
        #main frame 
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=0,y=220,width=1500,height=560)
        
        #insidde main frame another frame
        Upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION',font=('times new roman',11,'bold'),fg='red',bg='white')
        Upper_frame.place(x=10,y=10,width=1480,height=270)
        
        #labels Entry
        
        #case id
        caseid = Label(Upper_frame, text='Case ID:', font=('arial', 11, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, pady=2, sticky='w')

        
        caseentry=ttk.Entry(Upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,stick='w')
        
        
      # Criminal Number Label
        lbl_criminal_no = Label(Upper_frame, text='CRIMINAL NUMBER:', font=('arial', 11, 'bold'), background='white')
        lbl_criminal_no.grid(row=0, column=2, padx=2, sticky=W, pady=7)

      # Criminal Number Entry
        txt_criminal_no = ttk.Entry(Upper_frame,textvariable=self .var_criminal_no, width=22, font=('arial', 11, 'bold'))
        txt_criminal_no.grid(row=0, column=3, padx=2, sticky='w')


       #Criminal Name:
        lbl_Name = Label(Upper_frame, text='CRIMINAL Name:', font=('arial', 11, 'bold'), background='white')
        lbl_Name.grid(row=1, column=0, padx=2, sticky=W, pady=7)
        
        txt_Name = ttk.Entry(Upper_frame,textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        txt_Name.grid(row=1, column=1, padx=2, sticky='w',pady=7)
    
    
        #criminal Nickname:
        lbl_Nickname = Label(Upper_frame, text='Nickname:', font=('arial', 11, 'bold'), background='white')
        lbl_Nickname.grid(row=1, column=2, padx=2, sticky=W, pady=7)
        
        txt_Nickname = ttk.Entry(Upper_frame, textvariable=self.var_nickname,width=22, font=('arial', 11, 'bold'))
        txt_Nickname.grid(row=1, column=3, padx=2, sticky='w',pady=7)
        
        #Arrest DATE
        lbl_arrestdate= Label(Upper_frame, text='Arrest date:', font=('arial', 11, 'bold'), background='white')
        lbl_arrestdate.grid(row=2, column=0, padx=2, sticky=W, pady=7)
        
        txt_arrestdate = ttk.Entry(Upper_frame, textvariable=self.var_arrest_date,width=22, font=('arial', 11, 'bold'))
        txt_arrestdate.grid(row=2, column=1, padx=2, sticky='w',pady=7)
        
        #date of crime:
        lbl_doc= Label(Upper_frame, text='Date of Cirme:', font=('arial', 11, 'bold'), background='white')
        lbl_doc.grid(row=2, column=2, padx=2, sticky=W, pady=7)
        
        txt_doc= ttk.Entry(Upper_frame,textvariable=self.var_date_of_crime, width=22, font=('arial', 11, 'bold'))
        txt_doc.grid(row=2, column=3, padx=2, sticky='w',pady=7)
        
        #address:
        lbl_address= Label(Upper_frame, text='Address:', font=('arial', 11, 'bold'), background='white')
        lbl_address.grid(row=3, column=0, padx=2, sticky=W, pady=7)
        
        txt_address= ttk.Entry(Upper_frame, textvariable=self.var_address,width=22, font=('arial', 11, 'bold'))
        txt_address.grid(row=3, column=1, padx=2, sticky='w',pady=7)
        
        #Age:
        lbl_age= Label(Upper_frame, text='AGE:', font=('arial', 11, 'bold'), background='white')
        lbl_age.grid(row=3, column=2, padx=2, sticky=W, pady=7)
        
        txt_age= ttk.Entry(Upper_frame,textvariable=self.var_age, width=22, font=('arial', 11, 'bold'))
        txt_age.grid(row=3, column=3, padx=2, sticky='w',pady=7)
        
        #occupation
        lbl_ocu= Label(Upper_frame, text='Occupation:', font=('arial', 11, 'bold'), background='white')
        lbl_ocu.grid(row=4, column=0, padx=2, sticky=W, pady=7)
        
        txt_ocu= ttk.Entry(Upper_frame,textvariable=self.var_occupation, width=22, font=('arial', 11, 'bold'))
        txt_ocu.grid(row=4, column=1, padx=2, sticky='w',pady=7)
        
        #Birthmark
        lbl_bm= Label(Upper_frame, text='BirthMark:', font=('arial', 11, 'bold'), background='white')
        lbl_bm.grid(row=4, column=2, padx=2, sticky=W, pady=7)
        
        txt_bm= ttk.Entry(Upper_frame, textvariable=self.var_birthmark,width=22, font=('arial', 11, 'bold'))
        txt_bm.grid(row=4, column=3, padx=2, sticky='w',pady=7)
        
        #crime type
        lbl_ct= Label(Upper_frame, text='CrimeType:', font=('arial', 11, 'bold'), background='white')
        lbl_ct.grid(row=0, column=4, padx=2, sticky=W, pady=7)
        
        txt_ct= ttk.Entry(Upper_frame,textvariable=self.var_crime_type, width=22, font=('arial', 11, 'bold'))
        txt_ct.grid(row=0, column=5, padx=2, sticky='w',pady=7)
        
        
        #father NAME:
        lbl_fathername= Label(Upper_frame, text='FatherName:', font=('arial', 11, 'bold'), background='white')
        lbl_fathername.grid(row=1, column=4, padx=2, sticky=W, pady=7)
        
        txt_fathername= ttk.Entry(Upper_frame,textvariable=self.var_father_name, width=22, font=('arial', 11, 'bold'))
        txt_fathername.grid(row=1, column=5, padx=2, sticky='w',pady=7)
        
       
        
        #most wanted:
        lbl_wanted= Label(Upper_frame, text='Most Wanted:', font=('arial', 11, 'bold'), background='white')
        lbl_wanted.grid(row=3, column=4, padx=2, sticky=W, pady=7)
        
        
        #image in upper frame image:background roght side image
        
        img4 = Image.open('images/4.jpg')
        img4 = img4.resize((470, 245), Image.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(img4)

        self.img_4 = Label(Upper_frame, image=self.photo4)
        self.img_4.place(x=1000, y=0, width=470, height=245)

        
        # gender radio frame
        radio_frame_gender = Frame(Upper_frame, bd=2, relief='ridge', bg='white')
        radio_frame_gender.place(x=750, y=85, width=190, height=40)
        
         #gender:
        lbl_gender= Label(Upper_frame, text='Gender:', font=('arial', 11, 'bold'), background='white')
        lbl_gender.grid(row=2, column=4, padx=2, sticky=W, pady=7)
        
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',12,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')
        
        female = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Female', value='female', font=('arial', 12, 'bold'), bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)


        # most wanted radio frame
        radio_frame_wanted = Frame(Upper_frame, bd=2, relief='ridge', bg='white')
        radio_frame_wanted.place(x=760, y=130, width=190, height=40)
        
        Yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='Yes',font=('arial',12,'bold'),bg='white')
        Yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        self.var_wanted.set('Yes')
        
        
        No=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='No',font=('arial',12,'bold'),bg='white')
        No.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        #buttons
        button_frame=Frame(Upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)
        
        #add button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)
        
        #update button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
        
        
        #delete button
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)
        
        
        #clear button 
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)
        
        
        
        
        
        
        
        
         
        
        
        #down frame
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION TABLE',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)
        
        #inside downframe new frame
        
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text=' SEARCH CRIMINAL RECORD',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=10,y=0,width=1470,height=60)
        
        lbl_search_by = Label(search_frame, text='Search By:', font=('arial', 11, 'bold'), background='red', fg='white')
        lbl_search_by.grid(row=0, column=0, padx=2, sticky='w', pady=7)

        self.var_com_search=StringVar()
        
        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search,font=('arial', 11, 'bold'), width=18, state='readonly')
        combo_search_box['values'] = ('Select Option', 'Case_id', 'Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, padx=5, sticky='w')

        self.var_search=StringVar()
        search_txt = ttk.Entry(search_frame,textvariable=self.var_search, width=18, font=('arial', 11, 'bold'))
        search_txt.grid(row=0, column=2, padx=2, sticky='w')

        # Search button
        btn_search = Button(search_frame,command=self.search_data, text='Search', font=("arial", 13, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=3, pady=5)

        # Show all button
        btn_all = Button(search_frame, command=self.fetch_data,text='Show All', font=("arial", 13, 'bold'), width=14, bg='blue', fg='white')
        btn_all.grid(row=0, column=4, padx=3, pady=5)

        crimeagency = Label(search_frame, text='National Cirme Agency', font=('arial', 30, 'bold'), background='white', fg='crimson')
        crimeagency.grid(row=0, column=5, padx=50, sticky='w',pady=0)

        
        
        # to make table
       
        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        # Create horizontal and vertical scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nickename')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='CrimeOfDate')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')
        
        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=100)
        
        self.criminal_table.pack(fill=BOTH,expand=1)
        
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #Add Function
    def add_data(self):
      if self.var_case_id.get()=="":
        messagebox.showerror('Error','All Info is required',parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host='localhost',username='root',password='Amogh123',database='criminal_management')
          #there is a cursor in sql used to excute al  query
          my_cursor=conn.cursor()
          my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
            
                                                                            self.var_case_id.get(), 
                                                                            self .var_criminal_no.get(),
                                                                            self.var_name.get(),
                                                                            self.var_nickname.get(),
                                                                            self.var_arrest_date.get(),
                                                                            self.var_date_of_crime.get(),
                                                                            self.var_address.get(),
                                                                            self.var_age.get(),
                                                                            self.var_occupation.get(),
                                                                            self.var_birthmark.get(),
                                                                            self.var_crime_type.get(),
                                                                            self.var_father_name.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_wanted.get()

                                                                                                      ))
          conn.commit()
          self.fetch_data()
          self.clear_data()
          conn.close()
          messagebox.showinfo('Success','Criminal record has ben added')
        
        except Exception as es:
          messagebox.showerror('Error',f'due to{str(es)}')
         
    #fetch data
    def fetch_data(self):
          conn=mysql.connector.connect(host='localhost',username='root',password='Amogh123',database='criminal_management')
          my_cursor=conn.cursor()
          my_cursor.execute('select * from criminal')
          data=my_cursor.fetchall()
          if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
              self.criminal_table.insert('',END,values=i)
            conn.commit()
            
          conn.close()
    
    #get cursor
    def get_cursor(self,event=""):
      cursor_row=self.criminal_table.focus()
      content=self.criminal_table.item(cursor_row)
      data=content['values']
      
      
      self.var_case_id.set(data[0])
      self .var_criminal_no.set(data[1])
      self.var_name.set(data[2])
      self.var_nickname.set(data[3])
      self.var_arrest_date.set(data[4])
      self.var_date_of_crime.set(data[5])
      self.var_address.set(data[6])
      self.var_age.set(data[7])
      self.var_occupation.set(data[8])  
      self.var_birthmark.set(data[9])
      self.var_crime_type.set(data[10])
      self.var_father_name.set(data[11])
      self.var_gender.set(data[12])
      self.var_wanted.set(data[13])      
      
           
    # update
    def update_data(self):
      if self.var_case_id.get()=="":
        messagebox.showerror('Error','All Info is required',parent=self.root)
      else:
        try:
          update=messagebox.askyesno('Update','are you sure wanna update this criminal record')
          if update>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Amogh123',database='criminal_management')
            my_cursor=conn.cursor()
            my_cursor.execute('update criminal set  Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(
              
              
                                                                            self .var_criminal_no.get(),
                                                                            self.var_name.get(),
                                                                            self.var_nickname.get(),
                                                                            self.var_arrest_date.get(),
                                                                            self.var_date_of_crime.get(),
                                                                            self.var_address.get(),
                                                                            self.var_age.get(),
                                                                            self.var_occupation.get(),
                                                                            self.var_birthmark.get(),
                                                                            self.var_crime_type.get(),
                                                                            self.var_father_name.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_wanted.get(),
                                                                            self.var_case_id.get()
              
            ))
          else:
            if not update:
              return
          conn.commit()
          self.fetch_data()
          self.clear_data()
          conn.close()
          messagebox.showinfo('Sucess','Criminal record has beeen updated')
        except Exception as es:
          messagebox.showerror('Error',f'due to{str(es)}')
         
    
    #deelte 
    def delete_data(self):
      if self.var_case_id.get()=="":
        messagebox.showerror('Error','A;ll feilds are required ')
      else:
        try:
          delete=messagebox.askyesno('delete','are you sure wanna delete this criminal record')
          if delete>0:
            conn=mysql.connector.connect(host='localhost',username='root',password='Amogh123',database='criminal_management')
            my_cursor=conn.cursor()
            sql='delete from criminal where Case_id=%s'
            value=(self.var_case_id.get(),)
            my_cursor.execute(sql,value)
          else:
            if not delete:
              return
          conn.commit()
          self.fetch_data()
          self.clear_data()
          conn.close()
          messagebox.showinfo('Success','Criminal record succecfluu deleted')
        except Exception as es:
          messagebox.showerror('Error',f'due to{str(es)}') 
          
    #clear
    def clear_data(self):
      self.var_case_id.set("")
      self .var_criminal_no.set("")
      self.var_name.set("")
      self.var_nickname.set("")
      self.var_arrest_date.set("")
      self.var_date_of_crime.set("")
      self.var_address.set("")
      self.var_age.set("")
      self.var_occupation.set("")  
      self.var_birthmark.set("")
      self.var_crime_type.set("")
      self.var_father_name.set("")
      self.var_gender.set("")
      self.var_wanted.set("")      
    
    
    #search:
    def search_data(self):
      if self.var_com_search.get()=="":
        messagebox.showerror('error','All feilds are required')
      else:
        try:
          conn=mysql.connector.connect(host='localhost',username='root',password='Amogh123',database='criminal_management')
          my_cursor=conn.cursor()
          my_cursor.execute('select * from criminal where ' + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")

          rows=my_cursor.fetchall()
          if len(rows)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in rows:
              self.criminal_table.insert('',END,values=i)
          conn.commit()
            
          conn.close()
        except Exception as es:
          messagebox.showerror('Error',f'due to{str(es)}') 
          
    
                  
        
if __name__=="__main__":
    
    #for the window part
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
    
    
    
    
        