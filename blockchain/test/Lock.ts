import { expect } from "chai";
import { ethers } from "hardhat";
import { time } from "@nomicfoundation/hardhat-network-helpers";

describe("Lock", function () {
  it("Should set the right unlockTime", async function () {
    const ONE_YEAR_IN_SECS = 365 * 24 * 60 * 60;
    const ONE_GWEI = 1_000_000_000n;

    const lockedAmount = ONE_GWEI;
    const latestTime = await time.latest();
    const unlockTime = latestTime + ONE_YEAR_IN_SECS;

    const Lock = await ethers.getContractFactory("Lock");
    const lock = await Lock.deploy(unlockTime, { value: lockedAmount });

    await lock.waitForDeployment();

    expect(await lock.unlockTime()).to.equal(unlockTime);
  });
});
