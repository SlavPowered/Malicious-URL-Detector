const doc = document.querySelector("*");
const body = document.querySelector("body");
const hostname = document.getElementById('hostname');
const path = document.getElementById('path');
const evaluation = document.getElementById('evaluation');
const img = document.querySelector("img");

(async () => {
  const [tab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
  const url = new URL(tab.url);
  hostname.textContent = "Domain: " + url.hostname;
  
  fetch(`http://127.0.0.1:8080/eval?target=${tab.url}`)
  .then(response => response.json())
  .then(data => {
    if (data['prediction']){
      evaluation.textContent = "Malicious";
      doc.classList.add("malicious");
      body.classList.add("malicious");
      img.style.display = "block";
      path.textContent = "Be cautious from giving any permissions or downloading files.";
    }else{
      evaluation.textContent = "Safe";
      doc.classList.add("safe");
      body.classList.add("safe");
      path.textContent = "DOES NOT guarantee the safety of the website. Make sure to check the domain displayed above.";
    }
  })
  .catch(error => {
    console.error(error);
  });

})();