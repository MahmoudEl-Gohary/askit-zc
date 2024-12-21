<!-- questions.vue -->
<script setup>
import { onMounted, computed } from 'vue';
import { useQuestionsStore } from '@/stores/questions';
import axios from 'axios';

const questionsStore = useQuestionsStore();

function upvoteQuestion(id) {
  axios
    .post(`/api/questions/${id}/upVotes/`)
    .then((response) => {
      console.log(response.data);
      if (response.data.message == 'UpVoted') {
        this.question.upvotes_count += 1;
      }
      questionsStore.fetchQuestions();
    })
    .catch((error) => {
      console.error('Error upvoting question:', error);
    });
}

function downvoteQuestion(id) {
  console.log('Downvoting question with id:', id);

  axios
    .post(`/api/questions/${id}/downVotes/`)
    .then((response) => {
      console.log(response.data);
      if (response.data.message == 'DownVoted') {
        this.question.downvotes_count += 1;
      }
      questionsStore.fetchQuestions();
    })
    .catch((error) => {
      console.error('Error downvoting question:', error);
    });
}

onMounted(() => {
  questionsStore.fetchQuestions();
});

const questions = computed(() => questionsStore.questions);
</script>

<template>
      <div class="space-y-6">
        <div
          v-for="question in questions"
          :key="question.id"
          class="bg-white shadow-lg rounded-lg p-4 space-y-4"
        >
          <!-- Post Header -->
          <div class="flex items-center space-x-4">
            <img
              v-if="question.is_anonymous"
              src= "../assets/images/anonymous.png"
              alt="User Profile"
              class="h-12 w-12 object-cover"
            />
            <img
              v-else
              src= "../assets/images/profile.jpg"
              alt="User Profile"
              class="h-12 w-12 rounded-full object-cover"
            />
        <div>

            <h3 class="text-lg font-semibold text-gray-800">
                <span v-if="question.is_anonymous">Anonymous User</span>
                <span v-else>{{ question.created_by.first_name }} {{ question.created_by.last_name }}</span>
            </h3>
            
            <h6 class=" text-sm font-semibold text-gray-600">
                <span v-if="question.is_anonymous"></span>
                <span v-else>{{ question.created_by.major }}, {{ question.created_by.year }}</span>
            </h6>

              <p class="text-sm text-gray-500">{{ question.created_at_formated }}</p>
            </div>
          </div>

            <!-- Post Title -->
            <h2 class="text-xl font-semibold text-gray-900">{{ question.title }}</h2>
          <!-- Post Content -->
          <p class="text-gray-700">{{ question.body }}</p>

          <hr class="mt-4 mb-3" />

          <!-- Post Footer -->
          <div class="flex items-center justify-between text-gray-500 text-sm">
            <!-- Left Column -->
            <div>
              <button
                class="flex items-center bg-white px-3 py-1.5 rounded-md hover:bg-gray-200 transition-all"
                @click="upvoteQuestion(question.id)"
              >
                <img
                  src="/src/assets/Icons/Upvote.png"
                  alt="UpVote Icon"
                  class="h-5 w-5 mr-2"
                />
                {{ question.upvotes_count }} UpVotes
              </button>
            </div>


            <!-- Center Column -->
            <div>
              <button
              class="flex items-center bg-white px-3 py-1.5 rounded-md hover:bg-gray-200 transition-all"

              >
                <img
                  src="/src/assets/Icons/answer.png"
                  alt="Answers Icon"
                  class="h-5 w-5 mr-2"
                />
                <!-- {{ post.Answers }} --> 10 Answers 
              </button>
            </div>

            <!-- Right Column -->
            <div>
              <button
              class="flex items-center bg-white px-3 py-1.5 rounded-md hover:bg-gray-200 transition-all"
              @click="downvoteQuestion(question.id)"
              >
                <img
                  src="/src/assets/Icons/downvote.png"
                  alt="DownVote Icon"
                  class="h-5 w-5 mr-2"
                />
                {{ question.downvotes_count }} DownVotes
              </button>
            </div>
          </div>
        </div>

        <!-- No Posts Found -->
        <div v-if="questions.length === 0" class="text-gray-500 text-center">
          <p>No posts yet. Be the first to post!</p>
        </div>
      </div>
</template>