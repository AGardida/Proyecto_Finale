from tkinter import *
from web3 import Web3
import json
root= Tk()
root.geometry("620x500")
count=0
register=0
sel=0
driverList= ["Carlos", "Juan", "Andre", "Javier"]
driver=[
		["",0,0,0],
		["",0,0,0],
		["",0,0,0],
		["",0,0,0],
		]
driver_selected=0
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

def button1():
	def public_ride():
		global i
		global count
		global driver
		i= int(No_driver.get())
		driver[count][1]=E_period.get()
		driver[count][2]=E_positions.get()
		driver[count][3]=E_cost.get()

		if count==0:
			driver[0][0]=driverList[i]
			offer_1=Checkbutton(frame, text=driver[0][0],variable=var1,command=one_option)
			offer_1.grid(row=0,column=0,sticky="W")
			count+=1
		elif count==1:
			driver[1][0]=driverList[i]
			offer_2=Checkbutton(frame, text=driver[1][0],variable=var2,command=one_option)
			offer_2.grid(row=1,column=0,sticky="W")
			count+=1
		elif count==2:
			driver[2][0]=driverList[i]
			offer_3=Checkbutton(frame, text=driver[2][0],variable=var3,command=one_option)
			offer_3.grid(row=2,column=0,sticky="W")
			count+=1
		elif count==3:
			driver[3][0]=driverList[i]
			offer_4=Checkbutton(frame, text=driver[3][0],variable=var4,command=one_option)
			offer_4.grid(row=3,column=0,sticky="W")
			count=0


		top.destroy()

	top= Toplevel()
	L_period=Label(top,text="Define period ")
	L_period.grid(row=0,column=0)
	
	L_Positions=Label(top,text="How many positions are available? ")
	L_Positions.grid(row=4,column=0)
	
	L_cost=Label(top,text="Cost ")
	L_cost.grid(row=8,column=0)

	
	E_period=Entry(top)
	E_period.grid(row=0,column=1)
	E_positions=Entry(top)
	E_positions.grid(row=4,column=1)
	E_cost=Entry(top)
	E_cost.grid(row=8,column=1)

	#L_destination=Label(top,text="Destination")
	#L_destination.grid(row=10,column=0)

	#choices = ['Coyoacan', 'Santa Fe', 'Xochimilco']
	#L_destination = StringVar(root)
	#L_destination.set('No destination selected')

	#w = OptionMenu(root, L_destination, *choices)
	#w.pack(row=10,column=1);

	n_dr=Label(top,text="No driver ")
	n_dr.grid(row=12,column=0)
	No_driver=Entry(top)
	No_driver.grid(row=12,column=1)

	B_validate=Button(top,text="Public",command=public_ride)
	B_validate.grid(row=14,column=0)

def bids():
	def make_bid():
		global register

		if E_positionsR.get()>positions_1:
			print("Exceeded amount of passangers")
		else:
			label=Label(frame2,text=driver_selected)
			label.grid(row=register,column=0,sticky="W")
			resta=int(driver[sel][2])-int(E_positionsR.get())
			driver[sel][2]=str(resta)
				

			register+=1
			if register==4:
				register=0

		top.destroy()
	
	top= Toplevel()
	global driver_selected
	global sel
	period_1=0
	positions_1=0
	cost_1=0
	wallet_1=500
	


	if var1.get()==1:
		sel=0
		driver_selected=driver[0][0]
		period_1=driver[0][1]
		positions_1=driver[0][2]
		cost_1=driver[0][3]
		balance_1= int(wallet_1)-int(cost_1)
	if var2.get()==1:
		sel=1
		driver_selected=driver[1][0]
		period_1=driver[1][1]
		positions_1=driver[1][2]
		cost_1=driver[1][3]
		balance_1= int(wallet_1)-int(cost_1)
	if var3.get()==1:
		sel=2
		driver_selected=driver[2][0]
		period_1=driver[2][1]
		positions_1=driver[2][2]
		cost_1=driver[2][3]
		balance_1= int(wallet_1)-int(cost_1)
	if var4.get()==1:
		sel=3
		driver_selected=driver[3][0]
		period_1=driver[3][1]
		positions_1=driver[3][2]
		cost_1=driver[3][3]
		balance_1= int(wallet_1)-int(cost_1)
		

	L_period=Label(top,text="Period: ")
	L_period.grid(row=0,column=0,sticky="E")
	D_period=Label(top,text=period_1)
	D_period.grid(row=0,column=1,sticky="W")

	L_Positions=Label(top,text="Positions available: ")
	L_Positions.grid(row=1,column=0,sticky="E")
	D_positions=Label(top,text=positions_1)
	D_positions.grid(row=1,column=1,sticky="W")

	L_cost=Label(top,text="Cost: ")
	L_cost.grid(row=2,column=0,sticky="E")
	D_cost=Label(top,text=cost_1)
	D_cost.grid(row=2,column=1,sticky="W")

	L_wallet=Label(top,text="Wallet: ")
	L_wallet.grid(row=3,column=0,sticky="E")
	D_wallet=Label(top,text=wallet_1)
	D_wallet.grid(row=3,column=1,sticky="W")

	L_balance=Label(top,text="Balance: ")
	L_balance.grid(row=4,column=0,sticky="E")
	D_balance=Label(top,text=balance_1)
	D_balance.grid(row=4,column=1,sticky="W")

	L_positionsR=Label(top,text="Positions required: ")
	L_positionsR.grid(row=5,column=0,sticky="E")
	E_positionsR=Entry(top)
	E_positionsR.grid(row=5,column=1,sticky="W")

	B_validate=Button(top,text="Make bid",command=make_bid)
	B_validate.grid(row=6,column=0,sticky="E")




#To select another option, you have to unselect the checkbox thas has already been selected
def one_option():
	if var1.get()==1:
		var1.set(1)
		var2.set(0)
		var3.set(0)
		var4.set(0)
	if var2.get()==1:
		var2.set(1)
		var1.set(0)
		var3.set(0)
		var4.set(0)
	if var3.get()==1:
		var3.set(1)
		var1.set(0)
		var2.set(0)
		var4.set(0)
	if var4.get()==1:
		var4.set(1)
		var1.set(0)
		var2.set(0)
		var3.set(0)
	


send_bids=Button(root,text="Send Bids",padx=15,pady=10,command=bids)
#send_bids.pack(side=BOTTOM)
#send_bids.pack(anchor=SW)
send_bids.grid(row=1,column=0)

publicc=Button(root,text="Publish a ride",padx=15,pady=10,command=button1)
#publicc.pack(side=BOTTOM)
#publicc.pack(anchor=SE)
publicc.grid(row=1,column=1)

frame=LabelFrame(root,text="Rideshare Offers",padx=100,pady=160)
#frame.pack()
#frame.pack(side=RIGHT)
#frame.pack(anchor=NE)
frame.grid(row=0,column=0)


frame2=LabelFrame(root,text="My Future Travels",padx=100,pady=200)
#frame2.pack()
#frame.pack(side=LEFT)
#frame.pack(anchor=NW)
frame2.grid(row=0,column=1)


#label2=Label(frame,text="Rider_1")
#label2.grid(row=0,column=0)
#label2.pack()
frame.columnconfigure(0, weight=1)





root.mainloop()




