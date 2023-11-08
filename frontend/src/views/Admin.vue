<template>
    <div class="wrap min container">
        <n-space vertical>

            <n-tabs v-model:value="selectedTab" key="line" type="line" animated placement="right"
                @before-leave="handleBeforeLeave">
                <n-tab-pane name="settings" tab="首页" display-directive="show">
                    <User></User>
                </n-tab-pane>

                <n-tab-pane name="editor" tab="编辑器" display-directive="show">
                    <Editor :post="POST" :isNewPost="isNewPost"></Editor>
                </n-tab-pane>

                <!-- <n-tab-pane v-if="USER.is_manager" name="new" tab="添加" display-directive="show">
                    <New></New>
                </n-tab-pane> -->

                <n-tab-pane v-if="USER.is_manager" name="post" tab="草稿" display-directive="show">
                    <n-space class="table-header-btn margin-bottom">
                        <div class="left">
                            <n-button>新增</n-button>
                            <n-button>回收</n-button>
                            <n-button>保存</n-button>
                            <n-button type="error" ghost>删除</n-button>

                        </div>

                        <n-button>刷新</n-button>
                    </n-space>
                    <n-data-table :paginate-single-page="false" default-expand-all size="small" :columns="postColumns"
                        :data="postData" :pagination="pagination" />
                </n-tab-pane>

                <n-tab-pane v-if="USER.is_manager" name="category" tab="分类" display-directive="show">
                    <n-space class="table-header-btn margin-bottom">
                        <div class="left">
                            <n-button>新增</n-button>
                            <n-button>删除</n-button>
                            <n-button>保存</n-button>
                        </div>

                        <n-button>刷新</n-button>
                    </n-space>
                    <n-data-table :paginate-single-page="false" default-expand-all size="small" :columns="categoryColumns"
                        :data="categoryData" :pagination="pagination" />
                </n-tab-pane>

                <n-tab-pane v-if="USER.is_manager" name="tag" tab="标签" display-directive="show">
                    <n-space class="table-header-btn margin-bottom">
                        <div class="left">
                            <n-button>新增</n-button>
                            <n-button>删除</n-button>
                            <n-button>保存</n-button>
                        </div>

                        <n-button>刷新</n-button>
                    </n-space>
                    <n-data-table :paginate-single-page="false" default-expand-all size="small" :columns="tagColumns"
                        :data="tagData" :pagination="pagination" />
                </n-tab-pane>

                <n-tab-pane v-if="USER.is_manager" name="user" tab="用户" display-directive="show">
                    <n-space class="table-header-btn margin-bottom">
                        <div class="left">
                            <n-button>新增</n-button>
                            <n-button>删除</n-button>
                            <n-button>保存</n-button>
                        </div>

                        <n-button>刷新</n-button>
                    </n-space>
                    <n-data-table :paginate-single-page="false" default-expand-all size="small" :columns="userColumns"
                        :data="userData" :pagination="pagination" />
                </n-tab-pane>
            </n-tabs>
        </n-space>

    </div>
</template>

<script lang="ts" setup>
import { h, defineComponent, ref, onMounted, onBeforeUnmount, watch, onBeforeMount } from 'vue'
import { MyAxios,POST, USER, SETTINGS, TAG, CATEGORY } from '../assets/clay.utils';
import Editor from '../components/modules/Editor.vue';
import New from '../components/modules/New.vue';
import User from '../components/modules/User.vue';
// import axios from 'axios';
import { NEmpty, NTabs, NInput, NSelect, NRadio, NRadioGroup, NTabPane, NDivider, NGrid, NGridItem, NTag, NButton, useMessage, NSpace, NDataTable, NSwitch, NImage, NAvatar } from 'naive-ui'
const msg = useMessage();

const BASEEND_URL = "http://127.0.0.1:8000/api"
const isNewPost = ref(false)

const TAB_TYPE = ref()





// 切换tab
const switchTab = (tabName) => {
    selectedTab.value = tabName; // 切换选项卡
};



const checkedOptions = (data) => {
    if (data.value.length == 0) {
        return [];

    } else {
        return data.value.map(item => ({
            value: item.name,
            label: item.name,
            key: item.id
        }));
    }
};

const createPostColumns = ({
    saveRow,
    deleteRow,
    editRow
}) => {
    return [
        {
            type: 'expand',
            renderExpand: (rowData) => {
                return h(NInput, {
                    value: rowData.des,
                    placeholder: "文章摘要",
                    type: "textarea",
                    autosize: {
                        minRows: 3,
                        maxRows: 5
                    },
                    "on-update:value": (value, option) => {
                        rowData.des = value
                        // 在值更新时执行的回调函数
                    }
                })
            }
        },
        {
            title: "#",
            key: "id",
        },
        {
            title: "标题",
            key: "title",
            render(row, index) {
                return h(NInput, {
                    value: row.title,
                    style: {
                        "max-width": "15em",
                        "text-overflow": "ellipsis",
                    },
                    onUpdateValue(v) {
                        row.title = v;
                    }
                });
            }
        },
        {
            title: "用户",
            key: "user",
        },
        {
            title: '分类',
            key: 'category',
            render(row) {
                return h(NSelect, {
                    "v-model:value": row.category,
                    value: row.category,
                    filterable: true,
                    tag: true,

                    placeholder: row.category,
                    style: {
                        "max-width": "15em",
                        "text-overflow": "ellipsis",
                    },
                    options: checkedOptions(categoryData),
                    "on-update:value": (value, option) => {
                        row.category = value
                        // 在值更新时执行的回调函数
                    }
                });
            },
        },
        {
            title: "标签",
            key: "tag",
            render(row) {
                return h(NSelect, {
                    "v-module:value": row.tag,
                    "max-tag-count": "responsive",
                    class: "admin-tag",
                    tag: true,
                    value: row.tag,
                    type: "success",
                    filterable: true,
                    placeholder: row.tag,
                    multiple: true,
                    style: {
                        "min-width": "10em",
                        "text-overflow": "ellipsis",
                    },
                    options: checkedOptions(tagData),
                    "on-update:value": (value) => {
                        row.tag = value
                    }
                })
            }
        },
        {
            title: "Action",
            key: "actions",
            render(row) {
                return [
                    h(
                        NButton,
                        {
                            size: "small",
                            class: "action-button",
                            onClick: () => editRow(row)
                        },
                        { default: () => "编辑" }
                    ), h(
                        NButton,
                        {
                            size: "small",
                            class: "action-button",
                            onClick: () => deleteRow(row)
                        },
                        { default: () => "删除" }
                    ), h(
                        NButton,
                        {
                            class: "action-button",
                            size: "small",
                            onClick: () => saveRow(row)
                        },
                        { default: () => "保存" }
                    )
                ]
            }
        }
    ];
};

const createCategoryOrTagColumns = ({
    saveRow,
    deleteRow,
    editRow
}) => {
    return [
        {
            title: "#",
            key: "id",
        },
        {
            title: "名称",
            key: "name",
            render(row) {
                return h(NInput, {
                    value: row.name,
                    onUpdateValue(v) {
                        row.name = v;
                    }
                });
            }
        },
        {
            title: "描述",
            key: "des",
            render(row) {
                return h(NInput, {
                    value: row.des,
                    placeholder: "请输入描述",
                    onUpdateValue(v) {
                        row.des = v;
                    }
                });
            }
        },
        {
            title: "Action",
            key: "actions",
            render(row) {
                return [
                    h(
                        NButton,
                        {
                            class: "action-button",
                            size: "small",
                            onClick: () => deleteRow(row)
                        },
                        { default: () => "删除" }
                    ), h(
                        NButton,
                        {
                            class: "action-button",
                            size: "small",
                            onClick: () => saveRow(row)
                        },
                        { default: () => "保存" }
                    )
                ]
            }
        }
    ];
};

const createUserColumns = () => {
    return [
        {
            type: 'selection'
        },
        // {
        //     type: 'expand',
        //     renderExpand: (rowData) => {
        //         return rowData.des
        //     }
        // },
        {
            title: "#",
            key: "id",
        },
        {
            title: "头像",
            key: "avatar",
            render(row) {
                return h(NAvatar, {
                    src: USER.value.avatar,
                    size: "medium",
                    style: {
                        "align-items": "center",
                        "vertical-align": "middle"
                    }
                });
            }
        },
        {
            title: "名称",
            key: "name",
        },
        // {
        //     title: "描述",
        //     key: "des",
        // },
        {
            title: "管理员",
            key: "is_manager",
            render(row) {
                return h(NSwitch, {
                    value: row.is_manager,
                    onUpdateValue(v) {
                        row.is_manager = v;
                    }
                });
            }
        },
        {
            title: "Token",
            key: "is_accept",
            render(row) {
                return h(NSwitch, {
                    value: row.is_accept,
                    onUpdateValue(v) {
                        row.is_accept = v;
                    }
                });
            }
        },
        {
            title: "Action",
            key: "actions",
            render(row) {
                return [
                    h(
                        NButton,
                        {
                            class: "action-button",
                            size: "small",
                            onClick: () => {
                                let url = `${BASEEND_URL}/admin/${TAB_TYPE.value}/id/${row.id}`
                                MyAxios.delete(url).then(res =>
                                    msg.success(res.data.msg)
                                )
                            }
                        },
                        { default: () => "删除" }
                    ), h(
                        NButton,
                        {
                            class: "action-button",
                            size: "small",
                            onClick: () => {
                                let url = `${BASEEND_URL}/admin/${TAB_TYPE.value}/id`
                                MyAxios.put(url, row).then(res =>
                                    msg.success(res.data.msg)
                                )
                            }
                        },
                        { default: () => "保存" }
                    )
                ]
            }
        }
    ];
};

const commonActions = {


    saveRow(rowData) {
        let url = `${BASEEND_URL}/admin/${TAB_TYPE.value}/id`

        if (TAB_TYPE.value == "category" || TAB_TYPE.value == "tag") {
            MyAxios.put(url, rowData).then(res => {
                // categoryData.value = res.data
                msg.success(res.data.msg)
            })
        } else if (TAB_TYPE.value == "post") {
            MyAxios.put(url, rowData).then(res => {
                // categoryData.value = res.data
                msg.success(res.data.msg)

            })
        }

    },
    deleteRow(rowData) {
        let url = `${BASEEND_URL}/admin/${TAB_TYPE.value}/id/${rowData.id}`
        MyAxios.delete(url).then(res => {
            categoryData.value = res.data
        })
    },
    editRow(rowData) {
        let url = `${BASEEND_URL}/admin/${TAB_TYPE.value}/id/${rowData.id}`
        // 如果是post，请求相关信息并发送到编辑器
        if (TAB_TYPE.value == "post") {
            MyAxios.get(url).then(res => {
                POST.value = res.data
                switchTab("editor")
                isNewPost.value = true
            })

        }

    }
}

// 表格的数据
// 为每个选项卡添加对应的数据引用
const postData = ref([]);
const categoryData = ref([]);
const tagData = ref([]);
const userData = ref([]);

const postColumns = createPostColumns(commonActions)
const categoryColumns = createCategoryOrTagColumns(commonActions)
const tagColumns = createCategoryOrTagColumns(commonActions)
const userColumns = createUserColumns()

function getCategoryData() {
    MyAxios.get("http://127.0.0.1:8000/api/admin/category/all").then(res => {
        categoryData.value = res.data
    })
}

function getTagData() {
    MyAxios.get('http://127.0.0.1:8000/api/admin/tag/all').then(res => {
        tagData.value = res.data
    })
}

function getUserData() {
    MyAxios.get(`http://127.0.0.1:8000/api/admin/user/all`).then(res => {
        userData.value = res.data
    })
}

// 获取post信息
function getPostData() {
    getCategoryData()
    getTagData()
    MyAxios.get("http://127.0.0.1:8000/api/admin/category/all").then(res => {
        postData.value = res.data
    })
}


// 点击tab事件
const handleBeforeLeave = async (tabName: string) => {
    switch (tabName) {
        case 'post':
            getPostData()
            TAB_TYPE.value = "post"
            return true;

        case 'category':
            getCategoryData()
            TAB_TYPE.value = "category"
            return true;

        case 'tag':
            getTagData()
            TAB_TYPE.value = "tag"
            return true;


        case 'user':
            getUserData()
            TAB_TYPE.value = "user"
            return true;

        default:
            return true;
    }
};

// 受控模式的tab选择
const selectedTab = ref(localStorage.getItem("tab")); // 当前选中的选项卡
// 加载时执行一次
handleBeforeLeave(selectedTab.value)


const pagination = {
    pageSize: 10
}


// -----------------------------------------
// 加载时获取数据
// -----------------------------------------
// 突发关闭或者跳转到其他时当前访问的tab存入浏览器

window.addEventListener('beforeunload', function (event) {
    // 你需要保存的数据
    localStorage.setItem("tab", selectedTab.value);
});


</script>

<style>
main {
    padding-top: 3.8em;
    margin-top: 0em;
}

table {
    margin: 0;
}

table td,
table th {
    width: auto !important;
}


@media screen and (min-width: 1200px) {
    .wrap.min {
        min-width: 70em;
        width: 100%;
    }
}


.container {
    margin: 0 auto;

}

.action-button {
    margin-right: 3px;
}

.admin-tag {
    min-width: 3em;

}

.wrap.min.container .n-input.n-input--autosize .n-input__textarea-el,
.n-input.n-input--autosize .n-input__input-el {
    position: absolute;
    top: 0px !important;
    left: 0;
    height: 100%;
}

.n-tab-pane {
    padding: 15px !important;
    max-height: 100vh;
    overflow: scroll;
}

.n-tabs-nav--line-type.n-tabs-nav--right.n-tabs-nav {
    max-height: 100vh;
    overflow: hidden;
    padding: 15px 0 !important;

}

.n-tab-pane::-webkit-scrollbar,
.n-tabs-nav--line-type.n-tabs-nav--right.n-tabs-nav::-webkit-scrollbar {
    display: none;
}

.margin-bottom {
    margin-bottom: 15px;
}

.table-header-btn {
    display: flex;
    justify-content: space-between !important;
}

.table-header-btn button {
    margin-right: 5px;
}

.table-header-btn button:last-child {
    margin-right: 0px;
}

/* .table-header-btn .error-btn{
    background-color: transparent !important;
    border: 1px solid #ddd !important;
    color: ;
} */
</style>