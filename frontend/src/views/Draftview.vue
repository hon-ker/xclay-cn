<template>
  <n-space vertical>
    <n-layout has-sider>
      <n-layout-sider bordered collapse-mode="width" :collapsed-width="0" :width="240" :collapsed="rightMenuActive"
        @collapse="rightMenuActive" @expand="rightMenuActive">
        <!-- tab -->
        <n-tabs class="left-tab" type="line" animated>

          <n-tab-pane name="文件" tab="文件">
            <n-list hoverable clickable>
              <n-list-item @click="getDraftInfo(item.id)" v-for="item of draft_list" :id="item.id"
                class="left-tab-files-item">
                <svg t="1698834541374" class="left-tab-file-icon icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="12785" width="200" height="200">
                  <path
                    d="M879.397794 62.605278H709.778763A91.333324 91.333324 0 0 0 621.748633 0.009744H402.251367a93.81072 93.81072 0 0 0-64.41229 25.104278 86.213373 86.213373 0 0 0-23.122361 37.656416H143.941567a66.063887 66.063887 0 0 0-66.063887 63.751651v833.5611A66.063887 66.063887 0 0 0 143.941567 1024h735.456227a66.063887 66.063887 0 0 0 66.063888-63.916811V126.522089a66.063887 66.063887 0 0 0-66.063888-63.916811z m-507.700975-1.321278A44.427964 44.427964 0 0 1 402.251367 49.55766h219.497266a40.298971 40.298971 0 0 1 42.280888 37.821576 35.674499 35.674499 0 0 1-11.72634 26.095235 44.427964 44.427964 0 0 1-30.554548 11.72634H402.251367a40.298971 40.298971 0 0 1-42.280888-37.821575 35.674499 35.674499 0 0 1 11.72634-26.095236z m524.877586 898.799189a16.515972 16.515972 0 0 1-16.515972 14.368895H143.941567a16.515972 16.515972 0 0 1-16.515972-14.368895V126.522089a16.515972 16.515972 0 0 1 16.515972-14.368896h170.27967a84.066297 84.066297 0 0 0 4.624472 11.396021l1.321278 2.477396a86.708852 86.708852 0 0 0 6.441229 10.405062l0.990958 1.321278a89.021088 89.021088 0 0 0 7.432187 8.753465l1.486438 1.486437a91.168165 91.168165 0 0 0 9.414104 7.927667l2.147076 1.486437A92.654602 92.654602 0 0 0 358.649201 165.169463h0.990959a93.480401 93.480401 0 0 0 11.39602 4.624472h2.312236a94.636519 94.636519 0 0 0 12.552139 2.972875h2.642555a96.122956 96.122956 0 0 0 13.708257 1.156118h219.497266a93.81072 93.81072 0 0 0 64.41229-25.104277 86.213373 86.213373 0 0 0 10.405063-11.8915l1.981916-2.807715a86.708852 86.708852 0 0 0 6.936708-12.386979v-1.816757c0.990958-2.477396 2.147076-5.119951 2.972875-7.762507h170.940309a16.515972 16.515972 0 0 1 16.515972 14.368896z"
                    fill="#0074FF" p-id="12786"></path>
                  <path
                    d="M272.270668 411.422604h353.606958a24.773958 24.773958 0 0 0 0-49.547916H272.270668a24.773958 24.773958 0 0 0 0 49.547916zM272.270668 574.270086h231.223606a24.773958 24.773958 0 0 0 0-49.547915h-231.223606a24.773958 24.773958 0 0 0 0 49.547915zM751.729332 687.404493h-478.963184a24.773958 24.773958 0 0 0 0 49.547916h478.963184a24.773958 24.773958 0 0 0 0-49.547916z"
                    fill="#0074FF" p-id="12787"></path>
                </svg>{{ item.title }}
              </n-list-item>
            </n-list>
            <!-- <n-menu :collapsed="collapsed = false" :collapsed-width="64" :collapsed-icon-size="22" :options="draft_list"
              :render-label="renderMenuLabel" :render-icon="renderMenuIcon" :expand-icon="expandIcon"
              :on-update:value="getDraftInfo" /> -->
          </n-tab-pane>
          <n-tab-pane @click="" name="目录" tab="目录">
            <MdCatalog :editorId="editorID" :scrollElement="scrollElement" />

          </n-tab-pane>
          <n-tab-pane @click="" name="模版" tab="模版">
            模版
          </n-tab-pane>
        </n-tabs>

      </n-layout-sider>
      <n-layout>
        <!-- 编辑器 -->
        <MdEditor :editorId="editorID" class="draft-editor" ref="editorRef" height="100vh" v-model="draft.content"
          :toolbars="toolbars">
          <template #defToolbars>
            <!-- toc 1-->
            <NormalToolbar title="打开目录" @onClick="tocActivate">
              <template #trigger>
                <div class="md-editor-icon">
                  <svg t="1698565029893" class="fix icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="4052" width="200" height="200">
                    <path
                      d="M725.333333 256c23.466667 0 42.666667 19.2 42.666667 42.666667v426.666666c0 23.466667-19.2 42.666667-42.666667 42.666667h-170.666666c-23.466667 0-42.666667-19.2-42.666667-42.666667V298.666667c0-23.466667 19.2-42.666667 42.666667-42.666667h170.666666z m64-74.666667H234.666667c-29.866667 0-53.333333 23.466667-53.333334 53.333334v554.666666c0 29.866667 23.466667 53.333333 53.333334 53.333334h554.666666c29.866667 0 53.333333-23.466667 53.333334-53.333334V234.666667c0-29.866667-23.466667-53.333333-53.333334-53.333334z m0-64c64 0 117.333333 53.333333 117.333334 117.333334v554.666666c0 64-53.333333 117.333333-117.333334 117.333334H234.666667c-64 0-117.333333-53.333333-117.333334-117.333334V234.666667C117.333333 170.666667 170.666667 117.333333 234.666667 117.333333h554.666666z"
                      p-id="4053"></path>
                  </svg>
                </div>
              </template>
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
            <NormalToolbar title="保存" @onClick="draftActivate">
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
      </n-layout>
    </n-layout>
  </n-space>


  <!-- 文章设置 -->
  <n-drawer class="editor-drawer" v-model:show="draftActive" :width="502" placement="left">
    <n-drawer-content title="文章设置">
      <n-form ref="formRef" :model="model" label-placement="left" label-width="auto"
        require-mark-placement="right-hanging" :size="size">
        <!-- 标题 -->
        <n-form-item label="标题" path="name">
          <n-input v-model:value="draft.title" clearable placeholder="文章标签" />
        </n-form-item>
        <pre>{{ JSON.stringify(draft, "", 2) }}</pre>

        <!-- 提交 -->
        <n-space>
          <!-- 新建按钮 -->
          <n-tooltip v-if="isNewDraft">
            <template #trigger>
              <n-button tag="div" @click="submitDraft">
                保存
              </n-button>
            </template>
            保存成新文件
          </n-tooltip>
          <!-- 更新按钮 -->
          <n-tooltip v-if="!isNewDraft">
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
          <img @click="insertImage(item.alt, item.src)" v-for="item in columnItems(index)" :key="item.id" :src="item.src"
            :alt="item.alt" :style="{ width: '100%' }" />
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
  border: none;
  height: calc(100vh - 0px);
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
import { h, ref, onMounted, onBeforeUnmount } from 'vue'
import { NList, NThing, NListItem, NCollapse, NCollapseItem, NTabs, NTabPane, NLayout, NMenu, NLayoutSider, useMessage, NGridItem, NImage, NTooltip, NIcon, NButtonGroup, NDivider, NForm, NFormItem, NFormItemGi, NGrid, NRadioGroup, NRadioButton, NRadio, NSpace, NInputNumber, NTimePicker, NSlider, NTransfer, NInput, NSelect, NDatePicker, NSwitch, NCheckbox, NCheckboxGroup, NButton, NDrawerContent, NDrawer, NDynamicTags, NUpload, NCard } from 'naive-ui';
import axios from 'axios';
import type { MenuOption } from 'naive-ui'
import { LogoFacebook, BookmarkOutline, CaretDownOutline, CashOutline as CashIcon } from '@vicons/ionicons5';

// ---------------------------------------------
// editor对象，及本地操作
// ---------------------------------------------
const BACKEND_URL = "http://127.0.0.1:8000";

const editorRef = ref<ExposeParam>();
const editorID = "draft-editor";
// 通知对象
const message = useMessage();
// 展示更新还是保存按钮
const isNewDraft = ref(false)

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
  localStorage.setItem("editorContent", draft.value.content);
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

// 获取草稿内容
function getDraftInfo(key) {
  axios
    .get(`${BACKEND_URL}/draft/` + key)
    .then(response => {
      draft.value.title = response.data.title;
      draft.value.content = response.data.content;
    })
    .catch(error => {
      message.error("获取失败")
    });
}

// 创建draft
function submitDraft() {
  axios.post(`${BACKEND_URL}/draft`, draft.value)
    .then(response => {
      draftActive.value = false;
      message.success(response.data.msg)
    })
    .catch(error => {
      // 请求失败后的处理逻辑
      draftActive.value = false;
      message.error("提交失败!")
    });
}

// 更新draft
function updateDraft() {
  axios.put(`${BACKEND_URL}draft/`, draft.value)
    .then(response => {
      draftActive.value = false;
      message.success(response.data.msg)
    })
    .catch(error => {
      // 请求失败后的处理逻辑
      draftActive.value = false;
      message.error("提交失败!")

    });
}

// left munu图标渲染
function renderMenuIcon(option: MenuOption) {
  // 渲染图标占位符以保持缩进
  if (option.key === 'sheep-man') return true
  // 返回 falsy 值，不再渲染图标及占位符
  if (option.key === 'food') return null
  return h(NIcon, null, { default: () => h(BookmarkOutline) })
}
// left munu图标渲染
function expandIcon() {
  return h(NIcon, null, { default: () => h(CaretDownOutline) })
}

// 锚点跳转
const scrollElement = document.documentElement;

// ---------------------------------------------
// active展示定义
// ---------------------------------------------

const draftActive = ref(false);
const emojiActive = ref(false);
const rightMenuActive = ref(false);

// 打开文章设置
const draftActivate = () => {
  draftActive.value = true;
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
const draft = ref({
  id: "",
  title: "",
  content: ""
})
// 左侧文件列表
const draft_list = ref([])
// 获取文章列表
function getDraftList() {
  axios.get(`${BACKEND_URL}/draft`)
    .then(response => {
      // 请求成功后的处理逻辑
      draft_list.value = response.data
    })
    .catch(error => {
      // 请求失败后的处理逻辑
      message.error("获取文件列表失败!")
    });
}

const getEmoji = () => {
  return ""
}


let images = ref([
  { src: getEmoji(), alt: 'image 1', id: 1 },
  { src: getEmoji(), alt: 'image 1', id: 2 },
  { src: getEmoji(), alt: 'image 1', id: 3 },
  { src: getEmoji(), alt: 'image 1', id: 4 },
  { src: getEmoji(), alt: 'image 1', id: 5 },
  { src: getEmoji(), alt: 'image 1', id: 6 },
  { src: getEmoji(), alt: 'image 1', id: 7 },
  { src: getEmoji(), alt: 'image 1', id: 8 },
  { src: getEmoji(), alt: 'image 1', id: 9 },
  { src: getEmoji(), alt: 'image 1', id: 10 },
  // 更多图片
])

const columnItems = (index) => {
  return images.value.filter((_, i) => i % 3 === index)
}






// --------------------------------------------
// 起始调用
// --------------------------------------------

const init = () => {
  // 获取草稿列表
  getDraftList();
  // 初始化编辑器内容为上次缓存内容
  draft.value.content = localStorage.getItem("editorContent") ? localStorage.getItem("editorContent") : ""
}

onMounted(init)

// --------------------------------------------
// 收尾工作
// --------------------------------------------

// 突发关闭或者跳转到其他网页自动保存
window.addEventListener('beforeunload', function (event) {
  // 你需要保存的数据
  localStorage.setItem("editorContent", draft.value.content);
});


// --------------------------------------------
// 测试
// --------------------------------------------

import { reactive } from 'vue';
import { MdPreview, MdCatalog } from 'md-editor-v3';
import 'md-editor-v3/lib/preview.css';

</script>