document.addEventListener('DOMContentLoaded', () => {
    // --- File Upload Logic ---
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const uploadPanel = document.getElementById('upload-panel');
    const loadingState = document.getElementById('loading-state');
    const resultsSection = document.getElementById('results-section');

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    dropZone.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFile(e.target.files[0]);
        }
    });

    async function handleFile(file) {
        if (file.type !== 'application/pdf') {
            alert('Please upload a PDF file.');
            return;
        }

        uploadPanel.classList.add('hidden');
        loadingState.classList.remove('hidden');

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || 'Failed to process contract');
            }

            const data = await response.json();
            displayResults(data);

        } catch (error) {
            alert(error.message);
            loadingState.classList.add('hidden');
            uploadPanel.classList.remove('hidden');
        }
    }

    function displayResults(data) {
        loadingState.classList.add('hidden');
        resultsSection.classList.remove('hidden');

        // Render Markdown
        document.getElementById('res-summary').innerHTML = marked.parse(data['Summary'] || 'No summary generated.');
        document.getElementById('res-termination').innerHTML = marked.parse(data['Termination Clause'] || 'No data found.');
        document.getElementById('res-confidentiality').innerHTML = marked.parse(data['Confidentiality Clause'] || 'No data found.');
        document.getElementById('res-liability').innerHTML = marked.parse(data['Liability Clause'] || 'No data found.');
    }

    // --- Tab Switching Logic ---
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active classes
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.add('hidden'));

            // Add active class to clicked button
            btn.classList.add('active');

            // Show target pane
            const targetId = `tab-${btn.dataset.tab}`;
            document.getElementById(targetId).classList.remove('hidden');
            document.getElementById(targetId).classList.add('active');
        });
    });
});
