import axios from "../utils/request";
import base from "./base";

const api = {
    //注册
    register(params) {
        return axios.post(base.baseUrl + base.register, params)
    },
    //登录
    login(params) {
        return axios.post(base.baseUrl + base.login, params)
    },
    selectOrder(params) {
        return axios.get(base.baseUrl + base.selectOrder, {params})
    },
    adminLogin(params) {
        return axios.post(base.baseUrl + base.adminLogin, params)
    },
}

export default api