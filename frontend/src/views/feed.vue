<script setup>
    import Header from '@/components/Header.vue';
    import CreateQuestion from '@/components/create_question.vue';
    import Questions from '@/components/questions.vue';
</script>

<template>
    <div class="min-h-screen bg-gray-50">
        <Header />
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <CreateQuestion />
            <Questions />
        </div>
    </div>
</template>
