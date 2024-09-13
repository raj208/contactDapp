// pragma solidity >=0.4.22 <0.9.0;

// contract contact {
//   address owner; //state var
//   string[] names;
//   string[] mobiles;
//   string[] emails;
//   string[] organization;
//   mapping(string=>bool) _contracts;
//   constructor() public{
//     owner=msg.sender; //global var, storing owner address
//   }
// modifier onlyOwner { //function modifier-only owner can save contacts/telegram uses blockchain
//   require(owner==msg.sender);
//   _;
// }

// //inserting the contact into dapp
// function insertContact(string memory name, string memory mobile, string memory email, string memory, string memory org)public onlyOwner{
//   require(!_contacts[mobile]); //if mobile is not in contact, like _contacts['8888']->False
//   names.push(name);
//   mobiles.push(mobile);
//   emails.push(email);
//   organizations.push(org);
//   contracts[mobile] = true;
// }

// //read contract from blockchain
// function viewContacts() public view returns (string[] memory, string[] memory, string[], string[] memory){
//   return(names, mobiles, emails, organizations);
// }



// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Contact {
    address public owner;
    string[] public names;
    string[] public mobiles;
    string[] public emails;
    string[] public organizations;
    mapping(string => bool) private _contacts;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(owner == msg.sender, "Not authorized");
        _;
    }

    function insertContact(
        string memory name,
        string memory mobile,
        string memory email,
        string memory org
    ) public onlyOwner {
        require(!_contacts[mobile], "Contact already exists");
        names.push(name);
        mobiles.push(mobile);
        emails.push(email);
        organizations.push(org);
        _contacts[mobile] = true;
    }

    function viewContacts() 
        public 
        view 
        returns (
            string[] memory,
            string[] memory,
            string[] memory,
            string[] memory
        ) 
    {
        return (names, mobiles, emails, organizations);
    }
}

