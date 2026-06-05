// Fetch and render grid dynamically (optional)
async function loadGrid() {
    const response = await fetch('/api/terms');
    const terms = await response.json();
    const modalities = ['acoustic', 'voice', 'audio', 'sound'];
    const harms = ['harassment', 'violence', 'surveillance', 'monitoring', 'abuse'];
    
    const table = document.getElementById('dynamic-grid');
    // Build header row
    let html = '<thead><tr><th>Modality \\ Harm</th>';
    harms.forEach(h => html += `<th>${h.charAt(0).toUpperCase()+h.slice(1)}</th>`);
    html += '</tr></thead><tbody>';
    
    modalities.forEach(mod => {
        html += `<tr><td class="modality-col">${mod.charAt(0).toUpperCase()+mod.slice(1)}</td>`;
        harms.forEach(harm => {
            const term = terms.find(t => t.modality === mod && t.harmType === harm);
            const defShort = term ? (term.definition.substring(0, 80) + '...') : '—';
            const legal = term ? term.legalBasis : '';
            html += `<td class="term-cell" data-mod="${mod}" data-harm="${harm}">
                        <div class="definition-preview">${defShort}</div>
                        <div class="legal-basis">${legal}</div>
                     </td>`;
        });
        html += '</tr>';
    });
    html += '</tbody>';
    table.innerHTML = html;
    
    // Add click handlers
    document.querySelectorAll('.term-cell').forEach(cell => {
        cell.addEventListener('click', () => {
            const mod = cell.dataset.mod;
            const harm = cell.dataset.harm;
            window.location.href = `/term/${mod}/${harm}`;
        });
    });
}
document.addEventListener('DOMContentLoaded', loadGrid);
