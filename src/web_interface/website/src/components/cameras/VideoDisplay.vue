<template>
    <div class="background">
        <DragItem
            v-for="(stream, index) in streams"
            :key="stream.data.id"
            :extraData="{ ...stream.data, removeIndex: index }"
        >
            <VideoStream
                :host="host"
                :stream="stream"
                :peer="peers[stream.data.topic]"
            />
        </DragItem>
        <div v-if="streams.length === 0" class="centered">
            Drag some streams here!
        </div>
    </div>
</template>
<script>
import layoutToCoords from '@/components/cameras/layoutToCoords'
import DragItem from '@/components/cameras/DragItem.vue'
import VideoStream from '@/components/cameras/VideoStream.vue'
export default {
    components: { DragItem, VideoStream },
    props: {
        host: String, // should be a global
        layout: Object,
        peers: Object,
        rect: Object,
    },

    computed: {
        streams() {
            return layoutToCoords(this.layout, this.rect)
        },
    },
}
</script>
<style scoped>
.background {
    background-color: lightgray;
    height: 100%;
}
.centered {
    margin: 0 auto;
    padding-top: 10vh;
}
</style>
