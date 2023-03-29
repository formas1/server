const express = require("express");
const bodyParser = require("body-parser");
const app = express();

data = "{}";
app.use(bodyParser.json()); // add this middleware to parse JSON bodies

app.listen(3000, () => {
  console.log("Application started and Listening on port 3000");
});

app.get("/", (req, res) => {
  res.sendFile("/usr/test/index.html");
});

app.get("/data", (req, res) => {
  //res.sendFile("/usr/test/data.html");
  res.sendFile("/usr/test/data.html")
});

app.get("/raw/data", (req, res) => {
  //res.sendFile("/usr/test/data.html");
  res.send(data)
});

app.post("/api/data", (req, res) => {
  // assuming the incoming request body is in JSON format
  data = req.body;

  // do something with the data, e.g. store it in a database
  console.log(data);

  // send a response
  res.send("Data received successfully");
});