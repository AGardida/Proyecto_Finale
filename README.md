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
