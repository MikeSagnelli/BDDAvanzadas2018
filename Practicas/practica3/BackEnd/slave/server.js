var express = require('express');
var bodyparser = require('body-parser');

var app = express();

app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended: true}));

let memory = {};

app.post('/getCluster', function(request, result){
    let {file, clusterIndex} = request.body;
    console.log(`Cluster ${clusterIndex} from file ${file}`);
    console.log(memory[file][clusterIndex]);
    result.json(memory[file][clusterIndex]);
});

app.post('/file', function(request, result){
    let {file, clusterIndex, data} = request.body;
    if(!memory[file]){
        memory[file] = {};
    }

    memory[file][clusterIndex] = data;
    console.log(`Cluster number ${clusterIndex} of file ${file}: ${data} received...`)
    console.log('Current memory:', memory)
    result.send('OK');
});

app.get('/', function(req, res) {
    res.send("Distributed File System Slave Node");
  });

app.listen(4001, function(){
    console.log('Slave on port 4001');
});