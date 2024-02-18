



const title = document.querySelector(".title--wrap--Ms9Zv4A").childNodes[0].innerHTML
const images = []; document.querySelectorAll(".slider--img--D7MJNPZ").forEach(item => images.push(item.childNodes[0].src));
let price = ""; let container = null; document.querySelectorAll(".notranslate").forEach(c => c.classList.toString().includes("es--wrap") ? (container = c) : null); container.childNodes.forEach(i => "1234567890".includes(i.innerHTML) ? price += i.innerHTML : null); price
const data = { "Handle": title, "Title": title, "Body": title, "Variant Price": price, "Cost per item": price, "Images": images }; console.log


// This line code prints the data in the console, this data is added into load_bulk.json file to convert it into a csv file
function exportProduct() { const title = document.querySelector(".title--wrap--Ms9Zv4A").childNodes[0].innerHTML;const images = []; document.querySelectorAll(".slider--img--D7MJNPZ").forEach(item => images.push(item.childNodes[0].src));let price = ""; let container = null; document.querySelectorAll(".notranslate").forEach(c => c.classList.toString().includes("es--wrap") ? (container = c) : null); container.childNodes.forEach(i => "1234567890.,".includes(i.innerHTML) ? price += i.innerHTML.replace(",", ".") : null); price;const data = { "Handle": title, "Title": title, "Body": title, "Variant Price": price, "Cost per item": price, "Images": images }; console.log(JSON.stringify(data))}; exportProduct()


// function exportProduct() { const title = document.querySelector(".title--wrap--Ms9Zv4A").childNodes[0].innerHTML;const images = []; document.querySelectorAll(".slider--img--D7MJNPZ").forEach(item => images.push(item.childNodes[0].src));let price = ""; let container = null; document.querySelectorAll(".notranslate").forEach(c => c.classList.toString().includes("es--wrap") ? (container = c) : null); container.childNodes.forEach(i => "1234567890.,".includes(i.innerHTML) ? price += i.innerHTML.replace(",", ".") : null); price;const data = { "Handle": title, "Title": title, "Body": title, "Variant Price": price, "Cost per item": price, "Images": images }; console.log(JSON.stringify(data))}; exportProduct()