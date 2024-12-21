<script>
import axios from 'axios';
import Header from '@/components/Header.vue';

export default {
  name: 'QuestionView',

  components: {
    Header,
  },

  data() {
    return {
      question: {
        id: null,
        title: '',
        body: '',
        created_by: { first_name: '', last_name: '' },
        created_at_formated: '',
        is_anonymous: false,
        answers: [],
      },
      body: '', // To hold the new comment input
    };
  },

  mounted() {
    const questionId = this.$route.params.id;
    console.log('Question ID:', questionId); // Debugging
    if (questionId) {
      this.getQuestion(questionId);
    } else {
      console.error('Question ID is missing from route params.');
    }
  },

  methods: {
    // Fetch the question details from the backend
    getQuestion(id) {
      axios
        .get(`/api/questions/${id}/`)
        .then((response) => {
          console.log('Question data:', response.data);
          this.question = response.data.question;
        })
        .catch((error) => {
          console.error('Error fetching question:', error);
        });
    },

    // Submit a new answer to the question
    submitForm() {
      console.log('Submitting form with body:', this.body); // Debug log
      if (!this.body.trim()) {
        console.error('Comment body is empty.');
        return; // Prevent empty submissions
      }

      axios
        .post(`/api/questions/${this.$route.params.id}/answers/`, { body: this.body })
        .then((response) => {
          console.log('Answer added:', response.data);
          this.question.answers.unshift(response.data); // Add the new answer to the top of the list
          this.body = ''; // Clear the textarea
        })
        .catch((error) => {
          console.error('Error adding answer:', error);
        });
    },
  },
};
</script>

<template>
  <div>
    <!-- Header -->
    <Header />

    <!-- Question Details -->
    <div v-if="question.id" class="max-w-5xl mx-auto px-6 py-12 bg-gray-50">
      <div class="bg-white shadow-lg rounded-lg p-6">
        <h1 class="text-3xl font-bold text-gray-800">{{ question.title }}</h1>
        <div class="flex items-center mt-2 text-sm text-gray-500">
          <span v-if="question.is_anonymous">Anonymous User</span>
          <span v-else>
            {{ question.created_by.first_name }} {{ question.created_by.last_name }}
          </span>
          <span class="ml-4">{{ question.created_at_formated }}</span>
        </div>
        <p class="text-gray-700 text-lg mb-6">{{ question.body }}</p>
      </div>

      <!-- Answers Section -->
      <div class="bg-white shadow-lg rounded-lg p-6 mt-8">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Answers</h2>
        <div v-if="question.answers && question.answers.length > 0" class="space-y-4">
          <div
            v-for="answer in question.answers"
            :key="answer.id"
            class="p-4 bg-gray-100 rounded-lg shadow-sm"
          >
            <p class="text-gray-700">{{ answer.body }}</p>
            <div class="text-sm text-gray-500 mt-2">
              <span v-if="answer.is_anonymous">Anonymous User</span>
              <span v-else>
                {{ answer.created_by.first_name }} {{ answer.created_by.last_name }}
              </span>
              <span class="ml-4">{{ answer.created_at_formated }}</span>
            </div>
          </div>
        </div>
        <div v-else class="text-gray-500">No answers yet. Be the first to answer!</div>
      </div>

      <!-- Add a Comment Section -->
      <div class="bg-white shadow-lg rounded-lg p-6 mt-8">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Add a Comment</h2>
        <textarea
          v-model="body"
          placeholder="Write your comment here..."
          class="w-full h-28 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
        ></textarea>
        <button
          @click="submitForm"
          class="mt-4 px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition"
        >
          Submit Comment
        </button>
      </div>
    </div>

    <!-- Error Case for Missing Question -->
    <div v-else class="text-center text-gray-500 mt-20">
      <p>Question not found or invalid ID.</p>
    </div>
  </div>
</template>


