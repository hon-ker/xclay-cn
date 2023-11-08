import { ref } from "vue";
import axios from "axios";

// ==========================================
// 暴露接口
// ==========================================


const USER = ref({
    id: "",
    name: "",
    des: "暂无描述……",
    avatar: "https://cdnimg103.lizhi.fm/user/2017/02/04/2583325032200238082_160x160.jpg",
    passwd: "",
    repasswd: "",
    is_manager: true,
    is_accept: true,
})

const POST = ref({
    id: "",
    title: "",
    content: Boolean(localStorage.getItem("editorContent")) ? localStorage.getItem("editorContent") : "",
    des: "",
    category: "默认",
    tag: [],
    user: "假欢",
});

const CATEGORY = ref({
    id: "",
    name: "",
    des: ""
});

const TAG = ref({
    id: "",
    name: "",
    des: ""
});

const SETTINGS = ref({
    favicon: "https://cdnimg103.lizhi.fm/user/2017/02/04/2583325032200238082_160x160.jpg",
    webside_title: "Anyway.FM",
    webside_desc: "让你的听觉更懂视觉",
    allowed_register: false,
    draft_request: false,
    allowed_comment: false,
})

// ==========================================
// 请求方法接口
// ==========================================
const BASEEND_URL = "http://127.0.0.1:8000/api"


const MyAxios = axios.create({
    baseURL: BASEEND_URL, // 设置基本URL为代理路径，后续的请求将被发送到代理服务器
    withCredentials: true, // 可选的，如果你的 API 需要使用凭据（比如 cookie），你可以设置这个选项
    // 其他 axios 配置选项
});


// ==========================================
// 请求方法
// ==========================================
const handleResponse = (promise) => {
    return promise
        .then(response => {
            if (response.data.msg !== undefined) {
                msg.success(response.data.msg);
            }
            return response.data;
        })
        .catch(error => {
            if (error.response.data.msg !== undefined && error.response.data !== null && error.response.data !== undefined) {
                msg.error(error.response.data.msg);
            }
            return Promise.reject(error);
        });
};

const getBase = url => {
    return handleResponse(MyAxios.get(url));
};

const updateBase = (url, data) => {
    return handleResponse(MyAxios.put(url, data));
};

const createBase = (url, data) => {
    return handleResponse(MyAxios.post(url, data));
};

const delBase = url => {
    return handleResponse(MyAxios.delete(url));
};

// ordinary 获取一串数据
const getAllPost = () => {
    return getBase(`${BASEEND_URL}/post/all`);
};

const getAllCategory = () => {
    return getBase(`${BASEEND_URL}/category/all`);
};

const getAllTag = () => {
    return getBase(`${BASEEND_URL}/tag/all`);
};

// ordinary 获取单个数据
const getAllUser = () => {
    return getBase(`${BASEEND_URL}/user/all`);
};

const getPost = (title) => {
    return getBase(`${BASEEND_URL}/post/${title}`);
};

const getCategory = (name) => {
    return getBase(`${BASEEND_URL}/category/${name}`);
};

const getTag = (name) => {
    return getBase(`${BASEEND_URL}/tag/${name}`);
};

const getUser = (name) => {
    return getBase(`${BASEEND_URL}/user/${name}`);
};

// admin get one ------------------------------------

const adminGetPostByTitle = title => {
    return getBase(`${BASEEND_URL}/admin/post/${title}`);
};

const adminGetCategoryByName = name => {
    return getBase(`${BASEEND_URL}/admin/category/${name}`);
};

const adminGetTagByName = name => {
    return getBase(`${BASEEND_URL}/admin/tag/${name}`);
};

const adminGetUserByName = name => {
    return getBase(`${BASEEND_URL}/admin/user/${name}`);
};

// admin get one ------------------------------------

const adminGetPostById = id => {
    return getBase(`${BASEEND_URL}/admin/post/${id}`);
};

const adminGetCategoryById = id => {
    return getBase(`${BASEEND_URL}/admin/category/${id}`);
};

const adminGetTagById = id => {
    return getBase(`${BASEEND_URL}/admin/tag/${id}`);
};

const adminGetUserById = id => {
    return getBase(`${BASEEND_URL}/admin/user/${id}`);
};
// admin get all ------------------------------------

const adminGetAllPost = () => {
    return getBase(`${BASEEND_URL}/admin/post/all`);
};

const adminGetAllCategory = () => {
    return getBase(`${BASEEND_URL}/admin/category/all`);
};

const adminGetAllTag = () => {
    return getBase(`${BASEEND_URL}/admin/tag/all`);
};

const adminGetAllUser = () => {
    return getBase(`${BASEEND_URL}/admin/user/all`);
};

// admin update ------------------------------------

const adminUpdatePost = data => {
    return updateBase(`${BASEEND_URL}/admin/post/id`, data);
};

const adminUpdateCategory = data => {
    return updateBase(`${BASEEND_URL}/admin/category/id`, data);
};

const adminUpdateTag = data => {
    return updateBase(`${BASEEND_URL}/admin/tag/id`, data);
};

const adminUpdateUser = data => {
    return updateBase(`${BASEEND_URL}/admin/user/id`, data);
};

// admin create  ------------------------------------

const adminCreatePost = data => {
    return createBase(`${BASEEND_URL}/admin/post`, data);
};

const adminCreateCategory = data => {
    return createBase(`${BASEEND_URL}/admin/category`, data);
};

const adminCreateTag = data => {
    return createBase(`${BASEEND_URL}/admin/tag`, data);
};

const adminCreateUser = data => {
    return createBase(`${BASEEND_URL}/admin/user`, data);
};

// admin del all ------------------------------------

const adminDelPost = id => {
    return delBase(`${BASEEND_URL}/admin/post/${id}`);
};

const adminDelCategory = id => {
    return delBase(`${BASEEND_URL}/admin/category/${id}`);
};

const adminDelTag = id => {
    return delBase(`${BASEEND_URL}/admin/tag/${id}`);
};

const adminDelUser = id => {
    return delBase(`${BASEEND_URL}/admin/user/${id}`);
};

// ==========================================
// 暴露接口
// ==========================================

export { POST, USER, SETTINGS, CATEGORY, TAG }
export { MyAxios }