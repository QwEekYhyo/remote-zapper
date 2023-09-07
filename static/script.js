const volumeUpButton = document.getElementById("up");
const volumeDownButton = document.getElementById("down");
const resetVolumeButton = document.getElementById("reset");

async function increaseVolume() {
    const response = await fetch("/volume?turn=up");
    console.log(await response.json());
}

async function decreaseVolume() {
    const response = await fetch("/volume?turn=down");
    console.log(await response.json());
}

async function resetVolume() {
    const response = await fetch("/reset");
    console.log(await response.json());
}

volumeUpButton.addEventListener("click", increaseVolume)
volumeDownButton.addEventListener("click", decreaseVolume)
resetVolumeButton.addEventListener("click", resetVolume)
