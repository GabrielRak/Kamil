<template>
    <div class="sign-in">
        <h1>Sign In</h1>
        <form @submit.prevent="handleSignIn">
            <div>
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="email" required />
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" id="password" v-model="password" required />
            </div>
            <button type="submit">Sign In</button>
        </form>
    </div>
</template>

<script>
import { useAuthStore } from "../../stores/authStore";
export default {
    name: "SignIn",
    data() {
        return {
            email: "",
            password: "",
        };
    },
    methods: {
        async handleSignIn() {
            const authStore = useAuthStore();
            try {
                await authStore.authUser(this.email, this.password);
                this.$router.push("/dashboard");
            } catch (error) {
                console.error("Sign-in failed:", error);
            }
        },
    },
};
</script>

<style scoped>
.sign-in {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
}
form div {
    margin-bottom: 15px;
}
label {
    display: block;
    margin-bottom: 5px;
}
input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}
button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
button:hover {
    background-color: #0056b3;
}
</style>
