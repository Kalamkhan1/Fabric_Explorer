const express = require("express");
const errorHandler = require("./middleware/errorHandler.js");
const connectdb = require("./config/dbconnection");
const dotenv = require("dotenv").config();
connectdb();
const app = express();
const port = process.env.PORT;
app.use(express.json());

app.use("/api/fabrics",require("./routes/fabricRoutes.js"));
app.use(errorHandler);
app.listen(port,() => {  
    console.log(port);
});

