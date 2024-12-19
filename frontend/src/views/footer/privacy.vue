<script setup>
const privacyPolicy = [
  {
    title: "Data Collection",
    content:
      "We collect data when you create an account, use our services, and interact with the site. This includes personal information like name, email, and activity logs.",
  },
  {
    title: "Data Usage",
    content:
      "Your data is used to provide and improve our services. We never sell your information to third parties.",
  },
  {
    title: "Cookies",
    content:
      "We use cookies to enhance your browsing experience. You can manage your cookie preferences in your browser settings.",
  },
];
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <div class="max-w-4xl mx-auto px-6 py-12">
      <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Privacy Policy</h1>
      <p class="text-gray-600 mb-10">
        Your privacy is important to us. Below you'll find details about how we handle your information.
      </p>
      <div class="space-y-6">
        <div
          v-for="(section, index) in privacyPolicy"
          :key="index"
          class="bg-white shadow-lg rounded-lg p-6"
        >
          <h2 class="text-lg font-semibold text-gray-800">{{ section.title }}</h2>
          <p class="text-gray-600 mt-2">{{ section.content }}</p>
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
        <h1 class="text-4xl font-bold text-[#00b4d1] mb-6">Privacy Policy</h1>
        <p class="text-gray-600">
          Your privacy is important to us. This page outlines how we handle your personal information.
        </p>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Additional styles to match the website theme */
  </style> -->
  