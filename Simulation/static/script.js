let scale = 1; 

document.getElementById('treeForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/generate_tree', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const img = URL.createObjectURL(blob);
        document.getElementById('treeImage').src = img;
    });
});

document.getElementById('download_positions_csv').addEventListener('click', function(e) {
    e.preventDefault();
    const formData = new FormData(document.getElementById('treeForm'));
    fetch('/download_positions_csv', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'node_positions.csv';
        link.click();
    });
});

document.getElementById('download_heuristics_csv').addEventListener('click', function(e) {
    e.preventDefault();
    const formData = new FormData(document.getElementById('treeForm'));
    fetch('/download_heuristics_csv', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'heuristics.csv';
        link.click();
    });
});

// Zoom functionality
document.getElementById('zoomIn').addEventListener('click', function() {
    scale += 0.1; 
    document.getElementById('treeImage').style.transform = `scale(${scale})`;
});

document.getElementById('zoomOut').addEventListener('click', function() {
    scale = Math.max(1, scale - 0.1); 
    document.getElementById('treeImage').style.transform = `scale(${scale})`;
});

// Mouse scroll zoom functionality
const imageContainer = document.getElementById('treeImageContainer');
imageContainer.addEventListener('wheel', function(event) {
    event.preventDefault();
    if (event.deltaY < 0) {
        scale += 0.1; 
    } else {
        scale = Math.max(1, scale - 0.1);
    }
    document.getElementById('treeImage').style.transform = `scale(${scale})`;
});


document.getElementById('download_image').addEventListener('click', function() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const img = document.getElementById('treeImage');

    canvas.width = img.width;
    canvas.height = img.height;

    ctx.drawImage(img, 0, 0, img.width, img.height);

    canvas.toBlob(function(blob) {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'tree_visualization.png'; 
        link.click();
    });
});
