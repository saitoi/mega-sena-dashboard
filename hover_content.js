function setupHover(elementId, messageElementId) {
    let element = document.getElementById(elementId);
    let messageElement = document.getElementById(messageElementId);

    element.addEventListener('mouseover', function() {
        messageElement.style.display = 'block';
    });

    element.addEventListener('mouseout', function() {
        messageElement.style.display = 'none';
    });
}

setupHover('mean-prizes', 'hover-message');
setupHover('countour-map', 'hover-message2');
