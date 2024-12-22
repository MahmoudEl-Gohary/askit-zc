<!-- create_question.vue -->
<script setup>
    import { ref, computed } from 'vue';
    import { useQuestionsStore } from '@/stores/questions';

    const title = ref('');
    const body = ref('');
    const is_anonymous = ref(false);

    const questionsStore = useQuestionsStore();

    const profileImage = computed(() => {
        return is_anonymous.value
            ? '/src/assets/images/anonymous.png'
            : '/src/assets/images/profile.jpg';
    });

    async function submitForm() {
        try {
            await questionsStore.addQuestion(title.value, body.value, is_anonymous.value);
            title.value = '';
            body.value = '';
            is_anonymous.value = false;
        } catch (error) {
            console.error('Error submitting question:', error);
        }
    }
</script>

<template>
    <form @submit.prevent="submitForm" class="bg-white shadow-lg rounded-lg p-6 mb-8">
        <div class="flex items-start space-x-4">
            <!-- User Image -->
            <img
                :src="profileImage"
                alt="User Profile"
                class="h-12 w-12 rounded-full object-cover"
            />

            <!-- Post Input -->
            <div class="flex-1">
                <input
                    type="text"
                    v-model="title"
                    placeholder="Title"
                    class="w-full p-3 mb-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                />

                <textarea
                    v-model="body"
                    placeholder="What's on your mind?"
                    class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-[#00b4d1] focus:outline-none"
                    rows="2"
                ></textarea>

                <div class="mt-4 flex justify-between">
                    <!-- Post Button (Left) -->
                    <button
                        type="submit"
                        class="bg-[#00b4d1] text-white px-14 py-2 rounded-md hover:bg-[#0097b3] transition-all"
                    >
                        Post
                    </button>

                    <!-- Anonymous Checkbox (Right) -->
                    <label class="flex items-center space-x-3 text-gray-700 cursor-pointer">
                        <input
                            type="checkbox"
                            v-model="is_anonymous"
                            class="w-5 h-5 border-2 border-gray-300 rounded-md focus:outline-none"
                        />
                        <span class="flex items-center space-x-2">
                            <img
                                src="/src/assets/Icons/anonymous.png"
                                alt="Anonymous Icon"
                                class="h-6 w-6"
                            />
                            <span>Post Anonymously</span>
                        </span>
                    </label>
                </div>
            </div>
        </div>
    </form>
</template>
