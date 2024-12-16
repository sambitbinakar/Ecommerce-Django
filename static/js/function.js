
$(document).ready(function(){
    const Toast = Swal.mixin({
        toast:true,
        position:"top",
        showConfirmationButton:false,
        timer:2000,
        timerProgressBar:true,
    })
    function generateCardId(){
        const ls_cartid = localStorage.getItem("cartId")

        if(ls_cartid === null){
            var cartId = "";

            for(var i =0; i< 10;i++){
                cartId += Math.floor(Math.random()*10)
            }
            localStorage.setItem("cartId" , cartId);
        }
        return ls_cartid || cartId 
    }


    $(document).on("click",".add_to_cart", function(){
        const button_el = $(this)
        const id = button_el.attr("data-id")
        const qty = $(".quantity").val()
        const size = $("input[name='Rom']:checked").val();
        const color = $("input[name='color']:checked").val();
        const cart_id = generateCardId()


        $.ajax({
            url:"/add_to_cart/",
            data:{
                id:id,
                qty:qty,
                size:size,
                color:color,
                cart_id:cart_id,
            },
            beforeSend: function (){
                button_el.html("<i class=`ri-shopping-bag-line`></i><h3 class=`font-medium text-white`>Add to Cart</h3>")
            },
            success: function(response){
                console.log(response);
                Toast.fire({
                    icon:"success",
                    title:response?.message,
                })
                button_el.html("<i class=`ri-shopping-bag-line`></i><h3 class=`font-medium text-white`>Go to Cart</h3>")
                $(".total_cart_items").text(response?.total_cart_items)
            },
            error: function(xhr, status,error){
                console.log("Error status: ",xhr.status);
                console.log("Response Text: ",xhr.responseText);

                let errorResponse = JSON.parse(xhr.responseText)
                Toast.fire({
                    icon:"success",
                    title: errorResponse?.error,
                })
            }
        })
    })
})
