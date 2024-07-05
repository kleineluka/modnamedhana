/* Listen to which install type is currently selected */
document.addEventListener('DOMContentLoaded', () => {
    const copyGameButton = document.getElementById('copy-game');
    const patchGameButton = document.getElementById('patch-game');

    copyGameButton.addEventListener('click', () => {
        copyGameButton.classList.add('selected');
        patchGameButton.classList.remove('selected');
    });

    patchGameButton.addEventListener('click', () => {
        patchGameButton.classList.add('selected');
        copyGameButton.classList.remove('selected');
    });
});
