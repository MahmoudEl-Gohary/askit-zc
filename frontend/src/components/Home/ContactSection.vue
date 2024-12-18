<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const message = ref('')

const handleSubmit = () => {
  // Handle form submission
  console.log({ email: email.value, message: message.value })
}
</script>

<template>
  <section id="contact" class="py-20 bg-white">
    <div class="container mx-auto px-4 max-w-2xl">
      <h2 class="text-4xl font-bold text-[#00b4d1] text-center mb-12 tracking-tight">Get in Touch</h2>
      <form @submit.prevent="handleSubmit" class="space-y-8 backdrop-blur-sm bg-white/5 p-8 rounded-2xl shadow-xl">
        <div>
          <input
            v-model="email"
            type="email"
            placeholder="Your Email"
            class="w-full px-6 py-4 rounded-xl bg-white/10 border-2 border-[#00b4d1] focus:border-[#0099b3] text-black placeholder-gray-400 transition-all duration-300"
          />
        </div>
        <div>
          <textarea
            v-model="message"
            rows="4"
            placeholder="Your Message"
            class="w-full px-6 py-4 rounded-xl bg-white/10 border-2 border-[#00b4d1] focus:border-[#0099b3] text-black placeholder-gray-400 transition-all duration-300"
          ></textarea>
        </div>
        <button
          type="submit"
          class="w-full px-8 py-4 bg-[#00b4d1] text-white rounded-xl hover:bg-[#0099b3] transform hover:scale-[1.02] transition-all duration-300 font-semibold shadow-lg"
        >
          Send Message
        </button>
      </form>
    </div>
  </section>
</template>