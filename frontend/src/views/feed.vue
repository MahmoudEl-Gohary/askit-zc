<script setup lang="ts">
import { ref } from 'vue';
import Header from '@/components/Header.vue';

// Simulated data for posts
const posts = ref([
  {
    id: 1,
    user: {
      name: 'John Doe',
      image: '/src/assets/images/profile.jpg',
    },
    content: 'This is my first post!',
  },
  {
    id: 2,
    user: {
      name: 'Jane Smith',
      image: '/src/assets/images/profile2.jpg',
    },
    content: 'Loving this platform! 💙',
  },
]);

// New post content
const newPostContent = ref('');

// Function to add a new post
const addPost = () => {
  if (newPostContent.value.trim()) {
    posts.value.unshift({
      id: Date.now(),
      user: {
        name: 'Current User', // Replace with logged-in user’s name
        image: '/src/assets/images/profile.jpg', // Replace with logged-in user’s image
      },
      content: newPostContent.value,
    });
    newPostContent.value = '';
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <Header />

    <!-- Main Content -->
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Add Post Box -->
      <div class="bg-white shadow-lg rounded-lg p-6 mb-8">
        <h2 class="text-xl font-bold text-gray-800 mb-4">Create a Post</h2>
        <textarea
          v-model="newPostContent"
          placeholder="What's on your mind?"
          class="w-full p-4 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
          rows="3"
        ></textarea>
        <button
          @click="addPost"
          class="mt-4 bg-[#00b4d1] text-white px-6 py-2 rounded-lg hover:bg-[#0097b3] transition-all"
        >
          Post
        </button>
      </div>

      <!-- User Posts -->
      <div class="space-y-6">
        <div
          v-for="post in posts"
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
        <div v-if="posts.length === 0" class="text-gray-500 text-center">
          No posts yet. Be the first to post!
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Additional styles to match the existing theme */
</style>
