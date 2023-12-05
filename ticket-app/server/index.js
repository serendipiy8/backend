// import express from "express"
// const app = express()
// import cors from "cors"
// import { urlencoded } from "body-parser"
// import { router } from "./router.js"
const express = require("express");
const app = express();
const cors = require("cors");
const bodyParser = require("body-parser");
const router = require("./router");

app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));

app.use("/api", router);

app.listen(5000, () => {
    console.log(3000);
});
