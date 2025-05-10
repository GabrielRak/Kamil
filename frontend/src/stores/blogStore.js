import { defineStore } from "pinia";
import { fetchPosts,fetchPost } from "../services/blog_requests";

export const useBlogStore = defineStore("blogStore", {
  state: () => ({
    posts: [],
    post:[],
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
    async fetchPost(id){
      this.loading = true;
      this.error = null;
      try {
        this.post = await fetchPost(id);
      } catch (err) {
        this.error = "Failed to load data";
      } finally {
        this.loading = false;
      }
    }
  },
});
