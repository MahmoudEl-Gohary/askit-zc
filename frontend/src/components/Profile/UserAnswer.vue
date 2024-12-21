<script setup lang="ts">
import { ref } from 'vue'

const answers = ref([
  {
    id: 1,
    questionTitle: 'Best practices for Vue.js state management',
    answer: 'For small to medium applications, the Composition API with provide/inject...',
    votes: 12,
    accepted: true,
    date: '2024-03-14',
  },
  {
    id: 2,
    questionTitle: 'How to handle authentication in Vue?',
    answer: 'You can implement authentication using Vue Router guards...',
    votes: 7,
    accepted: false,
    date: '2024-03-12',
  },
])
</script>

<template>
  <div class="bg-white rounded-lg shadow p-6">
    <h2 class="text-xl font-bold text-gray-900 mb-4">My Answers</h2>
    <div class="space-y-4">
      <div v-for="answer in answers" :key="answer.id" class="border-b pb-4 last:border-0">
        <h3 class="text-lg font-semibold text-gray-900">{{ answer.questionTitle }}</h3>
        <p class="text-gray-600 mt-1">{{ answer.answer }}</p>
        <div class="flex items-center space-x-4 mt-2 text-sm">
          <span class="text-gray-500">{{ answer.votes }} votes</span>
          <span v-if="answer.accepted" class="text-green-600">✓ Accepted</span>
          <span class="text-gray-500">{{ answer.date }}</span>
        </div>
      </div>
    </div>
  </div>
</template>