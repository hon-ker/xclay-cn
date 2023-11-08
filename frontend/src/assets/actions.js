// ==========================================
// 请求方法接口
// ==========================================
const MyAxios = {
    get: (url) => {
        return axios.get(url)
    },
    post: (url, data) => {
        return axios.post(url, data)
    },
    put: (url, data) => {
        return axios.put(url, data)
    },
    del: (url) => {
        return axios.delete(url)
    }
}

// ==========================================
// 请求方法
// ==========================================
const handleResponse = (promise, msg) => {
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

const getBase = (url, msg) => {
    return handleResponse(MyAxios.get(url), msg);
};

const updateBase = (url, data, msg) => {
    return handleResponse(MyAxios.put(url, data), msg);
};

const createBase = (url, data, msg) => {
    return handleResponse(MyAxios.post(url, data), msg);
};

const delBase = (url, msg) => {
    return handleResponse(MyAxios.delete(url), msg);
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