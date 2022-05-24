<template>
    <div class="max-h-42 max-w-sm rounded-md">
        <video id="video" height="50" width="350" autoplay class="rounded-lg" />
        <div class="flex items-center justify-center p-4 bg-white">
            <button id="close" class="mt-4 mb-4 h-12 w-36 text-lg text-white bg-red-600 rounded-full">Fechar camera</button>
            <button @click="startCamera()" class="mt-4 ml-6 mb-4 h-12 w-32 text-lg text-white bg-green-600 rounded-full">Abrir camera</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Camera',
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
