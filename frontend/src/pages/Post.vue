<template>
    <div class="post">
        <!-- Content removed as 'posts' is not defined -->
        <h1 class="post-title">{{ post.title }}</h1>
        <p class="post-content">{{ post.content }}</p>
        <p class="post-author">Written by: {{ post.author }}</p>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useBlogStore } from '../stores/blogStore';
import { storeToRefs } from 'pinia';
import { useRoute } from 'vue-router';

const route = useRoute();
const postId = route.params.id;
const blogStore = useBlogStore();

onMounted(() => {
    blogStore.fetchPost(postId);
});

const { post } = storeToRefs(blogStore);

</script>

<style scoped>
.post {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    max-width: 600px;
    margin: 20px auto;
}

.post-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

.post-content {
    font-size: 16px;
    margin-bottom: 10px;
}

.post-author {
    font-size: 14px;
    color: #555;
}
</style>