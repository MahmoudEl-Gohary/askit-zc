<script>
    import Header from '../components/Header.vue';
    import UserQuestion from '@/components/Profile/UserQuestion.vue';
    import { useUserStore } from '@/stores/user';
    import { useToastStore } from '@/stores/toast';
    import axios from 'axios';

    export default {
        name: 'ProfileView',

        components: {
            Header,
            UserQuestion,
        },

        setup() {
            const userStore = useUserStore();
            const toastStore = useToastStore();

            return {
                userStore,
                toastStore,
            };
        },

        data() {
            return {
                user: {
                    id: '',
                    first_name: '',
                    last_name: '',
                    email: '',
                    uni_id: '',
                    major: '',
                    year: '',
                },
            };
        },

        props: {
            id: {
                type: String,
                required: true,
            },
        },

        mounted() {
            this.getUserInfo();
        },

        watch: {
            id: {
                handler(newId) {
                    this.getUserInfo(newId);
                },
                immediate: true,
            },
        },

        methods: {
            getUserInfo() {
                axios
                    .get(`/api/user/${this.id}/`)
                    .then((response) => {
                        this.user = response.data;
                    })
                    .catch((error) => {
                        console.error('Failed to fetch user data:', error);
                    });
            },
        },
    };
</script>

<template>
    <Header />

    <div class="min-h-screen bg-gray-50">
        <!-- Cover Photo -->
        <div class="relative h-48 md:h-64">
            <img
                src="/src/assets/images/profile.jpg"
                alt="Cover"
                class="w-full h-full object-cover"
            />
        </div>

        <!-- Profile Info -->
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="relative -mt-12 sm:-mt-16">
                <div class="flex flex-col sm:flex-row items-center sm:items-center sm:space-x-5 m-5 p-3">
                    <!-- Profile Picture -->
                    <div class="relative">
                        <img
                            src="/src/assets/images/anonymous.png"
                            alt="Profile"
                            class="h-24 w-24 sm:h-32 sm:w-32 rounded-full border-4 border-white shadow-lg"
                        />
                    </div>

                    <!-- Profile Details -->
                    <div class="mt-4 sm:mt-0 text-center sm:text-left">
                        <h1 class="text-2xl font-bold text-gray-900">{{ user.first_name }} {{ user.last_name }}</h1>
                        <p class="mt-1 text-gray-600">{{ user.major }}, {{ user.uni_id }}</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- User Questions -->
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <UserQuestion :id="user.id" />
        </div>
    </div>
</template>