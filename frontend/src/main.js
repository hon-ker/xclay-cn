import './assets/clay.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { MyAxios } from './assets/clay.utils'

const app = createApp(App)


router.beforeEach(async (to, from, next) => {
    if (to.path.includes('admin')) {
        try {
            const res = await MyAxios.get("/is_login")
            if (!res.data.is_login) {
                next('/login'); 
            } else {
                next();
            }
        } catch (error) {
            // console.error('请求登录状态时出现错误:', error);
            // next(false); // 如果请求出错，禁止导航
            next('/login');
        }
    } else {
        next(); // 其他页面继续导航
    }
});


app.use(router)



app.mount('#app')
