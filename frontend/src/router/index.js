import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {
        path:'/',
        name: 'Home',
        component: () => import('../pages/Home.vue'),
    },
    {
        path: '/blog',
        name: 'Blog',
        component: () => import('../pages/Blog.vue'),
    },
    {
        path:'/about',
        name:'About',
        component:() => import('../pages/About.vue'),
    },
    {
        path:'/careers',
        name:'Careers',
        component:() => import('../pages/Careers.vue'),
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('../pages/app/Dashboard.vue'),
    },
    {
        path:'/post/:id',
        name: 'Post',
        component: () => import('../pages/Post.vue'),
        props: true,
    },
    {
        path:'/sign_up',
        name:'Register',
        component:() => import('../pages/auth/Sign_up.vue'),
    },
    {
        path:'/sign_in',
        name:'Login',
        component:() => import('../pages/auth/Sign_in.vue'),
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;