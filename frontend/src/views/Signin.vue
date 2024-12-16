<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast';

export default {

    setup() {
        const userStore = useToastStore();
        return { userStore };
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        };
    },

    methods: {
        async submitForm() {
            this.errors = []
            if (this.form.email === '') { this.errors.push('Your e-mail is missing') }
            if (this.form.password === '') { this.errors.push('Your password is missing') }
            if (this.errors.length === 0) {
                console.log('form', this.form)
                // await axios
                //     .post('/api/login/', this.form)
                //     .then(response => {
                //         this.userStore.setToken(response.data)
                //         axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                //     })
                //     .catch(error => {
                //         console.log('error', error)
                //         this.errors.push('The email or password is incorrect!')
                //     })
            }

            if (this.errors.length === 0) {
                // await axios
                //     .get('/api/me/')
                //     .then(response => {
                //         this.userStore.setUserInfo(response.data)
                //         this.$router.push('/feed')
                //     })
                //     .catch(error => {
                //         console.log('error', error)
                //     })
            }
        }
    }
}
</script>
<template>
    <!-- Background color -->
    <div
        class="absolute inset-x-0 -top-60 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-96"
        aria-hidden="true"
    >
    <div
        class="relative left-[calc(50%-15rem)] aspect-[1155/678] w-[50rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#00b4d1] to-[#00a1b5] opacity-30 sm:left-[calc(50%-40rem)] sm:w-[90rem]"
        style="clip-path: polygon(72% 40%, 100% 60%, 95% 20%, 80% 0%, 70% 30%, 60% 60%, 50% 70%, 45% 60%, 40% 40%, 20% 80%, 0% 60%, 15% 100%, 25% 80%, 75% 100%, 72% 40%)"
    ></div>
    </div>
    <!-- end of background -->

  <div class="min-h-screen flex flex-col items-center justify-between">
        <!-- Main Content -->
        <div class="flex flex-col sm:flex-row items-center sm:justify-center w-full sm:w-4/5 max-w-6xl mt-20 sm:mt-40">

            <!-- Left Section -->
            <div class="text-center sm:text-left sm:w-1/2 px-4">
                <h1 class="text-5xl font-bold text-[#00b4d1]">Askit ZC</h1>
                <p class="mt-4 text-lg text-gray-700 leading-relaxed">
                    Dive into dynamic discourse that fuels curiosity, connects peers, and expands horizons at Zewail City. Your thoughts matter here!
                </p>
            </div>
            <!-- End of the left section -->

            <!-- Right Section (Login Form) -->
            <div class="mt-8 sm:mt-0 sm:w-1/3 sm:ml-10">
                <div class="bg-white p-6 rounded-lg shadow-md">

                    <!-- form section -->
                    <form class="space-y-4" v-on:submit.prevent="submitForm">
                        <input
                            type="email"
                            placeholder="Email address"
                            v-model="form.email"
                            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00b4d1]"
                        />
                        <input
                            type="password"
                            placeholder="Password"
                            v-model="form.password"
                            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00b4d1]"
                        />

                        <!-- Error Messages -->
                        <div v-if="errors.length > 0" class="mb-4">
                            <div v-for="error in errors" :key="error" class="text-red-500 text-sm font-semibold">
                                {{ error }}
                            </div>
                        </div>

                        <button
                            class="w-full py-3 px-4 bg-[#00b4d1] text-white rounded-lg font-medium hover:bg-[#0097b3] transition"
                        >
                            Log in
                        </button>
                    </form>
                    <!-- end of form section -->

                    <!-- Forgot password -->
                    <a
                        href="#"
                        class="block mt-4 text-[#00b4d1] text-sm text-center hover:underline"
                    >
                        Forgotten password?
                    </a>

                    <hr class="my-6" />

                    <!-- Sign in with google -->
                    <div>
                        <button
                            class="w-full flex items-center justify-center py-3 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-[#00b4d1] transition duration-200"
                        >
                            <img
                                src="/src/assets/icons/google-logo-png-open-2000.png"
                                alt="Google Icon"
                                class="w-5 h-5 mr-3"
                            />
                            Sign in with Google
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="w-full py-4 text-gray-600">
            <div class="mt-4 text-center text-xs text-gray-500">
                <RouterLink to="/signup" class="hover:underline mx-2 text-[#00b4d1]">Sign Up</RouterLink>
                <a href="#" class="hover:underline mx-2 text-[#00b4d1]">Privacy</a>
                <a href="#" class="hover:underline mx-2 text-[#00b4d1]">Terms</a>
                <a href="#" class="hover:underline mx-2 text-[#00b4d1]">Help</a>
            </div>
                <p class="mt-4 text-center text-xs text-gray-500">
                &copy; Askit ZC
            </p>
        </footer>

    </div>
</template>
