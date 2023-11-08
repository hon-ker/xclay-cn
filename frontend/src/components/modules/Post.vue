<template>
    <div class="wrap min">

        <section class="post-title">
            <h2>{{ post.title }}</h2>

            <div class="page-info"><span class="xicon-container left">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32"
                        class="xicon-icon" style="width: 18px; height: 18px; font-size: 18px; color: inherit;">
                        <path d="M16 4a5 5 0 1 1-5 5a5 5 0 0 1 5-5m0-2a7 7 0 1 0 7 7a7 7 0 0 0-7-7z" fill="currentColor">
                        </path>
                        <path d="M26 30h-2v-5a5 5 0 0 0-5-5h-6a5 5 0 0 0-5 5v5H6v-5a7 7 0 0 1 7-7h6a7 7 0 0 1 7 7z"
                            fill="currentColor"></path>
                    </svg> <span class="xicon-content">{{ post.user }}</span></span>
                <span class="xicon-container left">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32"
                        class="xicon-icon" style="width: 18px; height: 18px; font-size: 18px; color: inherit;">
                        <path
                            d="M11.17 6l3.42 3.41l.58.59H28v16H4V6h7.17m0-2H4a2 2 0 0 0-2 2v20a2 2 0 0 0 2 2h24a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2H16l-3.41-3.41A2 2 0 0 0 11.17 4z"
                            fill="currentColor"></path>
                    </svg>
                    <span class="xicon-content">{{ post.category }}</span></span>
                <span class="xicon-container left">
                    <svg t="1698385162529" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="12482" width="200" height="200">
                        <path
                            d="M512 863.008l384-54.016V169.984L525.984 222.976q-14.016 2.016-28 0L127.968 169.984v639.008zM136.992 106.016l370.016 52.992q4.992 0.992 10.016 0L887.04 106.016q28.992-3.008 50.496 16t22.496 48v639.008q0 24-15.488 41.504t-39.488 21.504L517.056 927.04q-4.992 0.992-10.016 0L119.04 872.032q-24-4-39.488-21.504t-15.488-41.504V170.016q0.992-28.992 22.496-48t50.496-16zM480 192h64v704h-64V192z"
                            p-id="12483"></path>
                    </svg>
                    <span class="xicon-content">{{ post.view }}</span>
                </span>
                <span class="xicon-container left">

                    <svg t="1698385195661" class="icon" viewBox="0 0 1024 1024" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" p-id="13562" width="200" height="200">
                        <path
                            d="M954.514 402.113c-7.724-22.304-27.494-38.582-51.328-42.155l-231.982-34.509L570.327 116.055c-10.595-22.01-33.307-36.087-58.312-36.087-24.918 0-47.632 14.077-58.264 36.087L352.876 325.449l-232.025 34.509c-23.84 3.574-43.606 19.851-51.329 42.155-7.685 22.299-1.873 46.884 14.989 63.662L254.491 635.63 215.04 871.145c-3.946 23.716 6.311 47.551 26.454 61.424 11.087 7.642 24.086 11.464 37.084 11.464 10.718 0 21.473-2.621 31.149-7.809l202.25-108.934L714.31 936.224c9.714 5.23 20.431 7.809 31.105 7.809 12.999 0 25.996-3.864 37.127-11.464 20.1-13.874 30.354-37.67 26.369-61.424L769.5 635.63l170.104-169.855C956.382 448.997 962.114 424.412 954.514 402.113L954.514 402.113zM734.95 590.657l-28.326 28.278 6.563 39.457 39.409 235.058L548.812 783.81l-36.833-19.851L475.14 783.81l-203.828 109.68 39.414-235.098 6.602-39.457-28.321-28.278-168.61-168.277 231.274-34.348 40.702-6.058 17.855-37.049 101.75-211.051 101.746 211.051 17.898 37.049 40.658 6.058 231.275 34.348L734.95 590.657 734.95 590.657z"
                            p-id="13563"></path>
                    </svg>
                    <span class="xicon-content">{{ post.star }} </span>
                </span>
                <span class="xicon-container left">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32"
                        class="xicon-icon" style="width: 18px; height: 18px; font-size: 18px; color: inherit;">
                        <path
                            d="M26 4h-4V2h-2v2h-8V2h-2v2H6c-1.1 0-2 .9-2 2v20c0 1.1.9 2 2 2h20c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 22H6V12h20v14zm0-16H6V6h4v2h2V6h8v2h2V6h4v4z"
                            fill="currentColor"></path>
                    </svg>
                    <span class="xicon-content">{{ post.ctime }}</span></span>
            </div>
        </section>

        <!-- 文章内容 -->
        <article v-html="post.content" class="post-content markdown-body">
        </article>

        <div class="page-meta">
            <div class="block">

                <span v-for="tag of post.tag" class="xicon-container left">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32"
                        class="xicon-icon" style="width: 18px; height: 18px; font-size: 18px; color: inherit;">
                        <path
                            d="M10 14a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4zm0-6a2 2 0 1 0 1.998 2.004A2.002 2.002 0 0 0 10 8z"
                            fill="currentColor"></path>
                        <path
                            d="M16.644 29.415L2.586 15.354A2 2 0 0 1 2 13.941V4a2 2 0 0 1 2-2h9.941a2 2 0 0 1 1.414.586l14.06 14.058a2 2 0 0 1 0 2.828l-9.943 9.943a2 2 0 0 1-2.829 0zM4 4v9.942L18.058 28L28 18.058L13.942 4z"
                            fill="currentColor"></path>
                    </svg>
                    <span class="xicon-content">{{ tag }}</span></span>
            </div>

            <div class="meta-item last-updated"><span class="xicon-container left meta-item-label">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 32 32"
                        class="xicon-icon" style="width: 20px; height: 20px; font-size: 20px; color: inherit;">
                        <path
                            d="M26 4h-4V2h-2v2h-8V2h-2v2H6c-1.1 0-2 .9-2 2v20c0 1.1.9 2 2 2h20c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 22H6V12h20v14zm0-16H6V6h4v2h2V6h8v2h2V6h4v4z"
                            fill="currentColor"></path>
                    </svg>
                    <span class="xicon-content">Updated {{ post.ltime }}</span></span></div>
        </div>

        <section class="post-author">
            <figure class="author-avatar">
                <img src="https://cravatar.cn/avatar/d22eb460ecab37fcd7205e6a3c55c228?s=200&amp;r=X" alt="Paul" width="200"
                    height="200">
            </figure>
            <div class="author-info">
                <h4>Paul</h4>
                <p>特立独行的一只前端菜狗。本站未注明转载的文章均为原创，并采用 <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh"
                        target="_blank" rel="nofollow">CC BY-NC-SA 4.0</a> 授权协议，<span>转载请注明来源</span>，谢谢！如本站内容对你有所帮助的话，不妨 <a
                        href="https://paul.ren/donate">捐助支持</a> 一下？同时欢迎订阅关注 <a href="https://paul.ren/note"
                        target="_blank">我的日记</a>，唠嗑（分享）每日的折腾经历。</p>
            </div>
        </section>

        <section class="post-near">
            <ul>
                <li>上一篇: <a href="https://paugram.com/essay/my-thoughts-about-fall-in-love-or-get-married.html"
                        title="谈谈我对恋爱/结婚的想法">谈谈我对恋爱/结婚的想法</a></li>
                <li>下一篇: 看完啦 (つд⊂)</li>
            </ul>
        </section>
        <section class="article-list">
            <h4><span class="title">目录</span></h4>
            <a v-for="item of toc" :href="'#' + item.id" :class="'toc_' + item.level">{{ item.text }}</a>
        </section>
    </div>
</template>

<style>
@media screen and (min-width: 800px) {
    body {
        margin-right: 15em;
    }
}

.block .xicon-container.left {
    margin-right: 10px;
}
</style>

<script setup>

import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import MarkdownIt from 'markdown-it';
import MarkdownItAnchor from 'markdown-it-anchor';
import MarkdownItTaskList from 'markdown-it-task-lists';
import hljs from 'highlight.js';
import 'highlight.js/styles/atom-one-dark.min.css';

const { params } = useRoute();
const post = ref({});
const toc = ref("");

//获取toc
function getToc(html, depth = 2) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const headers = doc.querySelectorAll(`h1, h2, h3, h4, h5, h6`);
    const toc = [];

    headers.forEach(header => {
        const id = header.getAttribute('id');
        const text = header.innerText || header.textContent;
        const level = parseInt(header.tagName.slice(1));
        if (id && text && level <= depth) {
            toc.push({ id, text, level });
        }
    });

    return toc;
}

function fetchPostData() {
    const title = params.title;
    axios
        .get(`http://127.0.0.1:8000/draft/${title}`)
        .then(response => {
            post.value = response.data;
            const md = new MarkdownIt()
                .use(MarkdownItAnchor)
                .use(MarkdownItTaskList)
                .use((md) => {
                    // 设置 highlight.js
                    md.options.highlight = (code, lang) => {
                        if (lang && hljs.getLanguage(lang)) {
                            try {
                                return hljs.highlight(lang, code).value;
                            } catch (error) {
                                console.error(error);
                            }
                        }
                        return ''; // 若语言未指定或者未识别，返回原始的 HTML 代码
                    };
                });
            post.value.content = md.render(post.value.content);
            // console.log(post.value.content);
            toc.value = getToc(post.value.content, 1)

            
        })
        .catch(error => {
            // document.location.href = "/404";
        });
}



onMounted(fetchPostData);

</script>