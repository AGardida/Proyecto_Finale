
#from curses.panel import top_panel
import numpy as np
import tkinter as tk
import pandas as pd
import os
from web3 import Web3
import json

ganache_url="http://127.0.0.1:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

account=["0xbcCB9F299c7f61e67f52799742d06555F68B6bCB","0x2325Df5634Cc650B88792Ef6B3a71b2f18E57Ca0","0x982ea450c84E5dC50489eb4AA3f317bCf4b30f1d","0x7768c40B5dF6B5F69e4E32db875a49a35f5f0dD8"]
print(account[1])
private_key1="48234d1e10180d6fb140cebf43138058e924a6aab679c4f6f1d96e3cf45907a7"
private_key2="e2d51e78916454c61b814bc22c70ea031c49100896d42ae09af26ff198fbe95d"
abi= json.loads('[{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"Micro","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"Vehicle_by_No","outputs":[{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"uint256","name":"vehicleId","type":"uint256"},{"internalType":"string","name":"driverName","type":"string"},{"internalType":"uint256","name":"cost","type":"uint256"},{"internalType":"uint256","name":"sits","type":"uint256"},{"internalType":"address payable","name":"driver","type":"address"},{"internalType":"address payable","name":"client","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"ckeckBid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"i","type":"uint256"}],"name":"getDataDriver","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"getDriversList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getNoDrivers","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_driver","type":"string"},{"internalType":"uint256","name":"_cost","type":"uint256"},{"internalType":"uint256","name":"_sits","type":"uint256"},{"internalType":"uint256","name":"_Id","type":"uint256"},{"internalType":"uint256","name":"_start","type":"uint256"},{"internalType":"uint256","name":"_duration","type":"uint256"}],"name":"publicDrive","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
bytecode='60806040526004361061004a5760003560e01c806306fdde031461004f57806365e0c006146100df578063964de5b21461010a578063bcc2b2f8146101dc578063f40e03c21461020a575b600080fd5b34801561005b57600080fd5b5061006461030a565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100a4578082015181840152602081019050610089565b50505050905090810190601f1680156100d15780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156100eb57600080fd5b506100f46103a8565b6040518082815260200191505060405180910390f35b34801561011657600080fd5b506101da6004803603604081101561012d57600080fd5b810190808035906020019064010000000081111561014a57600080fd5b82018360208201111561015c57600080fd5b8035906020019184600183028401116401000000008311171561017e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001909291905050506103ae565b005b610208600480360360208110156101f257600080fd5b81019080803590602001909291905050506105c0565b005b34801561021657600080fd5b506102436004803603602081101561022d57600080fd5b8101908080359060200190929190505050610973565b60405180868152602001806020018581526020018473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200183151515158152602001828103825286818151815260200191508051906020019080838360005b838110156102cb5780820151818401526020810190506102b0565b50505050905090810190601f1680156102f85780820380516001836020036101000a031916815260200191505b50965050505050505060405180910390f35b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103a05780601f10610375576101008083540402835291602001916103a0565b820191906000526020600020905b81548152906001019060200180831161038357829003601f168201915b505050505081565b60015481565b60008251116103bc57600080fd5b600081116103c957600080fd5b6001600081548092919060010191905055506040518060a0016040528060015481526020018381526020018281526020013373ffffffffffffffffffffffffffffffffffffffff16815260200160001515815250600260006001548152602001908152602001600020600082015181600001556020820151816001019080519060200190610458929190610a6e565b506040820151816002015560608201518160030160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060808201518160030160146101000a81548160ff0219169083151502179055509050507f24bcf511e8f50e673b8455c9fb8ebd0be7f6a47b7ec63917b271fa1c9dbd9bad600154838333600060405180868152602001806020018581526020018473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200183151515158152602001828103825286818151815260200191508051906020019080838360005b8381101561057e578082015181840152602081019050610563565b50505050905090810190601f1680156105ab5780820380516001836020036101000a031916815260200191505b50965050505050505060405180910390a15050565b6105c8610aee565b600260008381526020019081526020016000206040518060a001604052908160008201548152602001600182018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156106895780601f1061065e57610100808354040283529160200191610689565b820191906000526020600020905b81548152906001019060200180831161066c57829003601f168201915b50505050508152602001600282015481526020016003820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020016003820160149054906101000a900460ff1615151515815250509050600081606001519050816040015134101561072957600080fd5b81608001511561073857600080fd5b33826060019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff1681525050600182608001901515908115158152505081600260008581526020019081526020016000206000820151816000015560208201518160010190805190602001906107bb929190610a6e565b506040820151816002015560608201518160030160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060808201518160030160146101000a81548160ff0219169083151502179055509050508073ffffffffffffffffffffffffffffffffffffffff166108fc349081150290604051600060405180830381858888f19350505050158015610876573d6000803e3d6000fd5b507f328f818e79da4f486e43e65bde3bc51c97a9d9ccf7881e7721241401ff34da2d6001548360200151846040015133600060405180868152602001806020018581526020018473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200183151515158152602001828103825286818151815260200191508051906020019080838360005b83811015610930578082015181840152602081019050610915565b50505050905090810190601f16801561095d5780820380516001836020036101000a031916815260200191505b50965050505050505060405180910390a1505050565b6002602052806000526040600020600091509050806000015490806001018054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610a255780601f106109fa57610100808354040283529160200191610a25565b820191906000526020600020905b815481529060010190602001808311610a0857829003601f168201915b5050505050908060020154908060030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060030160149054906101000a900460ff16905085565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610aaf57805160ff1916838001178555610add565b82800160010185558215610add579182015b82811115610adc578251825591602001919060010190610ac1565b5b509050610aea9190610b35565b5090565b6040518060a00160405280600081526020016060815260200160008152602001600073ffffffffffffffffffffffffffffffffffffffff1681526020016000151581525090565b610b5791905b80821115610b53576000816000905550600101610b3b565b5090565b9056fea265627a7a723158207be18f32aaa5af893e878de7cd60b9b45d7d680dc4b0de13f6fad1471475440f64736f6c63430005110032'
address=web3.toChecksumAddress("0xC1FDcC197FcB567717A25116620E8Ce987AC9323")
Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)
contract=web3.eth.contract(
	address=address,
	abi=abi
)

def main_screen_window():
    
    global main_screen
    main_screen = tk.Tk()
    main_screen.geometry("500x500")
    main_screen.title("Login Screen")
    main_screen.config(bg = "#1f243a")
    
    tk.Label(text = "WELCOME",fg="white",bg = "#36616d",width = "200",height = "5", font = ("calibir",20)).pack()
    tk.Button(text = "Login",bg = "#252c44",width = "10",height = "3",command = login).pack()
    tk.Button(text = "Register",bg = "#252c44",fg = "black",width = "10",height = "3",command = register).pack()


    main_screen.mainloop()
 
def register():
 
    global register_screen
    register_screen = tk.Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("500x500")
    register_screen.config(bg = "#1f243a")
 

    global username
    global password
    global username_entry
    global password_entry

    username = tk.StringVar()
    password = tk.StringVar()
 

    tk.Label(register_screen, text="Create account", bg="#1f243a",fg = "white").pack()
    tk.Label(register_screen, text="",bg="#1f243a",fg = "white").pack()
    

    username_lable = tk.Label(register_screen, text="Username * ",bg="#1f243a",fg = "white")
    username_lable.pack()
 
    username_entry = tk.Entry(register_screen, textvariable=username,bg = "#363f69",fg = "white")
    username_entry.pack()
   
    password_lable = tk.Label(register_screen, text="Password * ",bg="#1f243a",fg = "white")
    password_lable.pack()
    
    password_entry = tk.Entry(register_screen, textvariable=password, show='*',bg = "#363f69",fg = "white")
    password_entry.pack()
    
    tk.Label(register_screen, text="",bg="#1f243a",fg = "white").pack()
    
    tk.Button(register_screen, text="Register", width=10, height=2, bg="blue",command = register_user).pack()
 

def register_user():
 

    username_info = username.get()
    password_info = password.get()
 

    file = open("C:/Users/andre/OneDrive/Documentos/cryptho/Users/"+username_info, "w")
 

    file.write(username_info + "\n")
    file.write(password_info+ "\n")
    file.close()
 
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
 
    # set a label for showing success information on screen 
    
    tk.Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

#--------------------------
def login():
    global login_screen
    login_screen = tk.Toplevel(main_screen)
    login_screen.title("Login Screen")
    login_screen.geometry("500x500")
    login_screen.config(bg = "#1f243a")
    tk.Label(login_screen, text="Enter username and password",fg = "white",bg = "#1f243a").pack()

    global username_check
    global password_check
    global username_login_entry
    global password_login_entry

    username_check = tk.StringVar()
    password_check = tk.StringVar()

    tk.Label(login_screen, text="Username * ",fg = "white",bg = "#1f243a").pack()
    username_login_entry = tk.Entry(login_screen, textvariable=username_check,bg = "#363f69",fg = "white")
    username_login_entry.pack()
    tk.Label(login_screen, text="",fg = "white",bg = "#1f243a").pack()
    tk.Label(login_screen, text="Password * ",fg = "white",bg = "#1f243a").pack()
    password_login_entry = tk.Entry(login_screen, textvariable=password_check, show= '*',bg = "#363f69",fg = "white")
    password_login_entry.pack()
    tk.Label(login_screen, text="",fg = "white",bg = "#1f243a").pack()
    tk.Button(login_screen, text="Login", width=10, height=2, command=login_verify).pack()



def login_verify():

    global username1
    global password1
    username1 = username_check.get()
    password1 = password_check.get()

    username_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)
 
    #-------------------------Cambiar path--------------------
    list_of_files = os.listdir("C:/Users/andre/OneDrive/Documentos/cryptho/Users/")
    print(list_of_files)  
 

    if username1 in list_of_files:
        file1 = open("C:/Users/andre/OneDrive/Documentos/cryptho/Users/"+username1, "r")   
        verify = file1.read().splitlines() 
        if password1 in verify:  
            web3.eth.default_account = username1                      #-----------------------probando
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_verification():
    print("Loading...")

    
def login_sucess():
 
    global login_success_screen  
    login_success_screen = tk.Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    login_success_screen.config(bg = "#1f243a")
    tk.Label(login_success_screen, text="Login Success",bg = "#1f243a",fg = "white").pack()
 
    tk.Button(login_success_screen, text="Smart Contract",width=10, height=2,command=smart_contract_window_1).pack()
    tk.Label(login_screen, text="",fg = "white",bg = "#1f243a").pack()
    tk.Button(login_success_screen, text="Log Out",width=10, height=2, command=log_out).pack()
    
 

def log_out():
    login_success_screen.destroy()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = tk.Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.config(bg = "#1f243a")
    tk.Label(password_not_recog_screen, text="Invalid Password ").pack()
    tk.Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()   

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = tk.Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    user_not_found_screen.config(bg = "#1f243a")
    tk.Label(user_not_found_screen, text="User Not Found").pack()
    tk.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

#---------------------------------------------SMART CONTRACT---------------

def smart_contract_window_2():
    def public_ride():
        publish=contract.functions.publicDrive(E_Name.get(),int(E_cost.get()),int(E_positions.get()),int(E_id.get()),int(E_time.get()),int(E_duration.get())).transact()
        tx_receipt=web3.eth.wait_for_transaction_receipt(publish)
        smart_contract_screen_2.destroy()
        No_drivers=contract.functions.getNoDrivers().call()
        i=0
        for i in range(No_drivers):
            Data_driver=contract.functions.getDataDriver(i).call()
            drivers_av=tk.Button(frame,text=Data_driver[1])
            drivers_av.grid(row=4*i,column=0)
        
    
    global smart_contract_screen_2
    smart_contract_screen_2= tk.Toplevel(smart_contract_screen_1)
    smart_contract_screen_2.config(bg = "#1f243a")

    L_time=tk.Label(smart_contract_screen_2,text="Start time: ",fg = "white",bg = "#1f243a")
    L_time.grid(row=0,column=0)

    L_duration= tk.Label(smart_contract_screen_2,text="Duration: ",fg = "white",bg = "#1f243a")
    L_duration.grid(row=4,column=0)

    L_Positions=tk.Label(smart_contract_screen_2,text="How many positions are available? ",fg = "white",bg = "#1f243a")
    L_Positions.grid(row=8,column=0)
    
    L_cost=tk.Label(smart_contract_screen_2,text="Cost ",fg = "white",bg = "#1f243a")
    L_cost.grid(row=12,column=0)
    
    L_Name=tk.Label(smart_contract_screen_2,text="Name: ",fg = "white",bg = "#1f243a")
    L_Name.grid(row=16,column=0)
    
    E_time=tk.Entry(smart_contract_screen_2,bg = "#363f69",fg = "white")    #E_period
    E_time.grid(row=0,column=1)
    E_duration=tk.Entry(smart_contract_screen_2,bg = "#363f69",fg = "white")  
    E_duration.grid(row=4,column=1)
    E_positions=tk.Entry(smart_contract_screen_2,bg = "#363f69",fg = "white")
    E_positions.grid(row=8,column=1)
    E_cost=tk.Entry(smart_contract_screen_2,bg = "#363f69",fg = "white")
    E_cost.grid(row=12,column=1)
    E_Name=tk.Entry(smart_contract_screen_2,bg = "#363f69",fg = "white")
    E_Name.grid(row=16,column=1)
    E_id=tk.Entry(smart_contract_screen_2,bg = "#363f69",fg = "white")
    E_id.grid(row=20,column=1)
    B_validate=tk.Button(smart_contract_screen_2,text="Public",command=public_ride)
    B_validate.grid(row=24,column=0)

def selection(ID):
    def pay (amount,_to,_from,key):
        nonce=web3.eth.getTransactionCount(_from)
        tx= {
            'nonce':nonce,
            'to':account[_to],
            'value':web3.toWei(amount,'ether'),
            'gas':3000000,
            'gasPrice':web3.toWei('50','gwei')
        }
        file = open("C:/Users/andre/OneDrive/Documentos/cryptho/Users/"+username1, "r")
        list_of_lines = file.readlines()
        file.close()
        #print(len(list_of_lines))
        lenn=len(list_of_lines)
        for i in range(2,lenn):
            iterr=contract.functions.getDataDriver(int(list_of_lines[i])).call()
            summ=int(iterr[4])+int(iterr[5])
            print(summ)
            summ2=int(Data_driver[4])+int(Data_driver[5])
            print(summ2)
            if ((summ>=int(Data_driver[4])) and (int(iterr[4])<=summ2)):
                print("No va")
            else:
                print("si va")
                signed_tx=web3.eth.account.signTransaction(tx,key)
                tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                web3.eth.wait_for_transaction_receipt(tx_hash)
                file = open("C:/Users/andre/OneDrive/Documentos/cryptho/Users/"+username1, "a") 
                file.write(str(Data_driver[0]) + "\n")
                file.close()
        
        file = open("C:/Users/andre/OneDrive/Documentos/cryptho/Users/"+username1, "r")
        list_of_lines = file.readlines()
        file.close()
        for i in range(2,len(list_of_lines)):
            rara=contract.functions.getDataDriver(int(list_of_lines[i])).call()
            labell=tk.Label(frame2,text="Travel with:"+str(rara[1])+" at "+ str(rara[4]))
            labell.pack()

        smart_contract_screen_4.destroy()

    print (ID)
    global smart_contract_screen_4
    smart_contract_screen_4=tk.Toplevel(smart_contract_screen_1)
    smart_contract_screen_4.config(bg="#1f243a")
    Data_driver=contract.functions.getDataDriver(ID).call()
    namee=tk.Label(smart_contract_screen_4,text="NAME: ",fg = "white",bg = "#1f243a")
    namee.grid(row=0,column=0)
    price=tk.Label(smart_contract_screen_4,text="PRICE: ",fg = "white",bg = "#1f243a")
    price.grid(row=4,column=0)
    sits=tk.Label(smart_contract_screen_4,text="SITS: ",fg = "white",bg = "#1f243a")
    sits.grid(row=8,column=0)
    L_driver=tk.Label(smart_contract_screen_4,text=Data_driver[1],fg = "white",bg = "#1f243a")
    L_driver.grid(row=0,column=1)
    L_cost=tk.Label(smart_contract_screen_4,text=Data_driver[2],fg = "white",bg = "#1f243a")
    L_cost.grid(row=4,column=1)
    L_sits=tk.Label(smart_contract_screen_4,text=Data_driver[3],fg = "white",bg = "#1f243a")
    L_sits.grid(row=8,column=1)
    button_make=tk.Button(smart_contract_screen_4,text="PAY",command=lambda:pay(int(Data_driver[2]),ID,username1,password1))  #  def pay (amount,_to,_from,key):
    button_make.grid(row=12,column=0)
#-------------------------------------------SMART CONTRACT
def make_bid():
    smart_contract_screen_3.destroy()

def smart_contract_window_3():
    global smart_contract_screen_3
    smart_contract_screen_3=tk.Toplevel(smart_contract_screen_1)
    smart_contract_screen_3.config(bg="#1f243a")
    B_validate=tk.Button(smart_contract_screen_2,text="Public",command=make_bid)
    B_validate.grid(row=12,column=0)

def smart_contract_window_1():
    global smart_contract_screen_1
    global Data_driver
    global frame
    global frame2
    smart_contract_screen_1= tk.Toplevel(login_success_screen)
    smart_contract_screen_1.config(bg = "#1f243a")
    frame=tk.LabelFrame(smart_contract_screen_1,text="Rideshare Offers",padx=100,pady=200)
    frame.pack()
    frame.pack(side=tk.RIGHT)
    frame.pack(anchor=tk.NE)

    frame2=tk.LabelFrame(smart_contract_screen_1,text="My Future Travels",padx=100,pady=200)
    frame2.pack()
    frame.pack(side=tk.LEFT)
    frame.pack(anchor=tk.NW)
    label=tk.Label(frame2,text="future")
    label.pack()
    No_drivers=contract.functions.getNoDrivers().call()
    #web3.eth.wait_for_transaction_receipt(No_drivers)
    print('Updated greeting: {}'.format(contract.functions.getNoDrivers().call()))
    print(No_drivers)
    if No_drivers==0:
        print("No hay conductores")
    else:
        i=0
        for i in range(No_drivers):
            Data_driver=contract.functions.getDataDriver(i).call()
            print('Updated greeting: {}'.format(contract.functions.getDataDriver(i).call()))
            if i==0:
                driver_0=tk.Button(frame,text=Data_driver[1],command=lambda:selection(0))
                driver_0.grid(row=4*i,column=0)
            elif i==1:
                driver_1=tk.Button(frame,text=Data_driver[1],command=lambda:selection(1))
                driver_1.grid(row=4*i,column=0)
            elif i==2:
                driver_2=tk.Button(frame,text=Data_driver[1],command=lambda:selection(2))
                driver_2.grid(row=4*i,column=0)
            elif i==3:
                driver_3=tk.Button(frame,text=Data_driver[1],command=lambda:selection(3))
                driver_3.grid(row=4*i,column=0)
            elif i==4:
                driver_4=tk.Button(frame,text=Data_driver[1],command=lambda:selection(4))
                driver_4.grid(row=4*i,column=0)
            elif i==5:
                driver_5=tk.Button(frame,text=Data_driver[1],command=lambda:selection(5))
                driver_5.grid(row=4*i,column=0)

    label2=tk.Label(frame,text="Rider_1")
    #label2.grid(row=1,column=0)
    #label2.pack()

    publicc=tk.Button(smart_contract_screen_1,text="Public a ride",padx=15,pady=10,command=smart_contract_window_2)
    publicc.pack()
    bid=tk.Button(smart_contract_screen_1,text="Make a bid",padx=15,pady=30,command=smart_contract_window_3)
    bid.pack()

    
def smart_contracts():
    return 0



main_screen_window()


