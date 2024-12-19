<script setup>
const terms = [
  {
    title: "Acceptance of Terms",
    content:
      "By using our services, you agree to comply with and be bound by these terms. If you do not agree, please do not use our services.",
  },
  {
    title: "User Responsibilities",
    content:
      "Users are responsible for keeping their account information secure and for all activities that occur under their account.",
  },
  {
    title: "Termination",
    content:
      "We reserve the right to suspend or terminate accounts that violate our policies or engage in unlawful activities.",
  },
];
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <div class="max-w-4xl mx-auto px-6 py-12">
      <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Terms & Conditions</h1>
      <p class="text-gray-600 mb-10">
        Please read these terms and conditions carefully before using our services.
      </p>
      <div class="space-y-6">
        <div
          v-for="(term, index) in terms"
          :key="index"
          class="bg-white shadow-lg rounded-lg p-6"
        >
          <h2 class="text-lg font-semibold text-gray-800">{{ term.title }}</h2>
          <p class="text-gray-600 mt-2">{{ term.content }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Additional styles to match the website theme */
</style>






<!-- <template>
    <div class="min-h-screen bg-gray-50">
      <div class="max-w-4xl mx-auto px-6 py-12">
        <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Terms & Conditions</h1>
        <p class="text-gray-600">
          Please review our terms and conditions carefully before using our services.
        </p>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Additional styles to match the website theme */
  </style> -->
  