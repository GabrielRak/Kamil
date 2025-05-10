<template>
    <div class="container">
        <h1>Sign Up</h1>
        <form @submit="handleSubmit" class="space-y-6 bg-white p-6 rounded-lg shadow-md">
            <div class="flex flex-col">
            <label for="username" class="mb-2 text-sm font-medium text-gray-700">Username:</label>
            <input type="text" id="username" name="username" required 
                class="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
            </div>
            <div class="flex flex-col">
            <label for="email" class="mb-2 text-sm font-medium text-gray-700">Email:</label>
            <input type="email" id="email" name="email" required 
                class="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
            </div>
            <div class="flex flex-col">
            <label for="password" class="mb-2 text-sm font-medium text-gray-700">Password:</label>
            <input type="password" id="password" name="password" required 
                class="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
            </div>
            <div class="flex flex-col">
            <label for="repeatPassword" class="mb-2 text-sm font-medium text-gray-700">Repeat Password:</label>
            <input type="password" id="repeatPassword" name="repeatPassword" required 
                class="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
            </div>
            <div class="flex flex-col">
            <label for="bio" class="mb-2 text-sm font-medium text-gray-700">Bio:</label>
            <textarea id="bio" name="bio" 
                class="border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"></textarea>
            </div>
            <button type="submit" 
            class="w-full bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
            Sign Up
            </button>
        </form>
    </div>
</template>

<script setup>
import { useAuthStore } from "../../stores/authStore";

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