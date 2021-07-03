
const happyFace = document.getElementById("face1");
const noFace = document.getElementById("face2");
const sadFace = document.getElementById("face3");

let rate = NaN;

happyFace.addEventListener("click",(e) => {
    rate = 1
    happyFace.style.transform = "scale(1.2)"
    happyFace.transition = "1s"
    noFace.style.transform = "none"
    noFace.style.transition = "1s"
    sadFace.style.transform = "none"
    sadFace.style.transition = "1s"
    history.pushState(null, "", "?rate=1");
});

noFace.addEventListener("click",(e) => {
    rate = 2
    happyFace.style.transform = "none";
    happyFace.style.transition = "1s";
    noFace.style.transform = "scale(1.2)";
    noFace.style.transition = "1s";
    sadFace.style.transform = "none";
    sadFace.style.transition = "1s";
    history.pushState(null, "", "?rate=2");
    
});

sadFace.addEventListener("click",(e) => {
    rate = 3
    happyFace.style.transform = "none"
    happyFace.style.transition = "1s"
    noFace.style.transform = "none"
    noFace.style.transition = "1s"
    sadFace.style.transform = "scale(1.2)"
    sadFace.style.transition = "1s"
    history.pushState(null, "", "?rate=3");
});

console.log("ASDASD");