<template>
    <n-message-provider>
        <NLoadingBarProvider>
            <RouterLink to="/"></RouterLink>
            <RouterView></RouterView>
        </NLoadingBarProvider>

    </n-message-provider>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { NMessageProvider, NLoadingBarProvider } from 'naive-ui'
</script>
