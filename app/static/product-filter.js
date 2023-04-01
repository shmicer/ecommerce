$(document).ready(function (){
    $('.ajaxLoader').hide();
    $('.filter-checkbox').on('click', function (){
       let _filterObj={};
       $('.filter-checkbox').each(function (index, ele){
           let _filterKey=$(this).data('filter');
           _filterObj[_filterKey]=Array.from(document.querySelectorAll(
               'input[data-filter='+_filterKey+']:checked'))
               .map(function(el) {
                   return el.value;
               });
       });

       $.ajax({
           url:'/filter-data',
           data: _filterObj,
           dataType:'json',
           beforeSend:function () {
               $('.ajaxLoader').show();
           },
           success:function (res) {
               console.log(res);
               $('#filteredProducts').html(res.items);
               $('.ajaxLoader').hide();
           }
       });

   });
});
