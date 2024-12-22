<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useToastStore } from '@/stores/toast';

export default {
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
            questions: [],
            user: null,
            userVotes: {},
        };
    },

    mounted() {
        this.getFeed();
        this.fetchUserVotes();
    },

    watch: {
        '$route.params.id': {
            handler: function () {
                this.getFeed();
                this.fetchUserVotes();
            },
            deep: true,
            immediate: true,
        },
    },

    methods: {
        getFeed() {
            axios
                .get(`/api/questions/profile/${this.$route.params.id}/`)
                .then((response) => {
                    this.questions = response.data.questions;
                    this.user = response.data.user;
                })
                .catch((error) => {
                    console.error('Error fetching questions:', error);
                });
        },

        fetchUserVotes() {
            axios
                .get('/api/questions/votes/')
                .then((response) => {
                    response.data.forEach((vote) => {
                        this.userVotes[vote.question_id] = vote.type;
                    });
                })
                .catch((error) => {
                    console.error('Error fetching user votes:', error);
                });
        },

        toggleVote(questionId, type) {
            const currentVote = this.userVotes[questionId];

            if (currentVote === type) {
                this.removeVote(questionId);
            } else {
                this.castVote(questionId, type);
            }
        },

        castVote(questionId, type) {
            const endpoint = type === 'upvote' ? `/api/questions/${questionId}/upVotes/` : `/api/questions/${questionId}/downVotes/`;

            axios
                .post(endpoint)
                .then(() => {
                    this.userVotes[questionId] = type;
                    this.getFeed();
                })
                .catch((error) => {
                    console.error(`Error casting ${type} for question ${questionId}:`, error);
                });
        },

        removeVote(questionId) {
            axios
                .post(`/api/questions/${questionId}/removeVote/`)
                .then(() => {
                    delete this.userVotes[questionId]; 
                    this.getFeed();
                })
                .catch((error) => {
                    console.error(`Error removing vote for question ${questionId}:`, error);
                });
        },
    },
};
</script>

<template>
    <div class="space-y-6">
        <div
            v-for="question in questions"
            :key="question.id"
            class="bg-white shadow-lg rounded-lg p-4 space-y-4"
        >
            <!-- Post Header -->
            <div class="flex items-center space-x-4">
                <img
                    v-if="question.is_anonymous"
                    src="@/assets/images/anonymous.png"
                    alt="User Profile"
                    class="h-12 w-12 object-cover"
                />
                <img
                    v-else
                    src="@/assets/images/profile.jpg"
                    alt="User Profile"
                    class="h-12 w-12 rounded-full object-cover"
                />
                <div>
                    <h3 class="text-lg font-semibold text-gray-800">
                        <span v-if="question.is_anonymous">Anonymous User</span>
                        <span v-else>{{ question.created_by.first_name }} {{ question.created_by.last_name }}</span>
                    </h3>
                    <h6 class="text-sm font-semibold text-gray-600">
                        <span v-if="question.is_anonymous"></span>
                        <span v-else>{{ question.created_by.major }}, {{ question.created_by.year }}</span>
                    </h6>
                    <p class="text-sm text-gray-500">{{ question.created_at_formated }}</p>
                </div>
            </div>

            <!-- Post Title -->
            <h2 class="text-xl font-semibold text-gray-900">{{ question.title }}</h2>

            <!-- Post Content -->
            <p class="text-gray-700">{{ question.body }}</p>

            <hr class="mt-4 mb-3" />

            <!-- Post Footer -->
            <div class="flex items-center justify-between text-gray-500 text-sm">
                <!-- Upvote Button -->
                <button
                    :class="{
                        'bg-blue-100': userVotes[question.id] === 'upvote',
                    }"
                    class="flex items-center bg-white px-3 py-1.5 rounded-md hover:bg-gray-200 transition-all"
                    @click="toggleVote(question.id, 'upvote')"
                >
                    <img
                        src="/src/assets/Icons/Upvote.png"
                        alt="UpVote Icon"
                        class="h-5 w-5 mr-2"
                    />
                    {{ question.upvotes_count }} UpVotes
                </button>

                <!-- Center Column (Answers Placeholder) -->
                <div>
                    <button
                        class="flex items-center bg-white px-3 py-1.5 rounded-md hover:bg-gray-200 transition-all"
                    >
                        <img
                            src="/src/assets/Icons/answer.png"
                            alt="Answers Icon"
                            class="h-5 w-5 mr-2"
                        />
                        {{ question.answers_count || 0 }} Answers
                    </button>
                </div>

                <!-- Downvote Button -->
                <button
                    :class="{
                        'bg-red-100': userVotes[question.id] === 'downvote',
                    }"
                    class="flex items-center bg-white px-3 py-1.5 rounded-md hover:bg-gray-200 transition-all"
                    @click="toggleVote(question.id, 'downvote')"
                >
                    <img
                        src="/src/assets/Icons/downvote.png"
                        alt="DownVote Icon"
                        class="h-5 w-5 mr-2"
                    />
                    {{ question.downvotes_count }} DownVotes
                </button>
            </div>
        </div>

        <!-- No Posts Found -->
        <div v-if="questions.length === 0" class="text-gray-500 text-center">
            <p>No posts yet. Be the first to post!</p>
        </div>
    </div>
</template>
