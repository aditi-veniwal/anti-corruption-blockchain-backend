const hre = require("hardhat");

async function main() {
  const FundRelease = await hre.ethers.getContractFactory("FundRelease"); // matches your contract name
  const fundRelease = await FundRelease.deploy(); // add args here if constructor has any

  await fundRelease.waitForDeployment();

  console.log(`✅ FundRelease deployed to: ${await fundRelease.getAddress()}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
