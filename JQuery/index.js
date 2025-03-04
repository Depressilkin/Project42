// CЕЛЕКТОРЫ
//document.getElementById('container')
//console.log(jQuery('.first'))
//console.log($('#cont'))
//console.log($('#container , #first')) // выбор нескольких
//console.log($('div:odd')) //нечетный
//console.log($('div:even')) //четный
//console.log($('#container>div:even')) //четный, внутри контейнера
////console.log($('div[name="two"]')) //по атрибуту
//console.log($('#container>div:last-child'))
//console.log($('div:nth-child(3n)'))
//console.log($('html'))
//const vrt = $('div:nth-child(3n)')
//console.log(vrt)

//СТИЛИ
//document.getElementById('container').style.backgroundColor = 'pink'
//$('#container').css('background-color', 'pink')// если изменяется одно сво-во
//$('#first').css({'background-color':'green', 'border':'solid 5px'})// для изменений нескольких свойств

//ОБРАБОТКА СОБЫТИЙ
//document.getElementById('first').addEventListener('click',function (){
//    document.getElementById('first').style.backgroundColor = 'pink'
//})
//$('div>div').on('click',function (){ // обработка события click
//    $(this).css('background-color','pink') // назначения property(сво-во) этому объекту
//})
//$('div>div').on('click',function (event){//
//    $(event.target).css('border',`solid 5px ${$(event.target).css('color')}`)// обращение к объекту через event.target
//    }
//)
//
//$('#first').trigger('click')// активизирует(вызывает) событие клик на элементе first


// ДОБАВЛЕНИЕ И УДАЛЕНИЕ ЭЛЕМЕНТОВ
//$('#null').append('<p>Привет, Я - новая строка </p>')// добавляет в конец объекта
//$('#null').prepend('<p>Привет, Я - новая строка </p>')// добавляет в начало объекта
//$('#null, #first').wrap('<section></section>') // обертка в добавленный родительский элемент

//$('<p>Привет, Я - новая строка </p>').appendTo('#first')// добавляет в конец объекта
//$('<p>Привет, Я - новая строка </p>').prependTo('#first')// добавляет в начало объекта

//$('#null').remove() // удаляет элемент, включая события на нем для освобождения памяти
//$('#first').detach() // удаляет элемент (скрывает), но оставляет его 
//свойства и события в памяти так, что если его снова добавить все свойства и события
//вернутся
//$('#null').empty() // удаляет все дочерние элементы и их события (очищает элемент от детей)
// ЭФФЕКТЫ
//$('#null').animate({ //анимация с позиционными параметрами 
//    opacity: 0.05, //{css свойства}, время выполнения, смягчение, функция после завершения анимации
//}, 5000)
//$('#first').animate({height:100},{duration:2000, queue: false}).animate({width:100},{duration:2000, queue: false})
//$('#second').fadeOut(2000).fadeIn(2000) // цепочка методов эффектов.

$('#container>div').on('click', function (event){
    $('#container>div').css('background-color','darkcyan')
    $(this).css('background-color','grey')
    let attr = '.'+$(this).attr('class')
    $('.content>div').css('display', 'none')
    $(`${attr}`).css('display', 'block')
})
$('.null').trigger('click')

