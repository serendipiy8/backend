import axios from 'axios'
import { ElNotification, ElMessageBox } from 'element-plus'
import sysConfig from "@/config"
import router from '@/router'
import qs from "qs"
import store from "../store"

axios.defaults.baseURL = "http://localhost:8080/" 

axios.defaults.timeout = sysConfig.TIMEOUT

// HTTP request 拦截器
axios.interceptors.request.use(

    (config) => {
        let token = localStorage.getItem('TOKEN')
        if (token) {
            config.headers['token'] = token
        }
        // 避免被缓存命中，强制拉取远程
        if (!sysConfig.REQUEST_CACHE && config.method === 'get') {
            config.params = config.params || {}
            config.params['_'] = new Date().getTime()

        }
        Object.assign(config.headers, sysConfig.HEADERS)
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

// HTTP response 拦截器
axios.interceptors.response.use(
    (response) => {
        const res = response.data
        if(res.code) {
            if (res.code === 200) {
                return Promise.resolve(res) }
            else if(res.code === 400) {
                ElNotification({
                    title: '提示',
                    message: '请先登录',
                    type: 'warning'
                })
                router.push('/login')
            }else if(res.code === 401) {
                ElNotification({
                    title: '提示',
                    message: '登录已过期',
                    type: 'warning'
                })
                localStorage.removeItem('TOKEN')
                router.push('/login')
            } else if(res.code === 404) {
                ElNotification({
                    title: '提示',
                    message: '您无权访问该页面',
                    type: 'warning'
                })
                router.push('/login')
            }else {
                return Promise.reject(res)
            }
        }
        return Promise.resolve(res)
    },
    (error) => {
        if (error.response) {
            if (error.response.status === 404) {
                ElNotification.error({
                    title: '请求错误',
                    message: "Status:404，正在请求不存在的服务器记录！"
                })
            } else if (error.response.status === 500) {
                ElNotification.error({
                    title: '请求错误',
                    message: error.response.data.message || "Status:500，服务器发生错误！"
                })
            } else if (error.response.status === 401) {
                ElMessageBox.confirm('当前用户已被登出或无权限访问当前资源，请尝试重新登录后再操作。', '无权限访问', {
                    type: 'error',
                    closeOnClickModal: false,
                    center: true,
                    confirmButtonText: '重新登录'
                }).then(() => {
                    router.replace({ path: '/login' })
                }).catch(() => {})
            } else {
                ElNotification.error({
                    title: '请求错误',
                    message: error.response.data.message || `Status:${error.response.status}，未知错误！`
                })
            }
        } else {
            ElNotification.error({
                title: '请求错误',
                message: "请求服务器无响应！"
            })
        }
        return Promise.reject(error.response)
    }
)
export default axios