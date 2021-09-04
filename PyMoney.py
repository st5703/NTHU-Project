import sys
from datetime import *

class Record:
	"""Represent a record."""
	def __init__(self,category,item,amount,date = date.today()):
		self._category = category
		self._item = item
		self._amount = amount
		self._date = date
	@property
	def category(self):
		return self._category

	@property
	def item(self):
		return self._item

	@property
	def amount(self):
		return self._amount

	@property
	def date(self):
		return self._date	

class Records:
	"""Maintain a list of all the 'Record's and the initial amount of money."""
	def __init__(self):
		self._current_money ,self._List  = self.check_file()
		
	@property
	def current_money(self):
		return self._current_money

	@property
	def List(self):
		return self._List

	def ini_money(self,money):
		self._current_money = money    




	def delete_tk(self,del_item,n):
		self._current_money -= int(del_item.split(' ')[3])        
		del(self._List[n])    





	def add(self,item_cost,categories):
		if (len(item_cost.split(' ')) == 3):
			item = Record(item_cost.split(' ')[0],item_cost.split(' ')[1], item_cost.split(' ')[2])
			item_cost = str(item.date)+' '+item_cost

		else:
			try:
				date.fromisoformat(item_cost.split(' ')[0])
			except ValueError:
				sys.stderr.write('The format of a record should be like this: YYYY-MM-DD')
				return self._List	

			item = Record(item_cost.split(' ')[1],item_cost.split(' ')[2],item_cost.split(' ')[3],item_cost.split(' ')[0])
		try:
			self._current_money += int(item.amount)
			if Categories.is_category_valid (item.category,categories):
				return	self._List.append(item_cost)
			else:
				print(f'\nThe specified category is not in the category list.\n\
You can check the category list by command "view categories".\nFail to add a record.')
				return self._List	
			
		# Error : salary3000 , Hot pot 300	
		except IndexError:
			sys.stderr.write('\nThe format of a record should be like this: meal breakfast -50.\
\nFail to add a record.\n\n')	
			return	self._List

		# Error : salary -asd , salary abc	
		except ValueError:
			sys.stderr.write('\nThe format of a record should be like this: meal breakfast -50.\
\nFail to add a record.\n\n')
			return	self._List	


	def view(self):
		# 1. Print all the records and report the balance.
		print('\nDate.\t      category\t      Description\tAmount')
		print('='*55)
		s = 0
		#split each item and seprate to meet the format.
		for i in self._List:
			Detail_item = i.split(' ')
			print(f'{Detail_item[0]:13s} {Detail_item[1]:<16s}{Detail_item[2]:<18s}{Detail_item[3]:<10s}\n',end = '')
			s+=1

		print('='*55)
		print ('Now you have %d dollars.\n' %self._current_money)	

	def delete(self, delete_list):
		# 1. Define the formal parameter.
		# 2. Delete the specified record from self._records.
		try:
			int(delete_list.split(' ')[3])

			# with same item	
			if (self._List.count(delete_list) > 1):
				self._current_money -= int(delete_list.split(' ')[3])
				s = 0
				print('\nNo.  Item_Name')
				print('='*20)
				for i in self._List :
					if i == delete_list:
						print(f'{s+1:<4d} {delete_list}')
					s+=1
				print('='*20)

				sequence = int(input(f'\nwhich No.\'{delete_list}\' do you want to delete? '))

				sequence = int(sequence)
				self._List.pop(sequence-1)							
				return self._List

			# Only one item
			elif (self._List.count(delete_list) == 1):
				self._current_money -= int(delete_list.split(' ')[3])			
				self._List.pop(self._List.index(delete_list))			
				return self._List		

			# No item 
			else:
				sys.stderr.write(f'There\'s no record with \'{delete_list}\'. Fail to delete a record.\n')
				return self._List	

		# Error : salary3000 , Hot pot 300				
		except IndexError:
			sys.stderr.write('Invalid format. Fail to delete a record.\n')	
			return self._List
		# Error : salary -asd , salary abc	
		except ValueError:
			sys.stderr.write('Invalid format. Fail to delete a record.\n')				
			return self._List



	def find(self,target_cat):
		if (target_cat != []):
			print('\nDate.\t      category\t      Description\tAmount')
			print('='*55)
			cat_cost = 0
			for i in self._List:
				if i.split(' ')[1] in target_cat:
					cat_cost += int(i.split(' ')[3])														
					Detail_item = i.split(' ')
					print(f'{Detail_item[0]:13s} {Detail_item[1]:<16s}{Detail_item[2]:<18s}{Detail_item[3]:<10s}\n',end = '')	
			print('='*55)
			print ('The total amount above is %d \n' %cat_cost)

		else:
			print(f'No this category.')	



	def save(self):
		with open('records.txt','w') as fh:
			fh.write(str(self._current_money)+'\n')
			for i in self._List:
				fh.writelines(i+'\n')	

                
             

	@staticmethod
	def check_file():
		try:
			fh =  open('records.txt')		

		#file not exist
		except FileNotFoundError:
			sys.stderr.write('File not found. Create New file : \'records.txt\'.\n')	
			current_money = input ('How much money do you have? ')

			#check current money if (int)
			try:
				current_money = int (current_money)
				pre_record = []

				

			# Invalid format , initialize current money to 0
			except ValueError as err:
				sys.stderr.write('Invalid value for money. Set to 0 by default.\n')	
				#Initialize current money to 0
				current_money = 0
				pre_record = []

			return current_money, pre_record

		else:
			current_money = fh.readline()

			#check current money if (int)
			try:
				current_money = int (current_money)
				print('Welcome Back!')
				pre_record = fh.readlines()

			# Invalid format , initialize current money to 0	
			except ValueError as err:
				sys.stderr.write('Invalid format in records.txt. Deleting the contents.\n')	
				current_money = input ('How much money do you have? ')

				#check current money if (int)
				try:
					current_money = int (current_money)
					pre_record = []

				except ValueError as err:
					sys.stderr.write('Invalid value for money. Set to 0 by default.\n')	
					#Initialize current money to 0
					current_money = 0
					pre_record = []

			fh.close()		

			List = []
			for i in pre_record:
				List.append(i.split('\n')[0])
				

			
			return current_money, List


class Categories:
	"""Maintain the category list and provide some methods."""

	def __init__(self):
		self._categories =  ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation',['bus', 'railway']], 'income', ['salary', 'bonus']]

	def __repr__(self):
		return f'{self._categories}'

	@property
	def categories(self):
		return self._categories
	

	def view(self):
		cat = self._categories

		def view_categories(categories,prefix = ()):
			if type(categories) in {list , tuple}:
				i = 0
				for v in categories:
					if type(categories) not in {list, tuple}:
						i+=1
					view_categories(v,prefix+(i,))	
			else:
				s = ' '*2*(len(prefix)-1)
				s+= '- '+categories
				print(s)

		view_categories(cat)


	def is_category_valid (cat,categories):
		if type(categories) in {list,tuple}:
			for i,v in enumerate(categories):
				p = Categories.is_category_valid (cat,v)
				if p == True:
					return True
				if p != False:
					return True
		return categories == cat		



	def find_subcategories(self,category):

		def find_sub(category, categories):
			if type(categories) == list:
				for v in categories:
					p = find_sub(category, v)
					if p == True:
						index = categories.index(v)
						if index + 1 < len(categories) and \
								type(categories[index + 1]) == list:
							return self._flatten(categories[index:index + 2])
						else:
							return [v]
					if p != []:
						return p
			return True if categories == category else []

		return find_sub(category,self._categories)
  

	def _flatten(self,L):		
			if type(L) == list:
				result = []
				for child in L:
					result.extend(self._flatten(child))
				return result
			else:
				return [L]
   
#####################################




def addtolist():
	date_var = date_ent.get()
	if (date_var ==''):
		date_var = str(date.today())
	cat_vat = cat_ent.get()
	des_var = des_ent.get()
	amount_vat = amount_ent.get()
	record = date_var+' '+cat_ent.get()+' '+des_ent.get()+' '+amount_ent.get()
	records.add(record,categories.categories)
	if record == records.List[-1]:
		lb.insert('end',record)
		cur_mon_var.set(f'Now you have {records.current_money} dollars')     
    
def update_ini_money():
	ini_money = ini_ent.get()
	records.ini_money(int(ini_money))    
	cur_mon_var.set(f'Now you have {records.current_money} dollars') 

def find_category():
	cat = find_ent.get()
	target_cat = categories.find_subcategories(cat)
	cat_cost = 0
	lb.delete(0,len(records.List))
	for i in records.List:
		if i.split(' ')[1] in target_cat:
			cat_cost += int(i.split(' ')[3])
			lb.insert('end',i)    
			cur_mon_var.set(f'Total cost {cat_cost} dollars')
            
def reset():
	lb.delete(0,len(records.List))
	for i in records.List:
		lb.insert('end',i)
	cur_mon_var.set(f'Now you have {records.current_money} dollars') 

        
def del_item():
	delete_item = lb.get(lb.curselection())   
	records.delete_tk(delete_item,lb.curselection()[0])    
	lb.delete(0,len(records.List))
	for i in records.List:
		lb.insert('end',i)
	cur_mon_var.set(f'Now you have {records.current_money} dollars')         


def save():
	with open('records.txt','w') as fh:
		fh.write(str(records._current_money)+'\n')
		for i in records._List:
			fh.writelines(i+'\n')	
    
    
    
    
############################

  
    
import tkinter
root = tkinter.Tk()
root.title('Pymoney')
root.geometry('1000x500')

#####################
find_lab = tkinter.Label(root, text='Find category')
find_lab.grid(row= 0 ,column=0)

ini_lab = tkinter.Label(root, text='Initial money')
ini_lab.grid(row= 0 ,column=4)

Date_lab = tkinter.Label(root, text='Date')
Date_lab.grid(row= 2 ,column=4)

cat_lab = tkinter.Label(root, text='Category')
cat_lab.grid(row= 3 ,column=4)

des_lab = tkinter.Label(root, text='Description')
des_lab.grid(row= 4 ,column=4)

amount_lab = tkinter.Label(root, text='Amount')
amount_lab.grid(row= 5 ,column=4)



###########################
  
find_bot=tkinter.Button(root,text="Find",width=3,height=1,command = find_category)
find_bot.grid(row= 0 ,column=2)

reset_bot=tkinter.Button(root,text="Reset",width=4,height=1,command = reset)
reset_bot.grid(row= 0 ,column=3)

update_bot=tkinter.Button(root,text="Update",width=6,height=1,command = update_ini_money)
update_bot.grid(row= 0 ,column=7)

add_bot=tkinter.Button(root,text="Add a record",width=10,height=1,command=addtolist)
add_bot.grid(row=6 ,column=5)

del_bot=tkinter.Button(root,text="Delete",width=10,height=1,command = del_item)
del_bot.grid(row= 6 ,column=2)

quit_bot=tkinter.Button(root,text="Quit",width=10,height=1,command=root.destroy)
quit_bot.grid(row= 6 ,column=8)

save_bot=tkinter.Button(root,text="Save",width=10,height=1,command=save)
save_bot.grid(row= 4 ,column=8) 


##########################
find_ent = tkinter.Entry(root,width=40,findvariable = None)
find_ent.grid(row= 0 ,column=1)

ini_ent = tkinter.Entry(root,inivariable = None)
ini_ent.grid(row= 0 ,column=5)

date_ent = tkinter.Entry(root,datevariable = None)
date_ent.grid(row=2 ,column=5)

cat_ent = tkinter.Entry(root,catvariable = None)
cat_ent.grid(row=3 ,column=5)

des_ent = tkinter.Entry(root,desvariable = None)
des_ent.grid(row=4 ,column=5)

amount_ent = tkinter.Entry(root,amountvariable = None)
amount_ent.grid(row=5 ,column=5)
############################


lb=tkinter.Listbox(root,width=40, height=20)
lb.grid(row=1 ,column=1)


############################

categories = Categories()
records = Records()

for i in records.List:
	lb.insert('end',i)


      

cur_mon_var = tkinter.StringVar()
cur_mon_var.set(f'Now you have {records.current_money} dollars')
cur_mon_lab = tkinter.Label(root, textvariable=cur_mon_var)
cur_mon_lab.grid(row= 6 ,column=0)        
            
  


    
    
tkinter.mainloop()

