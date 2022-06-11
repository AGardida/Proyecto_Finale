 pragma solidity ^0.5.0;

contract Flotilla {

    address payable client;
    address payable driver;
    uint No_of_vehicles=0;
    uint No_passangers=0;
    uint cost=0;

    struct Vehicle{
        uint startTime;
        uint duration;
        uint vehicleId;
        string driverName;
        uint cost;
        uint sits;
        address payable driver;
        address payable client;
    }
    mapping(uint=>Vehicle) public Vehicle_by_No;
    struct driverss{
        address conductor;
        }
    mapping(address =>bool) public Micro;

    modifier driversList(){
        require(Micro[msg.sender]==true,"Only drivers can access");
        _;
    }
    modifier justClients(){
        require(Micro[msg.sender] != true, "Only clients can access");
        _;
    }

    modifier AgreementTimesLeft(uint _index) {
        uint time = Vehicle_by_No[_index].startTime + Vehicle_by_No[_index].duration;
        require(now < time, "Agreement already Ended");
        _;
    }


    function getDriversList() public{
        Micro[0xbcCB9F299c7f61e67f52799742d06555F68B6bCB]=true;   //account 0
        Micro[0x2325Df5634Cc650B88792Ef6B3a71b2f18E57Ca0]=true;   //account 1
        Micro[0x982ea450c84E5dC50489eb4AA3f317bCf4b30f1d]=true;   //account 2
        Micro[0x7768c40B5dF6B5F69e4E32db875a49a35f5f0dD8]=true;   //account 3
    }

    function publicDrive(string memory _driver,uint _cost,uint _sits,uint _Id,uint _start,uint _duration) driversList() public {
            Vehicle_by_No[No_of_vehicles]=Vehicle(_start,_duration,No_of_vehicles,_driver,_cost,_sits,address(_Id),msg.sender);
            No_of_vehicles++;
            }
    function getNoDrivers() public view returns(uint){
        return uint(No_of_vehicles);
    }
    function getDataDriver(uint i) public view returns (uint, string memory, uint, uint,uint,uint){
        return (Vehicle_by_No[i].vehicleId,Vehicle_by_No[i].driverName,Vehicle_by_No[i].cost,Vehicle_by_No[i].sits,Vehicle_by_No[i].startTime,Vehicle_by_No[i].duration);
    }

    function ckeckBid(uint _id) justClients() public payable returns (bool){
        require(msg.value >= uint(Vehicle_by_No[_id].cost), "Not enough Ether in your wallet");
        return true;
    }

    function agreementTerminated(uint _index) public AgreementTimesLeft(_index){
        Vehicle_by_No[_index].sits = 0;
    }
}