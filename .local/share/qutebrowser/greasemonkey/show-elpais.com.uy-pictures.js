// ==UserScript==
// @name         show-elpais.com.uy-pictures
// @description  Mostrar imágenes en www.elpais.com.uy
// @version  1
// @grant    none
// @include      http://elpais.com.uy/*
// @include      http://www.elpais.com.uy/*
// @include      https://elpais.com.uy/*
// @include      https://www.elpais.com.uy/*
// @namespace    https://github.com/lufte
// ==/UserScript==

setTimeout(
  function() {
    for (item of document.querySelectorAll('img[data-src]')) {
      item.setAttribute('src', item.getAttribute('data-src'));
    }
  },
  1000
);
