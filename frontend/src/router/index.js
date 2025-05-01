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
        path: '/portfolio',
        name: 'Portfolio',
        component: () => import('../pages/Portfolio.vue'),
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('../pages/Dashboard.vue'),
    },
    {
        path:'/post/:postId(\\w+)',
        name: 'Post',
        component: () => import('../pages/Post.vue'),
        props: true,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;