<template>
    <n-input-group>
        <n-input-group-label>新建</n-input-group-label>
        <n-select placeholder="请选择一项新建" v-model:value="createType" :options="options" :on-update:value="choseCreateType" />

    </n-input-group>
    <n-space vertical>
    </n-space>
    <!-- 文章的表单 -->
    <n-space class="new-item draft" v-if="createType == 'post'" vertical>

        <Editor :draft="post"></Editor>
        <pre class="new-item pre">{{ JSON.stringify(post, "", 2) }}</pre>

    </n-space>
    <!-- 分类的表单 -->
    <n-space class="new-item" v-if="createType == 'category'" vertical>
        <n-form>
            <n-form-item label="名称" path="inputValue">
                <n-input  clearable  v-model:value="category.name" placeholder="分类名" />
            </n-form-item>
            <n-form-item label="描述" path="textareaValue">
                <n-input  clearable v-model:value="category.des" placeholder="对该分类的描述" type="textarea" :autosize="{
                    minRows: 3,
                    maxRows: 5
                }" />
            </n-form-item>
            <!-- 新建按钮 -->
            <n-button block secondary strong tag="div" @click="submitCategory">
                新建
            </n-button>
        </n-form>
        <pre class="new-item pre">{{ JSON.stringify(category, "", 2) }}</pre>

    </n-space>
    <!-- tag的表单 -->
    <n-space class="new-item" v-if="createType == 'tag'" vertical>
        <n-form>
            <n-form-item label="名称" path="inputValue">
                <n-input  clearable v-model:value="tag.name" placeholder="标签名" />
            </n-form-item>
            <n-form-item label="描述" path="textareaValue">
                <n-input  clearable v-model:value="tag.des" placeholder="对该标签的描述" type="textarea" :autosize="{
                    minRows: 3,
                    maxRows: 5
                }" />
            </n-form-item>

            <!-- 新建按钮 -->
            <n-button block secondary strong tag="div" @click="submitTag">
                新建
            </n-button>
        </n-form>


        <pre class="new-item pre">{{ JSON.stringify(tag, "", 2) }}</pre>

    </n-space>

    <!-- user的表单 -->
    <n-space class="new-item" v-if="createType == 'user'" vertical>
        <n-form label-placement="left" label-width="auto">
            <n-form-item label="头像" path="inputValue">
                <n-image class="self-avaver" width="200" :src="user.avatar" />
            </n-form-item>

            <n-form-item label="名称" path="inputValue">
                <n-input  clearable v-model:value="user.name" placeholder="用户名" />
            </n-form-item>
            <n-form-item label="简介" path="textareaValue">
                <n-input  clearable v-model:value="user.des" placeholder="用户简介" type="textarea" :autosize="{
                    minRows: 3,
                    maxRows: 5
                }" />
            </n-form-item>
            <n-form-item label="邮箱">
                <n-auto-complete v-model:value="user.mail" :options="mailComplate" placeholder="邮箱" size="medium" />
            </n-form-item>

            <n-form-item label="密码">
                <n-input  clearable v-model:value="user.passwd" type="password" show-password-on="click" placeholder="密码"
                    :maxlength="8" />
            </n-form-item>
            <n-form-item label="确认">
                <n-input  clearable v-model:value="user.repasswd" type="password" show-password-on="click" placeholder="密码"
                    :maxlength="8" />
            </n-form-item>

            <n-form-item label="秘钥" path="textareaValue">
                <n-input  clearable v-model:value="user.token" placeholder="秘钥" type="textarea" :autosize="{
                    minRows: 3,
                    maxRows: 5
                }" />
            </n-form-item>
            <n-form-item label="管理员" path="inputValue">
                <n-switch v-model:value="user.is_manager" />
            </n-form-item>
            <n-form-item label="通行证" path="inputValue">
                <n-switch v-model:value="user.is_accept" />
            </n-form-item>

            <!-- 新建按钮 -->
            <n-button block strong tag="div" @click="submitUser">
                新建
            </n-button>
        </n-form>


        <pre class="new-item pre">{{ JSON.stringify(user, "", 2) }}</pre>
    </n-space>
</template>
  
<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { NImage, NInputGroup, NInputGroupLabel, NSwitch, NAutoComplete, NTooltip, NButton, NDivider, useMessage, NForm, NFormItem, NInput, NSelect, NSpace } from "naive-ui";
import Editor from './Editor.vue';

const BACKEND_URL = "http://127.0.0.1:8000/admin";

// -------------------------------------------
// 新建项的模版
// -------------------------------------------
const post = ref({
    title: "",
    content: " ",
    des: "暂无描述……",
    tag: [],
    category: "默认",
    user: "xclay",
})


const category = ref({
    name: "",
    des: "暂无描述……"
})

const tag = ref({
    name: "",
    des: "暂无描述……"
})

const user = ref({
    name: "",
    des: "暂无描述……",
    avatar: "https://cdnimg103.lizhi.fm/user/2017/02/04/2583325032200238082_160x160.jpg",
    mail: "",
    is_manager: false,
    is_accept: true,
    passwd: "##12138",
    repasswd: "##12138",
    token: "",
})

const createType = ref("category")
const message = useMessage()
const options = [
    {
        label: "---文章类----",
        value: "---",
        disabled: true
    },
    {
        label: "文章",
        value: "post"
    },
    {
        label: "分类",
        value: "category"
    },
    {
        label: "标签",
        value: "tag",
    },
    {
        label: "---其他----",
        value: "----",
        disabled: true
    },
    // {
    //     label: "一言",
    //     value: "line"
    // },
    // {
    //     label: "漏洞",
    //     value: "vul"
    // },
    // {
    //     label: "表情包",
    //     value: "emoji"
    // },
    {
        label: "用户",
        value: "user",
    }
]

const mailComplate = computed(() => {
    return ["@qq.com", "@163.com", "@gmail.com", , "@xclay.cn", "@outlook.com"].map((suffix) => {
        const prefix = user.value.mail.split("@")[0];
        return {
            label: prefix + suffix,
            value: prefix + suffix
        };
    });
})
function choseCreateType(value, option) {
    createType.value = value
    // message.info(value)
}

// -------------------------------------------
// submit按钮
// -------------------------------------------
// 封装的函数
function submitBase(api, data) {
    axios.post(`${BACKEND_URL}/${api}`, data)
        .then(response => {
            data = {}
            message.success(response.data.msg)
            
        })
        .catch(error => {
            console.log(data);
            message.error("提交失败!")
        });
}
// 提交分类
const submitCategory = () => {
    submitBase("category", category.value)
}
const submitTag = () => {
    submitBase("tag", tag.value)
}
const submitUser = () => {
    submitBase("user", user.value)
}
</script>

<style>
.new-item {
    margin-top: 20px;
}

.new-item.draft,
.new-item.pre {
    margin-top: 10px;
}
</style>