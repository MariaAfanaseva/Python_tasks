function createProduct(form, form_url) {
   $('#create_btn').off('click').on('click', () => {
        $.ajax(
            {
                url: form_url,
                type: 'POST',
                data: form.serialize(),
                success: (data) => {
                    console.log(data);
                    if (data.form_is_valid) {
                        $('#add_product_modal').addClass('invisible');
                        $('#products_table').html(data.result);
                    } else {
                        $('#add_product_block').html(data.result);
                    }
                }
            }
            )
        })
}

function openModal(){
    const form = $('#create_product_form');
    const form_url = form.attr('action');
    $('#create_product').off('click').on('click', () => {
         $.ajax(
            {
                url: form_url,
                type: 'GET',
                success: (data) => {
                    $('.add_product_block').html(data.result);
                }
            }
            );
        $('#add_product_modal').removeClass('invisible');
        createProduct(form, form_url);
    });

    $('#close_modal').off('click').on('click', () => {
        $('#add_product_modal').addClass('invisible');
    });
}

$(document).ready(openModal);
