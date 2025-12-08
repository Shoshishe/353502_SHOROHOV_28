const rect = document.getElementById('rect')
const frames = [
    {
        scale: 0.25,
        offset: 0
    },
    {
        scale: 0.5,
        offset: 0.3
    },
    {
        scale: 1,
        offset: 0.6
    },
    {
        scale: 2,
        offset: 1
    }
]
const config = {
    duration: 600,
    easing: 'ease-in-out',
    iterations: Infinity,
    direction: 'alternate'
}

const animation = rect.animate(frames, config)

document.getElementById('pause').addEventListener('click', () => animation.pause())
document.getElementById('play').addEventListener('click', () => animation.play())
document.getElementById('cancel').addEventListener('click', () => animation.cancel())
document.getElementById('faster').addEventListener('click', () => (animation.playbackRate *= 2))
document.getElementById('slower').addEventListener('click', () => (animation.playbackRate /= 2))