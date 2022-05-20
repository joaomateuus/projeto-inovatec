<template>
    <div>
        <video id="video" autoplay />
    </div>
</template>

<script>
export default {
    name: 'Camera',
    methods: {
        startCamera() {
            navigator.mediaDevices
            .getUserMedia({video:true, width:1000})
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
