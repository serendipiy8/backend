import store from "../store"

if(localStorage.getItem("ticket")){
    store.commit("login/setUser",JSON.parse(localStorage.getItem("ticket")))
}