const requestPromise = require('request-promise');
const fs = require('fs');

const clusterSize = 10;

const replicaNumber = 2;

let files = {};

let slaves = [
    {index: 0, address:"http://localhost:4001", clusterCount: 0},
    {index: 1, address:"http://localhost:4002", clusterCount: 0},
    {index: 2, address:"http://localhost:4003", clusterCount: 0}
];

function getBestSlaveIndex(){
    let temp = 0;
    for(let i = 1; i < slaves.length; i++){
        if(slaves[i].clusterCount < slaves[temp].clusterCount){
            temp = i;
        }
    }
    return temp;
}

async function distributeFile(fileName, buffer){
    console.log(`Master: file ${fileName} is being distributed`);
    files[fileName] = []
    let size = buffer.length;
    let index = 0;
    let i = 0;
    
    while(size > clusterSize){
        let clusterPiece = buffer.slice(index, index + clusterSize);
        await distributeCluster(fileName, clusterPiece, i);
        index += clusterSize;
        i++;
        size -= clusterSize;
    }

    let clusterPiece = buffer.slice(index, -1);
    await distributeCluster(fileName, clusterPiece, i);

    console.log(files);
}

async function distributeCluster(fileName, clusterSlice, clusterIndex){
    console.log(`Master: Distributing ${clusterSlice} of ${fileName}`);
    let clusterLocations = [];

    for(let i = 0; i < replicaNumber; i++){
        slaveIndex = getBestSlaveIndex();
        if(await sendClusterToSlave(fileName, clusterSlice, clusterIndex, slaveIndex)){
            slaves[slaveIndex].clusterCount++;
            clusterLocations.push(slaveIndex);
        }
    }

    files[fileName].push(clusterLocations);
}

async function sendClusterToSlave(fileName, clusterSlice, clusterIndex, slaveIndex){
    console.log(`Slave: ${slaveIndex} ${slaves[slaveIndex]}`);
    console.log(`Sending cluster: ${clusterSlice} to slave number ${slaveIndex}`);
    let payload = {
        file: fileName,
        clusterIndex: clusterIndex,
        data: clusterSlice
    };

    console.log(`Sending: ${payload}`);
    const requestOptions = {
        method: 'POST',
        url: slaves[slaveIndex].address + "/file",
        body: payload,
        json: true
    };

    let slaveResponse;
    try{
        slaveResponse = await requestPromise(requestOptions);
    } catch (error){
        console.error(`Error sending to slave: ${error.message}`);
        return null;
    }

    return slaveResponse;
}

async function getFile(fileName){
    for(let i = 0; i < files[fileName].length; i++){
        let cluster = await getCluster(fileName, i);
        if(!cluster) {
            console.error(`Could not retrieve cluster number ${i} from ${fileName}`);
            return null;
        }
        fs.appendFileSync(__dirname + "/uploads/" + fileName, Buffer.from(cluster.data).toString("utf8"));
    }

    return true;
}

async function getCluster(fileName, index){
    let locations = files[fileName][index];
    let cluster;
    for(let i = 0; i < locations.length; i++){
        cluster = await getClusterFromSlave(locations[i], fileName, index);
        if(cluster){
            return cluster;
        }
        else{
            return null;
        }
    }
}

async function getClusterFromSlave(slaveIndex, fileName, index){
    const requestOptions = {
        method: 'POST',
        url: `${slaves[slaveIndex].address}/getCluster`,
        body: {file: fileName, clusterIndex: index},
        json: true
    };

    let slaveResponse;
    try{
        slaveResponse = requestPromise(requestOptions);
    } catch (error) {
        console.error(`Error getting cluster ${index} of ${fileName} from slave ${slaveIndex}`);
        console.error(error.error);
        return null;
    }
    return slaveResponse;
}

module.exports = {distributeFile, getFile};