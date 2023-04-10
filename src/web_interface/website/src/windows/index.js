import TestWindow from './TestWindow.vue'
import CameraWindow from './CameraWindow.vue'
import ControlWindow from './ControlWindow.vue'
import { useGstreamerStore } from '@/stores'

export default {
    testWindow: {
        typeName: 'Test Window',
        component: TestWindow,
        configOptions: {
            videoSource: {
                name: 'Video Source',
                type: 'select',
                possibleValues: () => {
                    const gstreamerStore = useGstreamerStore()
                    return Object.keys(gstreamerStore.peers)
                },
            },
            textTest: {
                name: 'Text test',
                type: 'text',
            },
            numberTest: {
                name: 'Number test',
                type: 'number',
            },
            rangeTest: {
                name: 'Range test',
                type: 'range',
                range: () => ({ min: -0.2, max: 5, step: 0.1 }),
            },
            aaaa: {
                name: 'AAAAA',
                type: 'range',
                range: () => ({ min: -0.2, max: 5, step: 0.1 }),
            },
            bbbb: {
                name: 'BBBBBB',
                type: 'boolean',
            },
        },
        icon: 'mdi-camera',
    },
    cameraWindow: {
        typeName: 'Camera Window',
        component: CameraWindow,
        configOptions: {
            videoSource: {
                name: 'Video Source',
                type: 'select',
                possibleValues: () => {
                    const gstreamerStore = useGstreamerStore()
                    return Object.keys(gstreamerStore.peers)
                },
            },
        },
        icon: 'mdi-camera',
    },
    controlWindow: {
        typeName: 'Control Window',
        component: ControlWindow,
        configOptions: {
            controlledObject: {
                name: 'Controlled Object',
                type: 'select',
                possibleValues: () => {
                    return ['Rover', 'Manipulator']
                },
            },
            controlMode: {
                name: 'Control Mode',
                type: 'select',
                possibleValues: () => {
                    return ['Keyboard', 'Touch']
                },
            },
            movementStrategy: {
                name: 'Movement Strategy',
                type: 'select',
                possibleValues: () => {
                    return ['Position', 'Velocity']
                },
            },
            maxLinearSpeed: {
                name: 'Max Linear Velocity [m/s]',
                type: 'number',
            },
            maxAngularSpeed: {
                name: 'Max Angular Velocity [rad/s]',
                type: 'number',
            },
        },
        icon: 'mdi-controller',
    },
}
