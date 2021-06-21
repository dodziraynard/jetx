const nav = document.querySelector("nav")

document.addEventListener('scroll', (event)=>{
    if(window.scrollY > 60){
        nav.classList.add("show")
    } else{
        nav.classList.remove("show")
    }
})