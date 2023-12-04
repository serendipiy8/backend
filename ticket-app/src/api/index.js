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
    }
}

export default api