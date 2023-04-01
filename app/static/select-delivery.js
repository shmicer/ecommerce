let select = document.getElementById('pickpoint');
let btnAdd = document.getElementById('pill-tab-1');
let btnRem = document.getElementById('pill-tab-0');

btnAdd.onclick = function() {
    select.name = 'address';
}
btnRem.onclick = function() {
    select.name -= 'address';
}