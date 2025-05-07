import { defineStore } from "pinia";
import axios from "axios";
export const useAuthStore = defineStore("authStore", {
    state:()=>({
        user: null,
        token: null,
        loading: false,
        error: null,
    }),
    actions:{
        async registerUser(data) {
          axios.post('http://localhost:8000/users/register', {
            username: data.username,
            password: data.password,
            email: data.email,
            bio: data.bio
          }, {
            headers: {
              'Content-Type': 'application/json'
            }
          }).then(res => {
            console.log('User registered:', res.data)
          }).catch(err => {
            console.error('Registration failed:', err.response?.data || err)
          })
        },
        async authUser(username,passsword) {  
            this.loading = true;
            this.error = null;
            try {
                const response = await axios.post("http://localhost:8000/users/login", {
                    username:username,
                    password: passsword,
                });
                this.user = response.data.user;
                console.log("User authenticated:", this.user);
            } catch (error) { 
                this.error = error.response?.data || "An error occurred";
            } finally {
                this.loading = false;
            }
        }
    }
});