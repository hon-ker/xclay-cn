<template>
    <div class="buttons">
        <a class="to-top" :class="{ active: isScrolled }" href="#"></a>
        <a class="toggle-list" ></a>
    </div>
    <div class="wrap min">
        <section class="widget">
            <div class="row">
                <div class="col-m-4">
                    <h3 class="title-recent">热门文章：</h3>
                    <ul>
                        <li><a href="" target="_blank">给你的博客增加动态看板娘</a></li>
                        <li><a href="" target="_blank">Single
                                主题与单身狗</a></li>
                        <li><a href="" target="_blank">Fantasy 幻想动漫风主题</a>
                        </li>
                        <li><a href="" target="_blank">CloudCone
                                折腾记</a></li>
                        <li><a href="" target="_blank">让你的网站实现
                                PJAX 无刷新</a></li>
                        <li><a href="" target="_blank">让你的网站文字“抖”起来</a>
                        </li>
                    </ul>
                </div>
                <div class="col-m-4">
                    <h3 class="title-date">时光机：</h3>
                    <ul>
                        <li><a href="https://paugram.com/2023/09/" rel="nofollow" target="_blank">2023 年 09 月</a></li>
                        <li><a href="https://paugram.com/2023/07/" rel="nofollow" target="_blank">2023 年 07 月</a></li>
                        <li><a href="https://paugram.com/2023/05/" rel="nofollow" target="_blank">2023 年 05 月</a></li>
                        <li><a href="https://paugram.com/2022/11/" rel="nofollow" target="_blank">2022 年 11 月</a></li>
                        <li><a href="https://paugram.com/2022/09/" rel="nofollow" target="_blank">2022 年 09 月</a></li>
                        <li><a href="https://paugram.com/2022/07/" rel="nofollow" target="_blank">2022 年 07 月</a></li>
                    </ul>
                </div>
                <div class="col-m-4">
                    <h3 class="title-comments">最近评论：</h3>
                    <ul>
                        <li>舒克: <a
                                href="https://paugram.com/essay/my-thoughts-about-fall-in-love-or-get-married.html/comment-page-1#comment-1237"
                                rel="nofollow" target="_blank">工作之余，真的...</a></li>
                        <li>Heresy: <a
                                href="https://paugram.com/essay/my-thoughts-on-open-source-software.html/comment-page-1#comment-1236"
                                rel="nofollow" target="_blank">用爱发电真不容...</a></li>
                        <li>步丈九州: <a
                                href="https://paugram.com/essay/my-thoughts-about-fall-in-love-or-get-married.html/comment-page-2#comment-1235"
                                rel="nofollow" target="_blank">笑死</a></li>
                        <li>步丈九州: <a
                                href="https://paugram.com/essay/my-thoughts-about-fall-in-love-or-get-married.html/comment-page-1#comment-1234"
                                rel="nofollow" target="_blank">情况和大佬类似...</a></li>
                        <li>rcqed: <a
                                href="https://paugram.com/essay/my-thoughts-on-open-source-software.html/comment-page-1#comment-1233"
                                rel="nofollow" target="_blank">赞同博主的观点...</a></li>
                        <li>Paul: <a
                                href="https://paugram.com/essay/my-thoughts-on-open-source-software.html/comment-page-1#comment-1232"
                                rel="nofollow" target="_blank">如果是 Win...</a></li>
                    </ul>
                </div>
            </div>
        </section>
        <section class="sub-footer">
            <p>© 2023 <a href="https://paugram.com/">保罗的小宇宙</a>. All Rights Reserved. Theme By <a
                    href="https://github.com/Dreamer-Paul/Single" target="_blank" rel="nofollow">Single</a>.</p>
        </section>
    </div>
</template>

<script setup>

import { ref, onMounted, onUnmounted } from 'vue';

// 声明一个 ref 变量用于判断是否滚动超过 300px
const isScrolled = ref(false);

// 定义判断滚动高度的函数
function checkScrollHeight() {
    const scrollY = window.scrollY || window.pageYOffset;
    isScrolled.value = scrollY > 300;
}
// 在组件挂载时添加滚动监听事件
onMounted(() => {
    window.addEventListener('scroll', checkScrollHeight);
});

// 在组件卸载时移除滚动监听事件
onUnmounted(() => {
    window.removeEventListener('scroll', checkScrollHeight);
});

</script>