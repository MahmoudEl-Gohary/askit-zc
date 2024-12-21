<script>
import Header from '@/components/Header.vue';

export default {
  name: 'AdminDashboard',

  components: {
    Header,
  },

  data() {
    return {
      questions: [
        {
          id: 1,
          title: 'How to learn Vue.js?',
          created_by: { first_name: 'John', last_name: 'Doe' },
          created_at_formated: '2023-12-01 10:30 AM',
          is_anonymous: false,
        },
        {
          id: 2,
          title: 'What is the best JavaScript framework?',
          created_by: { first_name: 'Jane', last_name: 'Smith' },
          created_at_formated: '2023-11-28 03:15 PM',
          is_anonymous: false,
        },
        {
          id: 3,
          title: 'Tips for becoming a full-stack developer?',
          created_by: { first_name: '', last_name: '' },
          created_at_formated: '2023-12-02 08:45 AM',
          is_anonymous: true,
        },
      ],
    };
  },

  methods: {
    deleteQuestion(id) {
      if (confirm('Are you sure you want to delete this question?')) {
        console.log(`Deleting question with ID: ${id}`);
        this.questions = this.questions.filter((q) => q.id !== id); // Remove the question from the list
      }
    },
  },
};
</script>

<template>
  <div>
    <!-- Header -->
    <Header />

    <!-- Dashboard Content -->
    <div class="max-w-7xl mx-auto px-6 py-12 bg-gray-50">
      <h1 class="text-4xl font-bold text-[#00b4d1] mb-8">Admin Dashboard</h1>
      <p class="text-gray-600 mb-6">
        Manage all posts from users. You can view, delete, or take necessary actions.
      </p>

      <!-- Questions Table -->
      <div class="bg-white shadow-lg rounded-lg overflow-hidden">
        <table class="min-w-full border-collapse">
          <thead>
            <tr class="bg-gray-100 border-b">
              <th class="px-6 py-3 text-left text-sm font-semibold text-gray-600">#</th>
              <th class="px-6 py-3 text-left text-sm font-semibold text-gray-600">Title</th>
              <th class="px-6 py-3 text-left text-sm font-semibold text-gray-600">User</th>
              <th class="px-6 py-3 text-left text-sm font-semibold text-gray-600">Created At</th>
              <th class="px-6 py-3 text-left text-sm font-semibold text-gray-600">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(question, index) in questions"
              :key="question.id"
              class="border-b hover:bg-gray-50"
            >
              <td class="px-6 py-4 text-sm text-gray-800">{{ index + 1 }}</td>
              <td class="px-6 py-4 text-sm text-gray-800">{{ question.title }}</td>
              <td class="px-6 py-4 text-sm text-gray-800">
                <span v-if="question.is_anonymous">Anonymous</span>
                <span v-else>{{ question.created_by.first_name }} {{ question.created_by.last_name }}</span>
              </td>
              <td class="px-6 py-4 text-sm text-gray-800">{{ question.created_at_formated }}</td>
              <td class="px-6 py-4 text-sm">
                <button
                  @click="deleteQuestion(question.id)"
                  class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition"
                >
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- No Questions Found -->
      <div v-if="questions.length === 0" class="text-center text-gray-500 mt-6">
        <p>No posts available.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Add any custom styles if needed */
</style>
