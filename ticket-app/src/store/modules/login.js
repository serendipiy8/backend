const getters = {
    getUserID: state => state.user.data.UserID
};

export default {
    namespaced: true,
    state: {
        user: {
            data: {
                UserID: "",
                username: "",
                // 其他可能的属性
            },
            token: ""
        }
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        }
    },
    getters
};
