// src/stores/questions.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useQuestionsStore = defineStore('questions', {
  state: () => ({
    questions: []
  }),

  actions: {
    async fetchQuestions() {
      try {
        const response = await axios.get('/api/questions/');
        this.questions = response.data;
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    },

    async addQuestion(title, body, is_anonymous) {
      try {
        const response = await axios.post('/api/questions/create/', {
          title,
          body, 
          is_anonymous
        });
        this.questions.unshift(response.data);
      } catch (error) {
        console.error('Error adding question:', error);
      }
    }
  }
});
