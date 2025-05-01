<template>
  <div class="post-list">
    <h1>Blog Posts</h1>
    <div>
      <div v-for="post in posts" :key="post.id" class="post">
        <RouterLink to="/post/{{ post.id }}">
          <h2 class="font-bold text-2xl text-gray-800">{{ post.title }}</h2>
        </RouterLink>
        <h1 class="font-bold text-3xl text-center">{{ post.title }}</h1>

        <div v-for="content in post.chapters" :key="content.id">
          <h3 class="text-xl text-gray-700">{{ content.title }}</h3>
          <p>{{ content.content }}</p>
        </div>
        <small>{{ formatDate(post.created_at) }}</small>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Posts",
  props: {
    posts: {
      type: Array,
      required: true,
    },
  },
  methods: {
    formatDate(date) {
      const options = { year: "numeric", month: "long", day: "numeric" };
      return new Date(date).toLocaleDateString(undefined, options);
    },
  },
};
</script>
