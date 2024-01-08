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
    selectRefund(params) {
        return axios.get(base.baseUrl + base.selectRefund, {params})
    },
    selectTheater(params) {
        return axios.get(base.baseUrl + base.selectTheater, {params})
    },
    deleteTheater(params) {
        return axios.delete(base.baseUrl + base.deleteTheater, {params})
    },
    searchTheater(params) {
        return axios.get(base.baseUrl + base.searchTheater, {params})
    },
    refundOrder(params) {
        return axios.post(base.baseUrl + base.refundOrder, params)
    },
    addTheater(params) {
        return axios.post(base.baseUrl + base.addTheater, params)
    },
    editorTheator(params) {
        return axios.put(base.baseUrl + base.editorTheator, params)
    },
    commitRefund(params) {
        return axios.put(base.baseUrl + base.commitRefund, params)
    },
    selectTicket(params) {
        return axios.get(base.baseUrl + base.selectTicket, {params})
    },
    searchTicket(params) {
        return axios.get(base.baseUrl + base.searchTicket, {params})
    },
    addTicket(params) {
        return axios.post(base.baseUrl + base.addTicket, params)
    },
    deleteTicket(params) {
        return axios.delete(base.baseUrl + base.deleteTicket+'/' + params)
    },
    editorTicket(params) {
        return axios.put(base.baseUrl + base.editorTicket, params)
    },
    selectAdmin(params) {
        return axios.get(base.baseUrl + base.selectAdmin, {params})
    },
    deleteAdmin(params) {
        return axios.delete(base.baseUrl + base.deleteAdmin, {params})
    },
    addAdmin(params) {
        return axios.post(base.baseUrl + base.addAdmin, params)
    },
    searchAdmin(params) {
        return axios.get(base.baseUrl + base.searchAdmin, {params})
    },
    editorAdmin(params) {
        return axios.put(base.baseUrl + base.editorAdmin, params)
    },
    editorUser(params) {
        return axios.put(base.baseUrl + base.editorUser, params)
    },
    getUser(params) {
        return axios.get(base.baseUrl+ base.getUser, {params})
    },
}

export default api