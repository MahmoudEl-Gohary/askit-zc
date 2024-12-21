<script setup lang="ts">
import Header from '../components/Header.vue';
import UserQuestion from '@/components/Profile/UserQuestion.vue';

import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useToastStore } from '@/stores/toast';

const userStore = useUserStore();
const toastStore = useToastStore();

const user = ref({
  id: '',
  name: '',
  bio: '',
  description: '',
});

const posts = ref([]);

const getFeed = () => {
  axios
    .get(`/api/posts/profile/${userStore.user.id}/`)
    .then(response => {
      posts.value = response.data.posts;
      user.value = response.data.user;
    })
    .catch(error => {
      console.log('error', error);
    });
};

onMounted(() => {
  getFeed();
});

watch(
  () => userStore.user.id,
  () => {
    getFeed();
  },
  { immediate: true }
);
</script>

<template>
  <Header />
  <div class="min-h-screen bg-gray-50">
    <!-- Cover Photo -->
    <div class="relative h-48 md:h-64">
      <img
        src="/src/assets/images/profile.jpg"
        alt="Cover"
        class="w-full h-full object-cover"
      />
    </div>

    <!-- Profile Info -->
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="relative -mt-12 sm:-mt-16">
        <div class="flex flex-col sm:flex-row items-center sm:items-end sm:space-x-5 m-5 p-3">
          <!-- Profile Picture -->
          <div class="relative">
            <img
              src="/src/assets/images/anonymous.png"
              alt="Profile"
              class="h-24 w-24 sm:h-32 sm:w-32 rounded-full border-4 border-white shadow-lg"
            />
          </div>

          <!-- Profile Details -->
          <div class="mt-4 sm:mt-0 text-center sm:text-left">
            <!--edit here for the name and zewailcity ID-->
            <h1 class="text-2xl font-bold text-gray-900">Ahmed Sameh</h1>
            <p class="mt-1 text-gray-600">202201124</p>
          </div>
        </div>
      </div>
    </div>

    <!-- User Questions Section -->
    <UserQuestion :posts="posts" />
    
  </div>
</template>

<style scoped>
/* Add any additional styles if needed */
</style>