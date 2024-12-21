<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast';

export default {
    setup() {
        const toastStore = useToastStore();
        return { toastStore };
    },
    data() {
        return {
            currentYear: new Date().getFullYear(),
            form: {
                first_name: '',
                last_name: '',
                email: '',
                password1: '',
                password2: '',
                major: '',
                year: '',
                uni_id: '',
            },
            errors: [],
        };
    },
    methods: {
        submitForm() {
            this.errors = []
            if (!this.form.first_name) { this.errors.push('First name is required.'); }
            if (!this.form.last_name) { this.errors.push('Last name is required.'); }
            if (!this.form.email) { this.errors.push('Email is required.'); }
            if (!this.form.password1) { this.errors.push('Password is required.'); }
            if (!this.form.password2) { this.errors.push('Confirm password is required.'); }
            if (this.form.password1 !== this.form.password2) { this.errors.push('Passwords do not match.'); }
            if (!this.form.major) { this.errors.push('Major is required.'); }
            if (!this.form.year) { this.errors.push('Year is required.'); }
            if (!this.form.uni_id) { this.errors.push('Zewailcity ID is required.'); }
            if (this.errors.length === 0) {
                // console.log('form', this.form)
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered', 'bg-emerald-500')
                            this.form.first_name = ''
                            this.form.last_name = ''
                            this.form.email = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                            this.form.major = ''
                            this.form.year = ''
                            this.form.uni_id = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }
                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
};

</script>

<template>
    <!-- Background color -->
    <div
        class="absolute inset-x-0 -top-60 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-96"
        aria-hidden="true"
    >
    <div
        class="relative w-full h-[40rem] rotate-[30deg] bg-gradient-to-tr from-[#00b4d1] to-[#00a1b5] opacity-30"
        style="clip-path: polygon(72% 40%, 100% 60%, 95% 20%, 80% 0%, 70% 30%, 60% 60%, 50% 70%, 45% 60%, 40% 40%, 20% 80%, 0% 60%, 15% 100%, 25% 80%, 75% 100%, 72% 40%)"
    ></div>
    </div>
    <!-- end of background -->

    <div class=" min-h-screen flex flex-col justify-between">
        <!-- Main Content -->
        <div class="flex-grow flex items-center justify-center">
            <div class="bg-white w-full max-w-md p-6 rounded-lg shadow-lg">
                <div class="text-center">
                    <h1 class="text-4xl font-bold text-[#00b4d1]">Askit ZC</h1>
                    <h2 class="text-xl font-semibold mt-4">Create a new account</h2>
                </div>
                <form class="mt-6 space-y-4" v-on:submit.prevent="submitForm">

                    <!-- Name Fields -->
                    <div class="grid grid-cols-2 gap-4">
                    <input
                        type="text"
                        placeholder="First name"
                        v-model="form.first_name"
                        class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                    />
                    <input
                        type="text"
                        placeholder="Surname"
                        v-model="form.last_name"
                        class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                    />
                    </div>

                    <!-- ID field-->
                    <div>
                    <div class="flex space-x-2 mt-1">
                        <input
                        type="text"
                        placeholder="Zewailcity ID"
                        v-model="form.uni_id"
                        class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                        />
                    </div>
                    </div>

                    <!-- Major and Year Fields -->
                    <div class="grid grid-cols-2 gap-4">
                        <!-- Major Dropdown with Subfields -->
                        <select
                            v-model="form.major"
                            class="w-full px-4 py-3 text-gray-400 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                        >
                        <option value="" disabled selected class="text-gray-400">Major</option>
                        <optgroup label="CSAI">
                            <option value="DSAI">DSAI</option>
                            <option value="SWD">SWD</option>
                            <option value="IT">IT</option>
                            <!-- Add more subfields here -->
                        </optgroup>
                        <optgroup label="Engineering">
                            <option value="Aerospace">Aerospace </option>
                            <option value="CIE">CIE</option>
                            <option value="Environmental">Environmental</option>
                            <option value="Nano_ENG">Nano ENG</option>
                            <option value="Renewable">Renewable</option>
                            <!-- Add more subfields here -->
                        </optgroup>
                        <optgroup label="Science">
                            <option value="Biomedical">Biomedical </option>
                            <option value="Material">Material</option>
                            <option value="Physics">Physics</option>
                            <!-- Add more subfields here -->
                        </optgroup>
                        <optgroup label="Business">
                            <option value="Physics">Physics</option>
                            <option value="Biology">Biology</option>
                            <option value="Chemistry">Chemistry</option>
                            <!-- Add more subfields here -->
                        </optgroup>
                        </select>
                        <!-- Year Dropdown -->
                        <select
                        v-model="form.year"
                        class="w-full px-4 py-3 text-gray-400 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                        >
                        <option value="" disabled selected class="text-gray-400">Year</option>
                        <template v-for="year in currentYear - 2013 + 1" :key="year">
                            <option :value="2013 + year - 1">{{ 2013 + year - 1 }}</option>
                        </template>
                        </select>
                    </div>        

                    <!-- Email and Password Fields -->
                    <input
                        type="text"
                        placeholder="Email address"
                        v-model="form.email"
                        class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        v-model="form.password1"
                        class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                    />
                    <input
                        type="password"
                        placeholder="Confirm password"
                        v-model="form.password2"
                        class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                    />

                    <!-- Error Messages -->
                    <div v-if="errors.length > 0" class="mb-4">
                        <div v-for="error in errors" :key="error" class="text-red-500 text-sm font-semibold">
                            {{ error }}
                        </div>
                    </div>

                    <!-- Sign Up Button -->
                    <button
                        type="submit"
                        class="w-full bg-[#00b4d1] text-white font-medium py-3 rounded-md hover:bg-[#0097b3] transition"
                    >
                    Sign Up
                    </button>

                    <!-- Already Have Account -->
                    <p class="text-center text-sm text-gray-600 mt-4">
                    <RouterLink to="/" class="text-[#00b4d1] hover:underline">Already have an account?</RouterLink>
                    </p>
                    <hr class="my-6" />
                    <div>
                        <button
                            class="w-full flex items-center justify-center py-3 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#00b4d1] transition duration-200"
                        >
                            <img
                                src="/src/assets/icons/google-logo-png-open-2000.png"
                                alt="Google Icon"
                                class="w-5 h-5 mr-3"
                            />
                            Sign up with Google
                        </button>
                    </div>
                </form>
            </div>
        </div>
  
        <!-- Footer -->
        <footer class="py-4 text-gray-600 w-full">
        <div class="mt-4 text-center text-xs text-gray-500">
            <RouterLink to="/" class="hover:underline mx-2 text-[#00b4d1]">Sign In</RouterLink>
            <RouterLink to="/privacy" class="hover:underline mx-2 text-[#00b4d1]">Privacy</RouterLink>
            <RouterLink to="/terms" class="hover:underline mx-2 text-[#00b4d1]">Terms</RouterLink>
            <RouterLink to="/help" class="hover:underline mx-2 text-[#00b4d1]">Help</RouterLink>
        </div>
        <p class="mt-4 text-center text-xs text-gray-500">
            &copy; Askit ZC
        </p>
        </footer>

    </div>

  </template>