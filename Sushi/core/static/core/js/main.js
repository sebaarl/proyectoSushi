//JQuery
$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 60) {
            $('header').css('background-color', 'rgba(0, 0, 0, 0.9)')
            $('header').css('transition', '.7s')
            $('.header__sesion').css('background-color', '#d00008')
            $('.header__sesion').css( 'transition', '.7s')
        } else {
            $('header').css('background-color', 'transparent')
            $('header').css('transition', '.7s')
            $('.header__sesion').css('background-color', '#101010')
            $('.header__sesion').css( 'transition', '.7s')
        }
    })

    $('#nav-toggle').click(function() {
        $('#nav-menu').css('left', '0')
    })
    $('#nav-toggle-close').click(function(){
      $('#nav-menu').css('left', '-100%')
    })

    $('#form-login').validate( {
        rules: {
            username: {
                required: true,
                email: true
            },
            password: {
                required: true
            }
        },
        messages: {
            username: {
                required: 'Por favor ingrese su correo electronico',
                email: "Por favor ingresa un correo válido ej: email@emial.com"
            },
            password: {
                required: 'Por favor ingrese su contraseña'
            }
        }
    })

    $("#form-register").validate( {
        rules: {
            name: {
               required: true,
               minlength: 5
            },
            password: {
               required: true,
               minlength: 5
            },
            confirm: {
               required: true,
               minlength: 5,
               equalTo: "#password"
            },
            email: {
               required: true,
               email: true
            },
         },
         messages: {           
            name: {
               required: "Por favor ingresa tu nombre y apellido",
               minlength: "Tu nombre debe ser de no menos de 5 caracteres"
            },
            password: {
               required: "Por favor ingresa una contraseña",
               minlength: "Tu contraseña debe ser de no menos de 5 caracteres"
            },
            confirm: {
               required: "Por favor confirma tu conraseña",
               minlength: "Tu contraseña debe ser de no menos de 5 caracteres",
               equalTo: "Las contraseñas no coinciden"
            },
            email: {
                required: "Por favor ingresa un correo electronico",
                email: "Por favor ingresa un correo válido ej: email@emial.com"
            }
         }
    })
})

$(document).ready(function() {
    $('.api__container').hide()
    $('.api__content').hide()
    $('#dolar').click(function() {
        $('.api__container').show()
        $('.api__content').show()
        $.getJSON('https://mindicador.cl/api', function(data) {
            let item = data;
            $('.api__content').append(
                '<h3 class=section_title apititle>Valor del dolar</h3>' + ' <div class=api_body>' +
                '<p class=api__subtitle>El valor es:</p>' +
                '<p class=api__valor>' + '$' +item.dolar.valor + '</p>' + '<p>Con un dolar no te alcanzan unos sushitos</p>' +
                '</div>')
        })
        $('#dolar').off()
    })
})

//Mostrar scroll top
function scrollTop() {
  const scrollTop = document.getElementById('scroll-top')

  if (this.scrollY >= 560) {
      scrollTop.classList.add('show-scroll')
  } else {
      scrollTop.classList.remove('show-scroll')
  }
}

window.addEventListener('scroll', scrollTop)

// MIXITUP Filtro product
const mixer = mixitup('.product__container', {
  selectors: {
      target: '.product__content'
  },
  animation: {
      duration: 0
  }
});

// LINK active-product
const linkProduct = document.querySelectorAll('.product__item')

function activeProduct() {
  if (linkProduct) {
      linkProduct.forEach(l => l.classList.remove('active-product'))
      this.classList.add('active-product')
  }
}

linkProduct.forEach(l => l.addEventListener('click', activeProduct))

