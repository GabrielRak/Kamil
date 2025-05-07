<template>
    <div class="post">
        <h1 class="post-title">{{ post.title }}</h1>
        <p class="post-content">{{ post.content }}</p>
        <p class="post-author">Written by: {{ post.author }}</p>
    </div>
</template>

<script>
export default {
    name: "Post",
    data() {
    }
};
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