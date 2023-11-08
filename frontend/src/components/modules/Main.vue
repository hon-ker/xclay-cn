<template>
    <div class="wrap min">
        <section class="home-title">
            <h1>假欢</h1>
            <span>to be a monster.</span>
            <div class="home-social">
                <a rel="nofollow" title="新浪微博" href="http://weibo.com/234891753" target="_blank">
                    <i class="fa fa-weibo"></i>
                </a>
                <a rel="nofollow" title="企鹅群" href="https://jq.qq.com/?_wv=1027&amp;k=5uY9V3K" target="_blank">
                    <i class="fa fa-qq"></i>
                </a>
                <a rel="nofollow" title="GitHub" href="https://github.com/Dreamer-Paul" target="_blank">
                    <i class="fa fa-github"></i>
                </a>
                <a rel="nofollow" title="Steam" href="http://steamcommunity.com/id/dreamer-paul" target="_blank">
                    <i class="fa fa-steam"></i>
                </a>
                <a rel="nofollow" title="首页" href="https://paul.ren" target="_blank">
                    <i class="fa fa-home"></i>
                </a>
            </div>
        </section>
        <div class="features"><!--[-->
            <div class="feature">
                <h2>Blog</h2>
                <p>极致简约为上，如果有天我一周没更新了那一定是我偷懒了，请叫醒我</p>
            </div>
            <div class="feature">
                <h2>CVE 列表</h2>
                <p>每日 scss 评分 9.0 以上漏洞数据库，包含接口数据和详细官方文档 </p>
            </div>
            <div class="feature">
                <h2>EXP和POC库</h2>
                <p>学习的未学习的，往上的，尽可能去收集更多的已经披露的漏洞EXP和POC</p>
            </div>
            <div class="feature">
                <h2>主题</h2>
                <p>提供了一个开箱即用的默认主题。你也可以挑选一个社区主题，或者创建一个你自己的主题。</p>
            </div>
            <div class="feature">
                <h2>插件</h2>
                <p>灵活的插件API，使得插件可以为你的站点提供许多即插即用的功能。</p>
            </div>
            <div class="feature">
                <h2>打包工具</h2>
                <p>默认的打包工具是 Vite ，也同样支持 Webpack 。选一个你喜欢的来使用吧！</p>
            </div><!--]-->
        </div>

        <pre id="style-text">
/**
* Hey. My name's clay X. A handsome boy
* I build interactive websites.
* How about some live coding?
*/<img class="dragon" :src="gif" alt="">
</pre>
        
        <section class="posts">
            <div v-for="x of post" :key="x.id" class="magic-card post-item-container">
                <span class="magic-card__bg"></span>
                <div class="title"><a :href="'/post/' + x.title" class="">{{ x.title }}</a></div>
                <div class="des">
                    支持实时预览、图片（跨域）上传、预格式文本/代码/表格插入、代码折叠、搜索替换、只读模式、自定义样式主题和多语言语法高亮等功能；支持实时预览、图片（跨域）上传、预格式文本/代码/表格插入、代码折叠、搜索替换、只读模式、自定义样式主题和多语言语法高亮等功能；
                </div>
                <div class="page-info">
                    <span class="xicon-container left">
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                            viewBox="0 0 32 32" class="xicon-icon"
                            style="width: 18px; height: 18px; font-size: 18px; color: inherit;">
                            <path d="M16 4a5 5 0 1 1-5 5a5 5 0 0 1 5-5m0-2a7 7 0 1 0 7 7a7 7 0 0 0-7-7z"
                                fill="currentColor"></path>
                            <path d="M26 30h-2v-5a5 5 0 0 0-5-5h-6a5 5 0 0 0-5 5v5H6v-5a7 7 0 0 1 7-7h6a7 7 0 0 1 7 7z"
                                fill="currentColor"></path>
                        </svg> <span class="xicon-content" style="color: inherit; font-size: 14px;">{{ x.user }}</span>
                    </span>
                    <span class="xicon-container left">
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                            viewBox="0 0 32 32" class="xicon-icon"
                            style="width: 18px; height: 18px; font-size: 18px; color: inherit;">
                            <path
                                d="M26 4h-4V2h-2v2h-8V2h-2v2H6c-1.1 0-2 .9-2 2v20c0 1.1.9 2 2 2h20c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 22H6V12h20v14zm0-16H6V6h4v2h2V6h8v2h2V6h4v4z"
                                fill="currentColor"></path>
                        </svg> <span class="xicon-content" style="color: inherit; font-size: 14px;">{{ x.ctime }}</span>
                    </span>
                    <span class="xicon-container left">
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                            viewBox="0 0 32 32" class="xicon-icon"
                            style="width: 18px; height: 18px; font-size: 18px; color: inherit;">
                            <path
                                d="M11.17 6l3.42 3.41l.58.59H28v16H4V6h7.17m0-2H4a2 2 0 0 0-2 2v20a2 2 0 0 0 2 2h24a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2H16l-3.41-3.41A2 2 0 0 0 11.17 4z"
                                fill="currentColor"></path>
                        </svg> <span class="xicon-content" style="color: inherit; font-size: 14px;">{{ x.category }}</span>
                    </span>
                    <span class="xicon-container left">
                        <svg t="1698385162529" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="12482" width="200" height="200">
                            <path
                                d="M512 863.008l384-54.016V169.984L525.984 222.976q-14.016 2.016-28 0L127.968 169.984v639.008zM136.992 106.016l370.016 52.992q4.992 0.992 10.016 0L887.04 106.016q28.992-3.008 50.496 16t22.496 48v639.008q0 24-15.488 41.504t-39.488 21.504L517.056 927.04q-4.992 0.992-10.016 0L119.04 872.032q-24-4-39.488-21.504t-15.488-41.504V170.016q0.992-28.992 22.496-48t50.496-16zM480 192h64v704h-64V192z"
                                p-id="12483"></path>
                        </svg>
                        <span class="xicon-content">{{ x.view }}</span>
                    </span>
                </div>
            </div>
        </section>
    </div>
</template>
  
<style scoped>
#style-text {
    margin-bottom: 1.2rem;
    position: relative;
    overflow: visible;
    text-wrap: wrap;
}

#style-text .dragon {
    position: absolute;
    bottom: 6px;
    right: 30px;
}

@media (max-width: 450px) {
    .features {
        flex-direction: column;

    }

    #style-text .dragon {
        display: none;
    }
}

.code-block_root__mzqyn>div {
    border-color: var(--guide-color);
}

.code-block_header__t3NRd {
    padding: 0 12px 0 16px;
    border-radius: 6px 6px 0 0;
    /* border-bottom: 1px solid #eee; */
    display: flex;
    height: 48px;
    align-items: center;
    background: #fff;
}

.code-block_fileName__HmSv1 {
    color: var(--ds-gray-900);
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    min-width: 0;
    margin: 0 auto 0 0;
}

.code-block_actions__yphRf {
    display: flex;
    gap: 4px;
}

.code-block_copyButton__uo5Yu {
    height: 32px;
    width: 32px;
    border-radius: 4px;
    border: none;
    /* color: var(--ds-gray-900); */
    cursor: pointer;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: inherit;
    position: relative;
    transition: background .2s ease;
}

.code-block_copyButton__uo5Yu svg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.code-block_copyButton__uo5Yu svg:nth-child(2) {
    opacity: 0;
    transform: translate(-50%, -50%) scale(.5);
}

.code-block_copyButton__uo5Yu svg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

@keyframes code-block_hide__enoxr {
    0% {
        opacity: 1;
        transform: translate(-50%, -50%)
    }

    20% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(.5)
    }

    80% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(.5)
    }

    to {
        opacity: 1;
        transform: translate(-50%, -50%)
    }
}

.code-block_copyButton__uo5Yu.code-block_copyButtonCopied__fMOZ5 svg {
    animation: code-block_hide__enoxr 1.25s forwards;
}



@media (hover: hover) {
    .code-block_copyButton__uo5Yu:hover:not([data-active]) {
        background: hsla(0, 0%, 92%, 1) !important;
        color: hsla(0, 0%, 40%, 1) !important;
    }
}

.code-block_pre___OLfy {
    font-size: 14px;
    background-color: #fff;
    padding: 10px 15px;
}



@media (max-width: 719px) {
    .features {
        /* flex-direction: column; */
        padding: 1.2rem 0;

    }

    .features .feature {
        flex-grow: 1;
        flex-basis: 50%;
        max-width: 48%;
    }
}

@media (max-width: 450px) {
    .features {
        flex-direction: column;

    }

    .features .feature {
        flex-grow: 1;
        flex-basis: 100%;
        max-width: 100%;
    }
}

@media (min-width: 719px) {
    .features {
        /* flex-direction: column; */
        padding: 1.2rem 0;

    }

    .features .feature {
        flex-grow: 1;
        flex-basis: 30%;
        max-width: 30%;
    }



}


.features {
    border-top: 1px solid var(--c-border);
    transition: border-color var(--t-color);
    padding: 1.2rem 0;
    margin-top: 2.5rem;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    align-content: stretch;
    justify-content: space-between;
    border-top: 1px solid #eaecef;
}

.feature h2 {
    font-size: 1.4rem;
    font-weight: 500;
    border-bottom: none;
    padding-bottom: 0;
    color: #3a5169;
    margin: 18px 0;
}

.feature p {
    color: #4e6e8e;
    font-size: 14px;
    margin: 16px 0;
}

p,
ul,
ol {
    line-height: 1.7;
    overflow-wrap: break-word;
}

h2 {
    font-size: 1.65rem;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid var(--c-border);
    transition: border-color var(--t-color);
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-weight: 600;
    line-height: 1.25;
    overflow-wrap: break-word;
}
</style>
<script setup>

import { NDivider } from 'naive-ui';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const post = ref({})
const isActive = ref(false)
function toggleActive() {
    isActive.value = !isActive.value
}

const gif = ref()

function fetchPostData() {
    // 使用 axios 发送 API 请求获取数据
    axios.get('http://127.0.0.1:8000/other/gif')
        .then(response => {
            // 成功获取数据，将数据保存到组件的变量中
            gif.value = "http://127.0.0.1:8000" + response.data.url;
            console.log(gif.value);
        })
        .catch(error => {
            // 处理错误
            console.error(error);
        });
}



// 在组件加载完成后调用 fetchPostData
onMounted(fetchPostData);

</script>