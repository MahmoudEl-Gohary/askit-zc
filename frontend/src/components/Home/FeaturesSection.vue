<script setup lang="ts">
import { AcademicCapIcon, UserGroupIcon, BellAlertIcon } from '@heroicons/vue/24/outline'

const features = [
  {
    icon: AcademicCapIcon,
    title: 'Explore Academics Effortlessly',
    description: 'Find answers to academic inquiries quickly and easily. Connect with your peers.'
  },
  {
    icon: UserGroupIcon,
    title: 'Engage Socially Instantly',
    description: 'Connect with peers. Share experiences and grow together socially and academically.'
  },
  {
    icon: BellAlertIcon,
    title: 'Stay Updated',
    description: 'Get real-time notifications for answers and discussions that matter to you.'
  }
]
</script>

<template>
  <section id="features" class="py-20 bg-white">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div v-for="feature in features" :key="feature.title" class="bg-white p-6 rounded-xl shadow-lg">
          <div class="w-12 h-12 rounded-full flex items-center justify-center mb-4">
            <component :is="feature.icon" class="w-6 h-6 text-[#00b4d1]" />
          </div>
          <h3 class="text-xl font-bold text-[#00b4d1]">{{ feature.title }}</h3>
          <p class="text-gray-600">{{ feature.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>