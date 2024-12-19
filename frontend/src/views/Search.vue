<script setup lang="ts">
import Header from '@/components/Header.vue';
import { ref, computed } from 'vue';

// Sample posts data
const posts = ref([
  {
    id: 1,
    user: {
      name: 'John Doe',
      image: '/src/assets/images/profile.jpg',
    },
    content: 'This is a post about Vue.js.',
  },
  {
    id: 2,
    user: {
      name: 'Jane Smith',
      image: '/src/assets/images/profile2.jpg',
    },
    content: 'I love programming and web development.',
  },
  {
    id: 3,
    user: {
      name: 'Alice Johnson',
      image: '/src/assets/images/profile3.jpg',
    },
    content: 'Searching for posts is super fun!',
  },
]);

// Search query
const searchQuery = ref('');

// Computed property to filter posts based on the search query
const filteredPosts = computed(() =>
  posts.value.filter((post) =>
    post.content.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
);
</script>

<template>
    <Header />

  <div class="min-h-screen bg-gray-50">
    <div class="max-w-5xl mx-auto px-6 py-12">
      <!-- Page Header -->
      <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Search Posts</h1>
      <p class="text-gray-600 mb-10">
        Use the search bar below to find posts based on their content or keywords.
      </p>

      <!-- Search Bar -->
      <div class="bg-white shadow-lg rounded-lg p-4 mb-8">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search for posts..."
          class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
        />
      </div>

      <!-- Posts List -->
      <div class="space-y-6">
        <!-- Render filtered posts -->
        <div
          v-for="post in filteredPosts"
          :key="post.id"
          class="bg-white shadow-lg rounded-lg p-6 flex items-start space-x-4"
        >
          <!-- User Image -->
          <img
            :src="post.user.image"
            alt="User Profile"
            class="h-12 w-12 rounded-full object-cover"
          />
          <!-- Post Content -->
          <div>
            <h3 class="text-lg font-semibold text-gray-800">{{ post.user.name }}</h3>
            <p class="text-gray-600 mt-2">{{ post.content }}</p>
          </div>
        </div>

        <!-- No Posts Found -->
        <div v-if="filteredPosts.length === 0" class="text-gray-500 text-center">
          <p>No posts found. Try a different search term.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Add any additional scoped styles if necessary */
</style>
