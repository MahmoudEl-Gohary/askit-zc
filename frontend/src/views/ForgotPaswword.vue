<template>
    <div>
      <h2>Forgot Password</h2>
      <form @submit.prevent="sendResetEmail">
        <input type="email" v-model="email" placeholder="Enter your email" />
        <button type="submit">Send Reset Link</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        message: '',
      };
    },
    methods: {
      async sendResetEmail() {
        try {
          const response = await fetch('http://localhost:8000/password-reset/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: this.email }),
          });
          if (response.ok) {
            this.message = 'Password reset link sent to your email.';
          } else {
            this.message = 'Failed to send reset email. Please try again.';
          }
        } catch (error) {
          console.error(error);
          this.message = 'An error occurred.';
        }
      },
    },
  };
  </script>
  