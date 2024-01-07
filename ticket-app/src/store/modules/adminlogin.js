const getters = {
    getAdminID: state => state.user.data.AdminID,
    getPermissions: state => state.user.data.Permissions
};
export default {
    namespaced: true,
    state: {
        user: {
            data: {
                AdminID: "",
                Permissions: ""
            },
            token: ""
        }
    },
    mutations: {
        setAdmin(state, user) {
            state.user = user;
        }
    },
    getters
};
