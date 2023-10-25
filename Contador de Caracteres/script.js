const textArea = document.getElementById('text-area');
const characterCount = document.getElementById('character-count');

textArea.addEventListener('input', function() {
  characterCount.textContent = textArea.value.length + ' caracteres';
});
