<template>
    <MdEditor :style="{ height: boxHeight + 'px' }" :editorId="editorID" class="post-editor" ref="editorRef" height="100vh"
        v-model="post.content" :toolbars="toolbars" @onUploadImg="onUploadImg">
        <template #defToolbars>
            <!-- toc 1-->
            <NormalToolbar title="打开目录" @onClick="tocActivate">

            </NormalToolbar>
            <!-- 表情包 3-->

            <NormalToolbar title="打开表情包" @onClick="emojiActivate">
                <template #trigger>
                    <div class="md-editor-icon">
                        <svg t="1698565533584" class="fix icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="26035" width="18" height="18">
                            <path
                                d="M896.991286 342.869511a449.338411 449.338411 0 1 1-772.027541 3.426857C75.070808 283.667603 58.986901 248.171404 58.986901 154.602454 58.986901 100.028773 87.872285 52.341629 112.359213 7.359208a300.401431 300.401431 0 0 0 118.561373 216.640382 448.767268 448.767268 0 0 1 558.735239-2.625944A301.609365 301.609365 0 0 0 912.484356-0.01313C936.511744 44.969291 964.937588 92.64987 964.937588 147.230116c0 95.479325-16.543447 130.568501-67.946302 195.639395zM108.74854 574.563116A403.213704 403.213704 0 1 0 511.962245 171.22468 403.279353 403.279353 0 0 0 108.74854 574.563116z m557.881807-147.354848h81.010373v81.043197H666.630347V427.208268z m-151.779564 256.830454a127.601185 127.601185 0 0 1-123.813261-103.724788h31.970869a97.317485 97.317485 0 0 0 188.017592 0h27.63806a127.653704 127.653704 0 0 1-123.81326 103.724788zM268.931126 427.208268h81.010373v81.043197H268.931126V427.208268z"
                                fill="" p-id="26036"></path>
                        </svg>
                    </div>
                </template>
            </NormalToolbar>
            <!-- 浏览器缓存 5-->
            <NormalToolbar title="缓存到本地" @onClick="saveCache">
                <template #trigger>
                    <div class="md-editor-icon">
                        <svg t="1698569398703" class="fix icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="31757" width="18" height="18">
                            <path
                                d="M201.315556 987.093333a32.611556 32.611556 0 0 1-27.235556-14.136889c-11.079111-16.056889-4.551111-35.854222-1.536-43.946666l92.629333-342.727111a28.16 28.16 0 0 1 0.896-2.744889 7.338667 7.338667 0 0 0 0.327111-0.995556h-56.078222c-21.162667 0-38.613333-9.002667-47.843555-24.689778-9.315556-15.829333-8.661333-35.726222 1.777777-54.556444l230.286223-414.72c16.284444-29.425778 53.745778-51.655111 87.139555-51.655111h334.833778c22.172444 0 39.424 9.344 47.345778 25.671111 7.964444 16.398222 4.551111 35.925333-9.329778 53.575111L616.661333 419.427556h101.575111c33.450667 0 43.818667 18.602667 46.72 26.581333 2.887111 7.964444 6.840889 28.686222-18.304 50.147555L236.131556 971.150222c-0.341333 0.327111-0.711111 0.668444-1.080889 0.967111-12.16 10.197333-22.883556 14.976-33.735111 14.976z m118.428444-384.725333l-77.013333 284.942222 441.742222-410.993778h-84.536889c-22.172444 0-39.424-9.344-47.345778-25.642666-7.978667-16.398222-4.565333-35.939556 9.315556-53.617778L799.758222 93.809778H481.678222c-12.629333 0-31.146667 11.064889-37.390222 22.328889L216.888889 525.639111h49.066667c20.352 0 37.987556 8.661333 48.369777 23.779556 10.225778 14.862222 12.174222 34.090667 5.418667 52.949333z"
                                fill="" p-id="31758"></path>
                            <path
                                d="M376.675556 376.988444a14.222222 14.222222 0 0 1-12.416-21.12l12.743111-22.954666a14.208 14.208 0 1 1 24.860444 13.795555l-12.743111 22.954667a14.222222 14.222222 0 0 1-12.444444 7.324444z m40.149333-72.32a14.222222 14.222222 0 0 1-12.416-21.12l60.216889-108.444444c12.330667-22.272 41.756444-39.751111 67.000889-39.751111h37.191111a14.222222 14.222222 0 1 1 0 28.444444H531.626667c-15.061333 0-34.730667 11.719111-42.140445 25.102223l-60.216889 108.458666a14.222222 14.222222 0 0 1-12.444444 7.310222z"
                                fill="" p-id="31759"></path>
                        </svg>
                    </div>
                </template>
            </NormalToolbar>
            <!-- 保存 7-->
            <NormalToolbar title="保存" @onClick="postActivate">
                <template #trigger>
                    <div class="md-editor-icon">
                        <svg t="1698565678127" class="fix icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="29624" width="18" height="18">
                            <path
                                d="M810.666667 469.333333l0 336.981333c0 1.109333-0.896 2.901333-1.792 4.352L214.869333 810.666667C214.058667 809.258667 213.418667 807.594667 213.333333 806.613333L213.333333 256l298.666667 0L512 170.666667 128 170.666667l0 72.490667 0 563.498667L128 896l768 0 0-89.386667L896 469.333333 810.666667 469.333333z"
                                fill="#333333" p-id="29625"></path>
                            <path
                                d="M349.269333 457.002667 285.397333 513.664 485.845333 739.541333 843.008 323.797333 778.325333 268.202667 484.821333 609.792Z"
                                fill="#333333" p-id="29626"></path>
                        </svg>
                    </div>
                </template>
            </NormalToolbar>
            <!-- 链接 9-->
            <NormalToolbar title="保存" @onClick="insetLink">
                <template #trigger>
                    <div class="md-editor-icon">
                        <svg t="1698572617786" class="fix icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="5958" width="20" height="20">
                            <path
                                d="M647.765333 204.032a170.666667 170.666667 0 0 1 247.808 234.581333l-6.4 6.826667L512 822.485333a234.666667 234.666667 0 0 1-339.285333-324.096l7.424-7.765333 316.8-316.8a42.666667 42.666667 0 0 1 63.872 56.32l-3.541334 4.053333-316.8 316.757334a149.333333 149.333333 0 0 0 204.8 217.216l6.4-6.016 377.130667-377.130667a85.333333 85.333333 0 0 0-115.242667-125.653333l-5.418666 4.992-377.173334 377.088a21.333333 21.333333 0 0 0 27.264 32.64l2.944-2.432 316.8-316.8a42.666667 42.666667 0 0 1 63.872 56.32l-3.541333 4.010666-316.8 316.8a106.666667 106.666667 0 0 1-156.032-145.28l5.205333-5.546666 377.088-377.173334z"
                                fill="#000000" p-id="5959"></path>
                        </svg>
                    </div>
                </template>
            </NormalToolbar>
        </template>
    </MdEditor>

    <!-- 文章设置 -->
    <n-drawer class="editor-drawer" v-model:show="postActive" :width="502" placement="left">
        <n-drawer-content title="文章设置">
            <n-form ref="formRef">
                <!-- 标题 -->
                <n-form-item label="标题" path="name">
                    <n-input v-model:value="post.title" clearable placeholder="文章标签" />
                </n-form-item>
                <!-- 摘要 -->
                <n-form-item label="摘要" path="textareaValue">
                    <n-input v-model:value="post.des" placeholder="对文章的摘要" type="textarea" :autosize="{
                        minRows: 3,
                        maxRows: 5
                    }" />
                </n-form-item>

                <!-- 分类 -->
                <n-form-item label="分类" path="name">
                    <n-select placeholder="请选择分类" v-model:value="post.category" filterable tag
                        :options="categoryOptions" />
                </n-form-item>

                <!-- 标签 -->
                <n-form-item label="标签" path="name">
                    <n-select placeholder="请选择标签，最多三个" v-model:value="post.tag" filterable multiple tag
                        :options="tagOptions" />
                </n-form-item>

                <pre>{{ JSON.stringify(post, "", 2) }}</pre>

                <!-- 提交 -->
                <n-space>
                    <!-- 新建按钮 -->
                    <n-tooltip v-if="!isNewPost">
                        <template #trigger>
                            <n-button tag="div" @click="submitDraft">
                                保存
                            </n-button>
                        </template>
                        保存成新文件
                    </n-tooltip>
                    <!-- 更新按钮 -->
                    <n-tooltip v-if="isNewPost">
                        <template #trigger>
                            <n-button tag="div" @click="updateDraft">
                                更新
                            </n-button>
                        </template>
                        更新草稿
                    </n-tooltip>
                </n-space>

            </n-form>
        </n-drawer-content>
    </n-drawer>

    <!-- 表情包 -->
    <n-drawer class="editor-drawer" v-model:show="emojiActive" :width="502" placement="left">
        <n-drawer-content title="表情包">
            <div class="masonry">
                <div class="column" v-for="(column, index) in 3" :key="index">
                    <img @click="insertImage(item.alt, item.src)" v-for="item in columnItems(index)" :key="item.id"
                        :src="item.src" :alt="item.alt" :style="{ width: '100%' }" />
                </div>
            </div>
        </n-drawer-content>
    </n-drawer>
</template>
  
<style>
.md-editor-toolbar-wrapper {
    padding: 6px;
}

.left-tab .v-x-scroll {
    padding: 0 10px;
    border-bottom: none;
}

.fa-file {
    padding-right: 6px;
}

.left-tab .n-tabs-tab-pad {
    width: auto;
    padding-right: 20px;
}


.left-tab .v-x-scroll .n-tabs-nav-scroll-content .n-tabs-bar {
    height: 3px !important;
}

.n-tab-pane {
    margin-top: 0 !important;
}

.left-tab-files-item {
    padding: 0 10px !important;
    margin-top: 0px;
}

.left-tab-file-icon {
    width: 20px;
    height: 20px;
    padding-right: 5px;
    top: -2px;
    position: relative;
}

.cm-content {
    line-height: 1.8em;
    font-size: 16px;
}

.has-preview .cm-scroller {
    overflow-y: auto !important;
    border-right: 1px solid #ddd;
}

.md-editor {
    /* border: 1px solid ; */
    border-radius: 4px;
    height: calc(100vh - 30px);
}

.md-editor-icon .fix {
    width: 18px;
    height: 18px;
    top: -3px;
    position: relative;
}

.n-input.n-input--autosize .n-input__textarea-el,
.n-input.n-input--autosize .n-input__input-el {
    position: absolute;
    top: -4px !important;
    left: 0;
    height: 100%;
}

.n-button__icon .n-base-icon {
    top: -2px;
}

.n-tag--closable .n-base-icon {
    top: -2px;
}

@media screen and (max-width: 900px) {
    .editor-drawer {
        width: calc(100vw / 5 * 3) !important;
    }
}

@media screen and (min-width: 900px) {
    .editor-drawer {
        width: calc(100vw / 5 * 2) !important;
    }
}


.upload-area {
    width: 200px;
    height: 200px;
    border: 1px dashed #999;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    padding: 10px 20px;
}

.upload-area img {
    max-width: 100%;
    max-height: 100%;
}

.masonry {
    display: flex;
    justify-content: space-between;
}

.column {
    flex: 1;
    margin-bottom: 6px;
    padding: 3px;
    border-radius: 4px;

}

.column img {
    border-radius: 4px;
    margin-bottom: 6px;
    border: 1px solid #eaeaea;
    padding: 3px;
}

form pre {
    margin-bottom: 20px;
}
</style>
  
<script setup lang="ts">
import { MdEditor, NormalToolbar, ExposeParam } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import { h, toRef, ref, onMounted, onBeforeUnmount } from 'vue'
import { NList, NThing, NListItem, NCollapse, NCollapseItem, NTabs, NTabPane, NLayout, NMenu, NLayoutSider, useMessage, NGridItem, NImage, NTooltip, NIcon, NButtonGroup, NDivider, NForm, NFormItem, NFormItemGi, NGrid, NRadioGroup, NRadioButton, NRadio, NSpace, NInputNumber, NTimePicker, NSlider, NTransfer, NInput, NSelect, NDatePicker, NSwitch, NCheckbox, NCheckboxGroup, NButton, NDrawerContent, NDrawer, NDynamicTags, NUpload, NCard } from 'naive-ui';
import axios from 'axios';

// 从父组件接收的参数

const props = defineProps({
    // post文章数据
    post: {
        type: Object,
        default: null

    },
    isNewPost: {
        type: Boolean,
        default: false
    }
});
// ---------------------------------------------
// editor对象，及本地操作
// ---------------------------------------------
const BACKEND_URL = "http://127.0.0.1:8000/api/admin";

const editorRef = ref<ExposeParam>();
const editorID = "-editor";
// 通知对象
const message = useMessage();
// 展示更新还是保存按钮

// 编辑器toolbars
const toolbars = [
    "1",
    'revoke',
    'next',
    '-',
    'codeRow',
    'code',
    'quote',
    "9",
    'image',
    'table',
    "3",
    'task',
    'unorderedList',
    'orderedList',
    'mermaid',
    'katex',
    '-',
    // 'bold',
    // 'underline',
    // 'italic',
    // 'title',
    // 'strikeThrough',
    // 'sub',
    // 'sup',
    // '-',
    "5",
    "7",
    '=',
    'pageFullscreen',
    'fullscreen',
    'preview',
    'htmlPreview',
];

// 编辑器本地浏览器缓存
function saveCache() {
    localStorage.setItem("editorContent", post.value.content);
    message.success("缓存成功!")
}
// 编辑器插入link
const insetLink = () => {
    editorRef.value?.insert((selected) => {
        /**
         * @return targetValue    待插入内容
         * @return select         插入后是否自动选中内容
         * @return deviationStart 插入后选中内容鼠标开始位置
         * @return deviationEnd   插入后选中内容鼠标结束位置
         */
        return {
            targetValue: ` [${selected}](https://${selected})`,
            select: true,
            deviationStart: 0,
            deviationEnd: 0
        };
    });
};

// 编辑器插入表情包
function insertImage(alt, src) {
    editorRef.value?.insert(() => {
        /**
         * @return targetValue    待插入内容
         * @return select         插入后是否自动选中内容
         * @return deviationStart 插入后选中内容鼠标开始位置
         * @return deviationEnd   插入后选中内容鼠标结束位置
         */
        return {
            targetValue: `   \n![${alt}](${src})   \n`,
            select: false,
            deviationStart: 0,
            deviationEnd: 0
        };
    });
    message.success("插入成功!")
    emojiActive.value = false
}

// 编辑器上传图片
const onUploadImg = async (files, callback) => {
  const res = await Promise.all(
    files.map((file) => {
      return new Promise((rev, rej) => {
        const form = new FormData();
        form.append('file', file);

        axios
          .post('http://127.0.0.1:8000/img/upload', form, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then((response) => rev(response))
          .catch((error) => rej(error));
      });
    })
  );

  callback(res.map((item) => "http://127.0.0.1:8000"+item.data.url));
};

// 获取草稿内容
function getDraftInfo(key) {
    axios
        .get(`${BACKEND_URL}/post/` + key)
        .then(response => {
            post.value.title = response.data.title;
            post.value.content = response.data.content;
        })
        .catch(error => {
            message.error("获取失败")
        });
}


// 创建post
function submitDraft() {
    axios.post(`${BACKEND_URL}/post`, post.value)
        .then(response => {
            postActive.value = false;
            message.success(response.data.msg)
        })
        .catch(error => {
            // 请求失败后的处理逻辑
            postActive.value = false;
            message.error("提交失败!")
        });
}

// 更新post
function updateDraft() {
    axios.put(`${BACKEND_URL}/post/`, post.value)
        .then(response => {
            postActive.value = false;
            message.success(response.data.msg)
        })
        .catch(error => {
            // 请求失败后的处理逻辑
            postActive.value = false;
            message.error("提交失败!")

        });
}


// ---------------------------------------------
// active展示定义
// ---------------------------------------------

const postActive = ref(false);
const emojiActive = ref(false);
const rightMenuActive = ref(false);

// 打开文章设置
const postActivate = () => {
    postActive.value = true;
}
// 打开emoji
const emojiActivate = () => {
    emojiActive.value = true;
}

const tocActivate = () => {
    rightMenuActive.value = !rightMenuActive.value;
}

// ---------------------------------------------
// 需要从后端获取的数据
// ---------------------------------------------
const post = toRef(props, 'post');

if (post.value === null) {
    post.value = ref({
        id: "",
        title: "",
        des: "",
        content: Boolean(localStorage.getItem("editorContent")) ? localStorage.getItem("editorContent") : "",
        category: "默认",
        tag: [],
        user: "xclay"
    });

}



// 分类
const categoryOptions = ref()
function getCategory() {
    axios.get(`${BACKEND_URL}/category/all`).then(response => {

        categoryOptions.value = response.data.map(item => ({
            value: item.name,
            label: item.name,
            key: item.id
        })
        )
    }
    ).catch(error => {
        // message.error(`加载分类时出错：${error}`);
    })

}

// 标签
const tagOptions = ref()
function getTag() {
    axios.get(`${BACKEND_URL}/tag/all`).then(response => {

        tagOptions.value = response.data.map(item => ({
            value: item.name,
            label: item.name,
            key: item.id
        })
        )
    }
    ).catch(error => {
        // message.error(`加载标签时出错：${error}`);
    })
}

let images = ref([])
const getEmoji = async () => {
    const data = [];
    let counter = 0;

    const fetchEmoji = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/other/gif');
            const img = {
                src: "http://127.0.0.1:8000" + response.data.url,
                alt: "",
                id: counter++,
            };
            data.push(img);
        } catch (error) {
            console.error(error);
        }
    };

    const promises = [];
    for (let i = 0; i < 10; i++) {
        promises.push(fetchEmoji());
    }

    await Promise.all(promises);
    images.value = data
    // console.log(images.value);
};

const columnItems = (index) => {
    return images.value.filter((_, i) => i % 3 === index)
}

// --------------------------------------------
// 起始调用
// --------------------------------------------

const init = () => {
    // 获取草稿列表
    // getDraftList();
    // 初始化编辑器内容为上次缓存内容
    getCategory()
    getTag()
    getEmoji()

}

onMounted(init)

// --------------------------------------------
// 收尾工作
// --------------------------------------------

// 突发关闭或者跳转到其他网页自动保存
window.addEventListener('beforeunload', function (event) {
    // 你需要保存的数据
    localStorage.setItem("editorContent", post.value.content);
});


// --------------------------------------------
// 测试
// --------------------------------------------

</script>