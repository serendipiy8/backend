// import { createConnection } from "mysql"
const mysql = require("mysql")

const client = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "20030205",
    database: "ticket-app"
})

client.connect((err) => {
    if (err) throw err
    console.log('Connected!')
})

const sqlClient = (sql, arr, callback) => {
    client.query(sql, arr, (error, result) => {
        if (error) {
            console.log(error)
            return
        }
        callback(result)
    })
}

module.exports = sqlClient