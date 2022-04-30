$( document ).ready(function() {
    $('.like-form').submit(function(e){
        e.preventDefault()

        const article_id = $(this).attr('id')

        const likeText = $(`.like-btn${article_id}`).text()
        const trim = $.trim(likeText)

        const url = $(this).attr('action')

        let result;
        const likes = $(`.like-count${article_id}`).text()
        const trimCount = parseInt(likes)

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'article_id': article_id,
            },
            success: function(response) {
                if(trim === 'Ненравится') {
                    $(`.like-btn${article_id}`).text('Нравится')
                    result = trimCount - 1
                } else {
                    $(`.like-btn${article_id}`).text('Ненравится')
                    result = trimCount + 1
                }
                $(`.like-count${article_id}`).text(result)
            },
            error: function(response) {
                console.log('error', response)
            }
        })
    })
});