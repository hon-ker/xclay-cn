import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: IndexView
        },
        {
            path: '/post/:title',
            name: 'post',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/PostView.vue')
        },
        {
            path: '/404',
            name: '404',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/404View.vue')
        },{
            path: '/md',
            name: '12138',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../components/modules/Editor.vue')
        },
        {
            path: '/edit',
            name: '441',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/Draftview.vue')
        },
        {
            path: '/admin',
            name: '44',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/Admin.vue')
        },
        {
            path: '/login',
            name: 'cas',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/LoginView.vue')
        }
    ]
})

export default router
