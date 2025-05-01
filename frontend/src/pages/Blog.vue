<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <Posts :posts="posts" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useBlogStore } from "../stores/blogStore";
import { storeToRefs } from "pinia";
import Posts from "../views/Posts.vue";
const store = useBlogStore();

onMounted(() => {
  store.fetchPosts();
});

const { posts, loading, error } = storeToRefs(store);
</script>
