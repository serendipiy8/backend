// const base = {
//     baseUrl: "http://127.0.0.1:5000",
//     register: "/api/register",
//     login: "/api/login"
// }

const base = {
    baseUrl: "http://39.106.37.28:5000",
    // baseUrl: "http://127.0.0.1:5000",
    register: "/users/register",
    login: "/users/login",
    // selectOrder: "/orders/queryUser",
    selectOrder: "/Orders",
    adminLogin: "/administrators/login",
    selectRefund:"/Refunds",
    selectTheater:"/Theaters",
    deleteTheater:"/theaters",
    searchTheater:"/theaters",
    addTheater:"/theaters",
    editorTheator:"/theaters",
    refundOrder:"/refunds",
    
}


export default base