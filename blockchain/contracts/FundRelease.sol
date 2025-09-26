// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FundRelease {
    mapping(address => uint256) public allocations;
    mapping(address => bool) public completed;

    function allocateFunds(address recipient, uint256 amount) public {
        allocations[recipient] = amount;
    }

    function markProjectCompleted(address recipient) public {
        completed[recipient] = true;
    }

    function releaseFunds(address recipient) public view returns (uint256) {
        require(completed[recipient], "Project not complete");
        return allocations[recipient];
    }
}
