<template>
    <div class="h-fit max-w-sm rounded-md">
        <video id="video" autoplay class="rounded-lg" />
        <div class="flex items-center justify-between p-4 bg-white rounded-md">
            <button @click="startCamera()" class="mt-4 ml-6 mb-4 h-12 w-32 text-lg text-white bg-green-600 rounded-full">
                <v-icon>mdi-camera</v-icon>
            </button>
            <button id="close" class="mt-4 mb-4 h-12 w-36 text-lg text-white bg-red-600 rounded-full">
                <v-icon>mdi-camera-off</v-icon>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Camera',
    data: () => ({
        constraints: {
            video: {
                height: {
                    min: 1280,
                    ideal: 1920,
                    max: 2560
                },
                width: {
                    min: 720,
                    ideal: 1080,
                    max: 1440
                },
                facingMode: {
                    exact: 'environment'
                }
            }
        }
    }),
    methods: {
        startCamera() {
            navigator.mediaDevices
            .getUserMedia({video:true, facingMode: {exact: 'environment'}})
            .then(stream => {
                const videoElement = document.querySelector('#video');
                videoElement.srcObject = stream;

                const closeCam = document.querySelector('#close');
                closeCam.addEventListener('click', ((ev)=>{
                    stream.getVideoTracks()[0].stop();
                    video.src='';
                }))
            }).catch(error => {
                alert("Browser doesn't support or there is some errors." + error);
            });
        },
    },
    mounted() {
        this.startCamera();
    }
    
}
</script>

<style />