<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import Header from '@/components/Header.vue';
import { useQuestionsStore } from '@/stores/questions';

// Store setup
const questionsStore = useQuestionsStore();

const searchQuery = ref('');
const questions = computed(() => questionsStore.questions);

onMounted(async () => {
  try {
    await questionsStore.fetchQuestions();
  } catch (error) {
    console.error('Error fetching questions:', error);
  }
});

const filteredQuestions = computed(() =>
  questions.value.filter((question) => {
    const query = searchQuery.value.toLowerCase();
    return (
      question.title.toLowerCase().includes(query) ||
      question.body.toLowerCase().includes(query) ||
      question.created_by.uni_id.includes(query) ||
      (question.is_anonymous
        ? 'anonymous'.toLowerCase().indexOf(query) !== -1 // Use indexOf as a fallback
        : question.created_by.first_name.toLowerCase().includes(query) ||
          question.created_by.last_name.toLowerCase().includes(query))
    );
  })
);
</script>

<template>
  <Header />

  <div class="min-h-screen bg-gray-50">
    <div class="max-w-5xl mx-auto px-6 py-12">
      <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Search Questions</h1>
      <p class="text-gray-600 mb-10">Use the search bar below to find questions.</p>

      <div class="bg-white shadow-lg rounded-lg p-4 mb-8">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search for questions..."
          class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
        />
      </div>

      <div class="space-y-6">
        <div
          v-for="question in filteredQuestions"
          :key="question.id"
          class="bg-white shadow-lg rounded-lg p-6 flex items-start space-x-4"
        >
          <img
            v-if="question.is_anonymous"
            src="../assets/images/anonymous.png"
            alt="User Profile"
            class="h-12 w-12 object-cover rounded-full"
          />
          <img
            v-else
            src="../assets/images/profile.jpg"
            alt="User Profile"
            class="h-12 w-12 object-cover rounded-full"
          />

          <div class="flex-grow">
              <h3 class="text-lg font-semibold text-gray-800">
                <span v-if="question.is_anonymous">Anonymous User</span>
                <span v-else>{{ question.created_by.first_name }} {{ question.created_by.last_name }}</span>
              </h3>
              <h6 class=" text-sm font-semibold text-gray-600">
                <span v-if="question.is_anonymous"></span>
                <span v-else>{{ question.created_by.major }}, {{ question.created_by.year }}</span>
            </h6>
              <h2 class="text-xl font-semibold text-gray-900">{{ question.title }}</h2>
              <p class="text-gray-700">{{ question.body }}</p>
              <p class="text-sm text-gray-500">{{ question.created_at_formated }}</p>
          </div>
        </div>

        <div v-if="filteredQuestions.length === 0" class="text-gray-500 text-center">
          <p>No questions found. Try a different search term.</p>
        </div>
      </div>
    </div>
  </div>
</template>


