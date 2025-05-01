import { defineStore } from "pinia";
import { fetchPosts } from "../services/blog_requests";

export const useBlogStore = defineStore("blogStore", {
  state: () => ({
    posts: [],
    loading: false,
    error: null,
  }),

  actions: {
    async fetchPosts() {
      this.loading = true;
      this.error = null;

      try {
        this.posts = await fetchPosts();
      } catch (err) {
        this.error = "Failed to load data";
      } finally {
        this.loading = false;
      }
    },
  },
});
