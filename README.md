# Proyecto_Finale
Cryptology

Most carpooling systems and radio cab facilities come with a middleman, the agency itself. So, what if an agency like Uber decides to shut down business in the city? There are a lot of issues related to this architecture, such as the cost and delay imposed on the main in the middle agent.

In our community, we have many students who need to move to different places to go to Campus every day. Given this scenario, things in e ridesharing and car hire are transferred to the blockchain, without an intermediary, where both riders and drivers can get connected directly.



The core idea is to create a system where the ridesharing times will be published using a smart contract, to bring trust and transparency. Then, the passengers will place bids within the smart contract-defined interval.

The desired workflow is:

A driver publishes a slot time where he is available to rideshare. In the rideshare publication, the driver needs to define: the period, how many positions are open, and the cost.
The passengers send their bids.
System checks if everything is ok (using smart contracts)
The passengers receive confirmation that their bids are accepted (or not).
While building this project, you need to make sure of some things to make your system work.

Details of the users should be hidden in your application due to privacy issues. To accomplish this requirement, you need to use an Ethereum address, which will be the only identifier for the users.
One person should be able to place only one bid, and that too only when eligible.
It should be transparent that all the bids’ rules are being followed. Then, of course, we need the bids to be accurately recorded and counted. There should not be any mistake or possibility of fraud in the system.


The system is made up of three main blocks the GUI, the smart contracts and the interface between the transactions over the blockchain suing ganache. This three blocks will be described below.

-- GUI
The graphicall user interface is made using python, it consistis of a main page where user can login and register a new account. 
To register a new a ccount, the user will new an addres, this will be obtained from the ganache blockchain. Once the new user has been registered the user has the possibility to login going back to the main page. The data of the new users is sored into files in disk.

After the login the user will be asked to log out or to create a smart contract. If the user choose to log out, the session will be closed and the addres from the user will be deleted. on the other hand, if th e user chooses to create a smartcontract a new window will pop-up displaying the dirvers info and the posibility to create a new transaction. By this moment the GUI has been connected with the ganache blockchain and the soldity interface.

-- Smart contracts
The smartcontracts are creted using solidity.
A contract called Flotilla is created inside we initialize some variables as addresses, number of vehicles, passengers and cost.
Then we define the strucutre of the vehicle

<img width="280" alt="Captura de Pantalla 2022-06-14 a la(s) 2 07 40 p m" src="https://user-images.githubusercontent.com/107238191/173669379-1d0c8009-6548-43e9-ae82-fb593adc76b8.png">

Later we create a function to make a public drive

<img width="936" alt="Captura de Pantalla 2022-06-14 a la(s) 2 08 53 p m" src="https://user-images.githubusercontent.com/107238191/173669569-6d56837e-546a-496d-bb14-21cf94fe33f7.png">

If there isnt enough funds a message will be displayed and drive is not going to be succesfull
<img width="819" alt="Captura de Pantalla 2022-06-14 a la(s) 2 09 21 p m" src="https://user-images.githubusercontent.com/107238191/173669653-27179413-b0fc-43de-919c-bff5e1c2a582.png">


-- Connection between gaanche, solidity and the GUI
To create a connection with ganache blockchain it is necessary to have the web3 library, in ganache we set a new project and get the ganache url then in the python code we stablish the connection (web3=Web3(Web3.HTTPProvider(ganache_url))), to verify if the connection is succesful we print a status message.

In order to link the blockchain whit the solidity smart contract it is necessary to add a json command that contain some of the following parameters.
  constant
  inputs
  name
  outputs
  payable
  etc
  
Later we stablish a connection with the solidity interface by using the following commands:
  address=web3.toChecksumAddress()
  
  contract=web3.eth.contract(
	  address=address,
	  abi=abi
  )

In the smart contract window, we implement a function to publish a contract that has the following structure:
publish=contract.functions.publicDrive(E_Name.get(),int(E_cost.get()),int(E_positions.get()),int(E_id.get()),int(E_time.get()),int(E_duration.get())).transact()

<img width="1001" alt="Captura de Pantalla 2022-06-14 a la(s) 1 50 45 p m" src="https://user-images.githubusercontent.com/107238191/173666621-146ccdc9-aeb5-4f13-bb09-3b4e5e0aa87d.png">

This function creates the contract with name, cost, position, and duration as arguments. Once th esmart contract has expired, the coontract is destoyed and the GUI is refreshed to show the latest drivers info.

To display this info in the ganache blockchain it is necesary the following code.

<img width="421" alt="Captura de Pantalla 2022-06-14 a la(s) 1 56 21 p m" src="https://user-images.githubusercontent.com/107238191/173667544-88a6642c-bddd-4b21-98db-80f902293166.png">

This function links the transaction into the blockchain structure and refresh the ganache interface for each transaction that has been made. Also int this part of the code, it is analyzed if the driver has enough funds to carry out the transaction.

<img width="772" alt="Captura de Pantalla 2022-06-14 a la(s) 2 00 25 p m" src="https://user-images.githubusercontent.com/107238191/173668166-28750555-b3b0-4eb1-8553-a9adc9146594.png">





