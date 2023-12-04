// import { Router } from "express"
// const router = Router()
// import sqlClient from "./config.js"
const express = require("express")
const router = express.Router()
const sqlClient = require("./config")
const jwt = require("jsonwebtoken")

//注册
router.post("/register", (req, res) => {
    const { username, password, email } = req.body
    const sql = "insert into userTest values(null,?,?,?)"
    const arr = [username, password, email]
    sqlClient(sql, arr, result => {
        console.log(result)
        if (result.affectedRows > 0) {
            res.send({
                status: 200,
                msg: "注册成功"
            })
        } else {
            res.send({
                status: 401,
                msg: "注册失败"
            })
        }
    })
})


//登录
router.post("/login", (req, res) => {
    const { username, password } = req.body;
    const sql = "select * from userTest where username=? and password=?"
    const arr = [username, password]
    sqlClient(sql, arr, result => {
        if (result.length > 0) {
            let token = jwt.sign({
                username,
                id:result[0].id
            },'soomekeys')

            res.send({
                status: 200,
                token,
                username
            })
        } else {
            res.send({
                status: 401,
                msg: "登录失败"
            })
        }
    })
})




module.exports = router