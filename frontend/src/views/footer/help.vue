<script setup>
const faqs = [
  {
    question: "How do I reset my password?",
    answer:
      "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions.",
  },
  {
    question: "How do I contact support?",
    answer:
      "You can contact support via email at support@example.com or by using the contact form on the 'Contact' page.",
  },
  {
    question: "Can I delete my account?",
    answer:
      "Yes, you can delete your account by navigating to the account settings and selecting 'Delete Account'.",
  },
];
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <div class="max-w-4xl mx-auto px-6 py-12">
      <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Help & Support</h1>
      <p class="text-gray-600 mb-10">
        Have questions? We've got answers. Check out our FAQs below or contact support for more assistance.
      </p>
      <div class="space-y-6">
        <div
          v-for="(faq, index) in faqs"
          :key="index"
          class="bg-white shadow-lg rounded-lg p-6"
        >
          <h2 class="text-lg font-semibold text-gray-800">{{ faq.question }}</h2>
          <p class="text-gray-600 mt-2">{{ faq.answer }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Additional styles to match the website theme */
</style>

<!-- 


<template>
    <div class="min-h-screen bg-gray-50">
      <div class="max-w-4xl mx-auto px-6 py-12">
        <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Help & Support</h1>
        <p class="text-gray-600">
          If you have any questions or need assistance, please contact our support team or check our FAQs.
        </p>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Additional styles to match the website theme */
  </style>
   -->
