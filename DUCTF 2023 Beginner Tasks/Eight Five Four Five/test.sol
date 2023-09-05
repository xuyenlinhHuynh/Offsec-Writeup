pragma solidity ^0.8.19;

interface EightFiveFourFive {
    function readTheStringHere() external view returns (string memory);
    function solve_the_challenge(string memory answer) external;
}
contract call{
        address addr = 0xf22cB0Ca047e88AC996c17683Cee290518093574;
        constructor() public payable {
        EightFiveFourFive(addr).solve_the_challenge(EightFiveFourFive(addr).readTheStringHere());
        }
}
