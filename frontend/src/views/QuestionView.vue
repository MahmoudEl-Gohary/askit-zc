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
      body: '', 
    };
  },

  mounted() {
    const questionId = this.$route.params.id;
    if (questionId) {
      this.getQuestion(questionId);
    } else {
      console.error('Question ID is missing from route params.');
    }
  },

  methods: {
    getQuestion(id) {
      axios
        .get(`/api/questions/${id}/`)
        .then((response) => {
          this.question = response.data.question;
        })
        .catch((error) => {
          console.error('Error fetching question:', error);
        });
    },

    // Submit a new answer to the question
    submitForm() {
      if (!this.body.trim()) {
        console.error('Answer body is empty.');
        return; // Prevent empty submissions
      }

      axios
        .post(`/api/questions/${this.$route.params.id}/answers/`, { body: this.body })
        .then((response) => {
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
        <!-- Question Creator Info -->
        <div class="flex items-center space-x-4 mb-4">
          <img
            v-if="question.is_anonymous"
            src="../assets/images/anonymous.png"
            alt="Anonymous"
            class="h-12 w-12 object-cover rounded-full"
          />
          <img
            v-else
            src="../assets/images/profile.jpg"
            alt="User Profile"
            class="h-12 w-12 object-cover rounded-full"
          />
          <div>
            <h2 class="text-lg font-semibold text-gray-800">
              <span v-if="question.is_anonymous">Anonymous User</span>
              <span v-else>
                {{ question.created_by.first_name }} {{ question.created_by.last_name }}
              </span>
            </h2>
            <p class="text-sm text-gray-500">{{ question.created_at_formated }}</p>
          </div>
        </div>

        <!-- Question Content -->
        <h1 class="text-3xl font-bold text-gray-800">{{ question.title }}</h1>
        <p class="text-gray-700 text-lg mt-4">{{ question.body }}</p>
      </div>

      <!-- Answers Section -->
      <div class="bg-white shadow-lg rounded-lg p-6 mt-8">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Answers</h2>
        <div v-if="question.answers && question.answers.length > 0" class="space-y-6">
          <div
            v-for="answer in question.answers"
            :key="answer.id"
            class="p-4 bg-gray-100 rounded-lg shadow-sm"
          >
            <!-- Answerer Info -->
            <div class="flex items-center space-x-4 mb-2">
              <img
                src="../assets/images/profile.jpg"
                alt="User Profile"
                class="h-12 w-12 object-cover rounded-full"
              />
              <div>
                <h3 class="text-md font-semibold text-gray-800">
                  <span class="text-xl font-bold text-gray-900">{{ answer.created_by.first_name }} {{ answer.created_by.last_name }} </span>
                  <p class="mt-1 text-gray-600">{{ answer.created_by.major }}, {{ answer.created_by.uni_id }}</p>
                </h3>
                <p class="text-md text-gray-500">{{ answer.created_at_formated }}</p>
              </div>
            </div>

            <!-- Answer Content -->
            <p class="text-gray-700">{{ answer.body }}</p>
          </div>
        </div>
        <div v-else class="text-gray-500">No answers yet. Be the first to answer!</div>
      </div>

      <!-- Add a Answer Section -->
      <div class="bg-white shadow-lg rounded-lg p-6 mt-8">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4">Add an Answer</h2>
        <textarea
          v-model="body"
          placeholder="Write your answer here..."
          class="w-full h-28 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
        ></textarea>
        <button
          @click="submitForm"
          class="mt-4 px-6 py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition"
        >
          Submit Answer
        </button>
      </div>
    </div>

    <!-- Error Case for Missing Question -->
    <div v-else class="text-center text-gray-500 mt-20">
      <p>Question not found or invalid ID.</p>
    </div>
  </div>
</template>