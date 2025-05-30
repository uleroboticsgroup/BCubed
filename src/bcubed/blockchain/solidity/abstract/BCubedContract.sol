// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract BCubedContract {

    address private immutable OWNER_ADDRESS;

        struct MetaDataRecord {
        uint256     recT;
        string      sysN;
        string      sysV;
        string      sysS;
        string      sysM;
        string      resP;
        string      bbnV;
        string      netN;
        string      osyT;
        string      sysP;
    }

    struct SystemDataRecord {
        uint256 recT;
        uint256 sysT;
        string  namF;
        bytes   valF;

        int16   idTwo;
        bytes   valueTwo;

        int16   idFou;
        bytes   valueFou1;
        bytes   valueFou2;
        bytes   valueFou3;
    }

    struct OverviewDataRecord {
        uint256     recT;
        uint256     bbtR;
        uint256     iniT;
        uint256     finT;
    }

    MetaDataRecord private metaDataRecord;
    OverviewDataRecord private overviewDataRecord;
    mapping(uint256 => SystemDataRecord[]) private systemDataRecords;

    uint256 nStoredRecords = 0;
    
    uint256 initialTimestamp = 2051226000; // 1/1/2035 - 01:00:00
    uint256 finalTimestamp = 0;


    // Set the transaction sender as the owner of the contract.
    constructor () {
        OWNER_ADDRESS = msg.sender;
    }

    // Modifier to check that the caller is the owner of the contract.
    modifier onlyOwner() {
        require(msg.sender == OWNER_ADDRESS, "Not owner");
        // Underscore is a special character only used inside a function modifier 
        // and it tells Solidity to execute the rest of the code.
        _;
    }

    modifier commonRequires(uint256 recT) {
        require(overviewDataRecord.recT == 0, 
            "OD record is already created. The Black Box cannot add more information. It is needed to create a new one.");

        require(recT != 0, "The recT field is required.");
        _;
    }

    function setMetaDataRecord(MetaDataRecord calldata newMetaDataRecord) public 
                onlyOwner() 
                commonRequires(newMetaDataRecord.recT) {

        require(metaDataRecord.recT == 0, "MD record is already created.");

        require(keccak256(abi.encodePacked(newMetaDataRecord.sysN)) != keccak256(abi.encodePacked("")), "The sysN field is required.");
        require(keccak256(abi.encodePacked(newMetaDataRecord.sysM)) != keccak256(abi.encodePacked("")), "The sysM field is required.");
        require(keccak256(abi.encodePacked(newMetaDataRecord.resP)) != keccak256(abi.encodePacked("")), "The resP field is required.");
        require(keccak256(abi.encodePacked(newMetaDataRecord.bbnV)) != keccak256(abi.encodePacked("")), "The bbnV field is required.");
        require(keccak256(abi.encodePacked(newMetaDataRecord.netN)) != keccak256(abi.encodePacked("")), "The netN field is required.");
        require(keccak256(abi.encodePacked(newMetaDataRecord.osyT)) != keccak256(abi.encodePacked("")), "The osyT field is required.");
        require(keccak256(abi.encodePacked(newMetaDataRecord.sysP)) != keccak256(abi.encodePacked("")), "The sysP field is required.");

        metaDataRecord = newMetaDataRecord;
        nStoredRecords += 1;
    }

    function getMetaDataRecord() public view returns (MetaDataRecord memory) {
        return metaDataRecord;
    }

    function addSystemDataRecord(SystemDataRecord memory newSystemDataRecord) private 
                commonRequires(newSystemDataRecord.recT) {

        require(metaDataRecord.recT != 0, "MD record does not exist. The Black Box cannot add information until it is initialized.");
        require(newSystemDataRecord.sysT != 0, "The sysT field is required.");

        require(bytes(newSystemDataRecord.namF).length != 0, "The namF field is required.");

        require(bytes(newSystemDataRecord.valF).length != 0 || newSystemDataRecord.idTwo != 0 || newSystemDataRecord.idFou != 0, 
            "The valF, twoV or fouV field is required if namF field is filled.");

        if (bytes(newSystemDataRecord.valF).length != 0) {
            require(newSystemDataRecord.idTwo == 0 && newSystemDataRecord.valueTwo.length == 0 && 
                newSystemDataRecord.idFou == 0 && newSystemDataRecord.valueFou1.length == 0 && newSystemDataRecord.valueFou2.length == 0 && newSystemDataRecord.valueFou3.length == 0, 
                "If valF is filled, then twoV and fouV fields cannot be filled.");
        } else if (newSystemDataRecord.idTwo != 0) {
            require(bytes(newSystemDataRecord.valF).length == 0 && 
                newSystemDataRecord.idFou == 0 && newSystemDataRecord.valueFou1.length == 0 && newSystemDataRecord.valueFou2.length == 0 && newSystemDataRecord.valueFou3.length == 0,
                "If twoV is filled, then valF and fouV fields cannot be filled.");
        } else if (newSystemDataRecord.idFou != 0) {
            require(bytes(newSystemDataRecord.valF).length == 0 && 
                newSystemDataRecord.idTwo == 0 && newSystemDataRecord.valueTwo.length == 0,
                "If fouV is filled, then valF and twoV fields cannot be filled.");
        }

        uint256 systemTimestamp = newSystemDataRecord.sysT/1000000000;
        systemDataRecords[systemTimestamp].push(newSystemDataRecord);

        nStoredRecords += 1;

        initialTimestamp = systemTimestamp < initialTimestamp ? systemTimestamp : initialTimestamp;
        finalTimestamp = finalTimestamp < systemTimestamp ? systemTimestamp : finalTimestamp;
    }

    function addSystemDataRecords(SystemDataRecord[] calldata newSystemDataRecords) public 
                onlyOwner() {

        for (uint256 i = 0; i < newSystemDataRecords.length; i++) {
            addSystemDataRecord(newSystemDataRecords[i]);
        }
    }

    function getSystemDataRecordsByTimestamp(uint256 _timestamp) public view returns (SystemDataRecord[] memory) {
        return systemDataRecords[_timestamp];
    }

    function setOverviewDataRecord(OverviewDataRecord calldata newOverviewDataRecord) public 
                onlyOwner() 
                commonRequires(newOverviewDataRecord.recT) {

        require(metaDataRecord.recT != 0, "MD record does not exist. The Black Box cannot add information until it is initialized.");

        nStoredRecords += 1;

        overviewDataRecord = newOverviewDataRecord;

        overviewDataRecord.bbtR = nStoredRecords;
        overviewDataRecord.iniT = initialTimestamp;
        overviewDataRecord.finT = finalTimestamp;
    }

    function getOverviewDataRecord() public view returns (OverviewDataRecord memory) {
        return overviewDataRecord;
    }

    function getStoredRecords() public view returns (uint256) {
        return nStoredRecords;
    }

    function getInitialTimestamp() public view returns (uint256) {
        return initialTimestamp;
    }

    function getFinalTimestamp() public view returns (uint256) {
        return finalTimestamp;
    }
}