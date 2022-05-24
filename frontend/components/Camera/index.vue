<template>
    <div>
        <video id="video" height="200" width="350" autoplay />
    </div>
</template>

<script>
export default {
    name: 'Camera',
    methods: {
        startCamera() {
            navigator.mediaDevices
            .getUserMedia({video:true})
            .then(stream => {
                const videoElement = document.querySelector('#video');
                videoElement.srcObject = stream;
            }).catch(error => {
            alert("Browser doesn't support or there is some errors." + error);
        });
        }
    },
    mounted() {
        this.startCamera();
    }
    
}
</script>

<style />
