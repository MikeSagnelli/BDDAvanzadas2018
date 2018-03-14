const express = require('express');
const rp = require('request-promise');
const multer  = require('multer');
const fs = require('fs');
const bodyParser = require('body-parser');
const master = require('./master')

const upload = multer({ dest: 'uploads/' })
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/file', upload.single('file'), function (request, result, next) {
  const path = request.file.path;
  const originalname = request.file.originalname;
  let fileContent = fs.readFileSync(path)
  master.distributeFile(originalname, fileContent).catch(console.error)
  fs.unlinkSync(path);
  result.send("OK");
})

app.get('/file/:fileName', async function (request, result) {
  let path = __dirname + "/uploads/" + request.params.fileName;
  let ok = await master.getFile(request.params.fileName);
  result.sendFile(path);
  fs.unlinkSync(path);
});

app.get('/', function(request, result) {
  result.send("Distributed File System Master Node");
});

app.listen(4000, function () {
  console.log('Master on port 4000');
});
