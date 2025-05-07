<template>
    <div class="container">
        <h1>Sign Up</h1>
        <form @submit="handleSubmit">
            <div>
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required />
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required />
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required />
            </div>
            <div>
                <label for="repeatPassword">Repeat Password:</label>
                <input type="password" id="repeatPassword" name="repeatPassword" required />
            </div>
            <div>
                <label for="bio">Bio:</label>
                <textarea id="bio" name="bio"></textarea>
            </div>
            <button type="submit">Sign Up</button>
        </form>
    </div>
</template>

<script setup>
import { useAuthStore } from "../stores/authStore";

const store = useAuthStore();

const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    try {
        await store.registerUser(data);
        console.log("Registration successful!");
    } catch (error) {
        console.log("Registration failed: " + error.message);
    }
};
</script>