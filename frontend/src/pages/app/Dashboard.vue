<template>
    <div>

        <h1>users data§</h1>
        
        <div class="container">
            <h1> <b>User data:</b>{{user}}</h1>
        </div>
        
    </div>
    </template>
<script setup>

import { onMounted } from 'vue';
import {useAuthStore} from '../../stores/authStore';
import { storeToRefs } from 'pinia';

const userStore = useAuthStore();

const {user}  = storeToRefs(userStore);

</script>