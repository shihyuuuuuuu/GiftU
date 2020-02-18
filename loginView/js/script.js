$(()=>{
    $(".button").on("click", (e)=>{
        console.log("clicked : "+$(e.target).attr("id"))
    })
})