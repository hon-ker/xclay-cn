<template>
    <link href="https://fastly.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <div class="head-title">
        <h4>假欢</h4>
    </div>
    <div class="head-action">
        <div class="toggle-btn"></div>
        <div class="light-btn"></div>
        <div @click="showInput" class="search-btn"></div>
    </div>
    <form class="head-search" :class="{ active: searchActive }" method="post">
        <input @input="handleInputChange" v-model="inputValue" type="text" name="s" placeholder="搜索什么？">
    </form>
    <nav class="head-menu">
        <n-dropdown trigger="hover" :options="category" :show-arrow="true" @select="">
            <a href="javascript:void(0)">分类</a>
        </n-dropdown>
        <a href="/">首页</a>
        <n-dropdown trigger="hover" :options="options" :show-arrow="true" @select="">
            <a href="javascript:void(0)">更多</a>
        </n-dropdown>

    </nav>
</template>

<script setup>
import { NText, NAvatar, NIcon, NInput, NSpace, NButton, NDropdown, NTooltip, NPopover } from 'naive-ui'
import { LogOutOutline, FlashOutline } from '@vicons/ionicons5'
import { onMounted, ref } from 'vue';

// 搜索
const searchActive = ref(false);
// 主题切换
const inputValue = ref('');

function showInput() {
    searchActive.value = !searchActive.value;
}

function handleInputChange() {
    if (inputValue.value.length > 0) {
        console.log(inputValue.value);
        // 搜索接口
    }
}

const category = ref([
    {
        label: '技术',
        key: 'jishu'
    },
    {
        label: '复现',
        key: 'cover'
    },

])

const options = [
    {
        label: '滨海湾金沙，新加坡',
        key: 'marina bay sands',
    },
    {
        label: '布朗酒店，伦敦',
        key: "brown's hotel, london"
    },
    {
        label: '亚特兰蒂斯巴哈马，拿骚',
        key: 'atlantis nahamas, nassau'
    },
    {
        label: '比佛利山庄酒店，洛杉矶',
        key: 'the beverly hills hotel, los angeles'
    }
]

</script>