// 开发环境下配置
const DEV_CONFIG = {
    // 标题
    APP_NAME: "演出售票系统课设",

    // 版本号
    APP_VER: "1.0.0",

    // 接口地址
    API_URL: "/",

    // 请求超时
    TIMEOUT: 10000,

    // TokenName
    TOKEN_NAME: "Authorization",

    // Token前缀，注意最后有个空格，如不需要需设置空字符串
    TOKEN_PREFIX: "",

    // 追加其他头
    HEADERS: {},

    // 请求是否开启缓存
    REQUEST_CACHE: false,

    // 布局 默认：default | 通栏：header | 经典：menu | 功能坞：dock
    // dock将关闭标签和面包屑栏
    LAYOUT: 'menu',

    // 菜单是否折叠
    MENU_IS_COLLAPSE: false,

    // 是否开启多标签
    LAYOUT_TAGS: true,

    // 主题颜色
    COLOR: '',

    // 角色定义
    ROLE_LIST: [{
        "role": "student",
        "roleName": "学生"
    },
    {
        "role": "teacher",
        "roleName": "老师"
    },
    {
        "role": "admin",
        "roleName": "管理员"
    }
    ],
    //IMG_BASEURL: "http://innovate.quwancode.com/"

}

// 生产环境下额外的配置，覆盖开发环境的配置


let APP_CONFIG = DEV_CONFIG


export default APP_CONFIG