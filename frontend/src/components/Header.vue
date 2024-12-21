<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

// Simulate user login state and data
const isLoggedIn = ref(false);
const userName = ref("John Doe");

const logout = () => {
  isLoggedIn.value = false;
  userName.value = "";
};
</script>

<template>
  <header class="bg-gradient-to-r from-[#00b4d1] to-[#00a1b5] sticky top-0 z-50 shadow-lg">
    <div class="container mx-auto flex items-center justify-between px-6 py-4 max-w-screen-xl">
      <!-- Logo Section -->
      <div class="flex items-center space-x-3">
        <RouterLink to="/">
          <div class="flex items-center space-x-3 cursor-pointer">
            <img src="../assets/Icons/header.png" alt="Logo" class="h-12 w-12" />
            <span class="text-3xl font-semibold text-white tracking-tight">askit.zc</span>
          </div>
        </RouterLink>
      </div>

      <!-- Navigation Links -->
      <nav class="flex items-center space-x-6">
        <RouterLink to="/Feed" class="text-white hover:text-[#fff2f2] cursor-pointer transition-all duration-300">
          Feed
        </RouterLink>
        <RouterLink to="/profile" class="text-white hover:text-[#fff2f2] cursor-pointer transition-all duration-300">
          Profile
        </RouterLink>
        <RouterLink to="/feed" class="text-white hover:text-[#fff2f2] cursor-pointer transition-all duration-300">
          Search
        </RouterLink>

          <RouterLink to="/signin">
            <button
              class="bg-[#00b4d1] text-white hover:bg-[#0099b3] rounded-lg px-6 py-2 font-medium transition-all duration-300 transform hover:scale-105 shadow-lg"
            >
              Sign Out
            </button>
          </RouterLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
/* Typography and Styling */
.font-space-grotesk {
  font-family: 'Space Grotesk', sans-serif;
}

/* Header Background with Linear Gradient */
header {
  background: linear-gradient(90deg, #00b5d1 0%, #00b5d191 100%); /* Gradient from cyan to a softer blue */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  border-bottom: 1px solid rgba(255, 255, 255, 0.1); /* Light transparent border */
}

/* Links Styling */
a {
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  transition: color 0.3s ease-in-out;
}

a:hover {
  color: #fff2f29a; /* Light off-white color on hover */
}

/* Action Button Styling */
button {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 1px;
  padding: 0.75rem 1.5rem;
  background-color: #00b4d1; /* Cyan button color */
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Soft shadow */
  transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}

button:hover {
  background-color: #0099b3; /* Darker cyan on hover */
  transform: translateY(-3px); /* Slight lift on hover */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* More shadow on hover */
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  nav {
    display: none; /* Hide desktop menu */
  }

  .md:hidden {
    display: flex; /* Show mobile hamburger icon */
  }
}
</style>