const dropZone = document.getElementById('drop-zone');
const loadingState = document.getElementById('loading-state');
const resultContainer = document.getElementById('result-container');
const outputText = document.getElementById('output-text');
const resetBtn = document.getElementById('reset-btn');
const copyBtn = document.getElementById('copy-btn');
console.log("Fichier en cours de lecture...");
['dragenter', 'dragover'].forEach(name => {
    dropZone.addEventListener(name, (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });
});

['dragleave', 'drop'].forEach(name => {
    dropZone.addEventListener(name, (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
    });
});

dropZone.addEventListener('drop', (e) => {
    const file = e.dataTransfer.files[0];
    if (!file) return;

    dropZone.classList.add('hidden');
    loadingState.classList.remove('hidden');

    const reader = new FileReader();

    reader.onload = async (event) => {
        let base64Data = event.target.result.split(',')[1];
        let mimeType = file.type || 'application/pdf';

        // Remplacer la variable prompt par :
const prompt = document.getElementById('custom-prompt').value.trim();

        try {
            const result = await pywebview.api.process_document(base64Data, mimeType, prompt);
            outputText.value = result;
            loadingState.classList.add('hidden');
            resultContainer.classList.remove('hidden');
        } catch (err) {
            alert('Erreur : ' + err);
            resetView();
        } finally {
            base64Data = null;
            mimeType = null;
        }
    };

    reader.readAsDataURL(file);
});

function resetView() {
    outputText.value = '';
    resultContainer.classList.add('hidden');
    loadingState.classList.add('hidden');
    dropZone.classList.remove('hidden');
}

resetBtn.addEventListener('click', resetView);

copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(outputText.value);
    copyBtn.innerText = 'Copié !';
    setTimeout(() => copyBtn.innerText = 'Copier', 2000);
});