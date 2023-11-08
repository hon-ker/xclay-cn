<template>
    <!-- 仪表盘 -->
    <n-card class="user-card">
        <n-breadcrumb>
            <n-breadcrumb-item>2023年</n-breadcrumb-item>
            <n-breadcrumb-item>11月</n-breadcrumb-item>
            <n-breadcrumb-item>09日</n-breadcrumb-item>
            <n-breadcrumb-item>03:03</n-breadcrumb-item>
        </n-breadcrumb>
        <n-row class="user-header">
            <div>
                <n-avatar :size="36" :src="settings.favicon" />
                <div class="user-header-name">{{ settings.webside_title }}</div>
                <div class="user-header-des">{{ settings.webside_desc }}</div>
            </div>
            <NButton @click="refreshPage">刷新</NButton>
        </n-row>
        <n-row>
            <n-col :span="5">
                <n-statistic label="文章">
                    <n-number-animation ref="numberAnimationInstRef" :from="0" :to="9" /> 篇
                </n-statistic>
            </n-col>
            <n-col :span="5">
                <n-statistic label="分类">
                    <n-number-animation ref="numberAnimationInstRef" :from="0" :to="39" /> 个
                </n-statistic>
            </n-col>

            <n-col :span="5">
                <n-statistic label="标签">
                    <n-number-animation ref="numberAnimationInstRef" :from="0" :to="19" /> 个

                </n-statistic>
            </n-col>
            <n-col :span="5">
                <n-statistic label="用户">
                    <n-number-animation ref="numberAnimationInstRef" :from="0" :to="91" /> 例
                </n-statistic>
            </n-col>
            <n-col :span="4">
                <n-statistic label="漏洞">
                    <n-number-animation ref="numberAnimationInstRef" :from="0" :to="13" /> 例
                </n-statistic>
            </n-col>
        </n-row>
    </n-card>
    <!-- 个人 -->
    <n-card class="user-card">
        <n-tabs type="line" animated>
            <n-tab-pane name="self" tab="个人">
                <!-- 个人相关 -->
                <n-form class="self-form" label-placement="left" label-width="auto" require-mark-placement="right-hanging">
                    <n-form-item label="头像" path="inputValue">
                        <n-image class="self-avaver" width="200" :src="user.avatar" />
                    </n-form-item>
                    <n-form-item label="名称" path="inputValue">
                        <n-input v-model:value="user.name" placeholder="昵称，用户唯一标识" />
                    </n-form-item>
                    <n-form-item label="简介" path="textareaValue">
                        <n-input v-model:value="user.des" placeholder="个人简介" type="textarea" :autosize="{
                            minRows: 3,
                            maxRows: 5
                        }" />
                    </n-form-item>
                    <n-form-item label="密码" path="inputValue">
                        <n-input v-model:value="user.passwd" placeholder="输入密码" type="password" />
                    </n-form-item>
                    <n-form-item label="重输" path="inputValue">
                        <n-input v-model:value="user.repasswd" placeholder="确认密码" type="password" />
                    </n-form-item>
                    <n-form-item label="秘钥" path="textareaValue">
                        <n-input v-model:value="user.token" placeholder="调用api或者快捷登录的唯一凭证" type="textarea" :autosize="{
                            minRows: 3,
                            maxRows: 5
                        }" />
                    </n-form-item>
                    <n-form-item label="Token" path="inputValue">
                        <n-switch v-model:value="user.is_accept" />
                    </n-form-item>
                    <!-- 保存按钮 -->
                    <n-button tag="div" @click="updateDraft">
                        保存
                    </n-button>
                </n-form>

            </n-tab-pane>
            <n-tab-pane v-if="user.is_manager" name="settings" tab="设置">
                <!-- 个人相关 -->
                <n-form class="self-form" label-placement="left" label-width="auto" require-mark-placement="right-hanging">
                    <n-form-item label="网站icon" path="inputValue">
                        <n-image class="self-avaver" width="40" :src="settings.favicon" />
                    </n-form-item>
                    <n-form-item label="网站名称" path="inputValue">
                        <n-input v-model:value="settings.webside_title" placeholder="网站名称" />
                    </n-form-item>
                    <n-form-item label="网站简介" path="textareaValue">
                        <n-input v-model:value="settings.webside_desc" placeholder="网站简介" type="textarea" :autosize="{
                            minRows: 3,
                            maxRows: 5
                        }" />
                    </n-form-item>
                    <n-form-item label="开放注册" path="inputValue">
                        <n-switch v-model:value="settings.allowed_register" />
                    </n-form-item>
                    <n-form-item label="开放投稿" path="inputValue">
                        <n-switch v-model:value="settings.draft_request" />
                    </n-form-item>
                    <n-form-item label="允许评论" path="inputValue">
                        <n-switch v-model:value="settings.allowed_comment" />
                    </n-form-item>
                    <!-- 保存按钮 -->
                    <n-button tag="div" @click="updateDraft">
                        保存
                    </n-button>
                </n-form>
            </n-tab-pane>
        </n-tabs>
    </n-card>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { NImage, NSwitch, NTab, NTabPane, NTabs, NRadioGroup, NRadio, NRow, NCol, NNumberAnimation, NCard, NAvatar, NPageHeader, NDropdown, NGrid, NGi, NBreadcrumb, NBreadcrumbItem, NStatistic, NTooltip, NButton, NDivider, useMessage, NForm, NFormItem, NInput, NSelect, NSpace } from "naive-ui";

const tag = ref({
    name: "",
    des: "暂无描述……"
})

const user = ref({
    id: "",
    name: "xclay",
    des: "暂无描述……",
    avatar: "https://cdnimg103.lizhi.fm/user/2017/02/04/2583325032200238082_160x160.jpg",
    passwd: "",
    repasswd: "",
    is_manager: true,
    is_accept:true

})

const settings = ref({
    favicon: "https://cdnimg103.lizhi.fm/user/2017/02/04/2583325032200238082_160x160.jpg",
    webside_title: "Anyway.FM",
    webside_desc: "让你的听觉更懂视觉",
    allowed_register: false,
    draft_request: false,
    allowed_comment: false,
})


function refreshPage() {
    location.reload();
}
</script>

<style>
.user-card {
    margin-bottom: 10px;
}

.number {

    font-size: 58px !important;
}

.user-col {

    margin-bottom: 10px !important;
}

.user-header {
    display: flex;
    align-items: center;
    margin: 20px 0 !important;
    font-family: v-sans, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

.user-header>div:first-child {
    margin-right: auto;
    display: flex;
    align-items: center;
}

.user-header .user-btn {
    margin-left: 10px;
}

.user-header-name {
    font-size: 18px;
    font-weight: 500;
    color: #000;
    margin: 0 10px;

}

.user-header-des {
    font-size: 14px;
    line-height: 36px;
    vertical-align: center;
    transition: color .3s cubic-bezier(.4, 0, .2, 1);
    color: rgb(118, 124, 130);
    margin-left: 6px;

}

.self-form {
    margin-top: 20px;
}

.self-avaver {
    border: 1px solid #ddd;
    border-radius: 4px;
}
</style>