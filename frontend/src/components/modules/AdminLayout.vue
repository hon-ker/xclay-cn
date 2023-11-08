<template>
    <div class="admin-header">
        <div class="left">
            <svg @click="toggleActive" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                viewBox="0 0 24 24">
                <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 6h16"></path>
                    <path d="M4 12h16"></path>
                    <path d="M4 18h16"></path>
                </g>
            </svg>
        </div>
        <div class="nav">
            <a href="">1213</a>
        </div>

    </div>
    <div class="admin-main">
        <n-layout has-sider>
            <n-layout-sider @dblclick="toggleActive" bordered collapse-mode="width" :collapsed="collapsed" icon-size="24"
                collapsed-icon-size="24" @collapse="collapsed" @expand="collapsed">
                <n-menu :options="menuOptions" key="whateverKey" key-field="whateverKey" label-field="whateverLabel" @on-update:value="handleMenuUpdate" />
            </n-layout-sider>
            <slot name="main"></slot>
            <n-layout />
        </n-layout>
    </div>
</template>

<script setup>
import { defineComponent, h, ref } from "vue";
import { NMessageProvider, useMessage, NButton, NSwitch, NIcon, NMenu, NLayout, NLayoutSider } from "naive-ui";
import {
    HomeOutline as HomeIcon,
    BookOutline as BookIcon,
    PersonOutline as PersonIcon,
    WineOutline as WineIcon,
} from "@vicons/ionicons5";

const collapsed = ref(true);

function renderIcon(icon) {
    return () => h(NIcon, null, { default: () => h(icon) });
}

function toggleActive() {
    collapsed.value = !collapsed.value;
}

const menuOptions = ref([
    {
        whateverLabel: "编辑器",
        whateverKey: "hear-the-wind-sing",
        icon: renderIcon(BookIcon)
    },
    {
        whateverLabel: "文章管理",
        whateverKey: "pinball-1973",
        icon: renderIcon(BookIcon),
    },
    {
        whateverLabel: "标签列表",
        whateverKey: "a-wild-sheep-chase",
        icon: renderIcon(BookIcon)
    },
    {
        whateverLabel: "分类列表",
        whateverKey: "dance-dance-dance",
        icon: renderIcon(BookIcon),
    }
]);

function handleMenuUpdate(key, item) {
    console.log("选中菜单项的键:", 121);
    console.log("菜单项的原始数据:", item);
    // 在这里可以根据需要处理选中菜单项的操作
}

</script>

<style>
.admin-header {
    height: 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px;
    background-color: #fff;
    border: 1px solid #e8e8e8;

}

.admin-header .left svg {
    width: 24px;
    height: 24px;
}
</style>
    