$(function() {
    $('#myModal form').submit(function() {
        $.ajax({
            type: "POST",
            data: $('#myModal form').serialize(),
            url: "{% url add %}",
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
                $('#todo').replaceWith(html);
                $('#myModal').modal('hide');
                $('#myModal form')[0].reset();
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert('Error occurs!');
            }
        });
        return false;
    });
    $('.icon-edit').click(function() {
        var id = $(this).parent().attr('todoid');
        $.ajax({
            url: '{% url edit %}',
            data: {
                'id': id
            },
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
                $('#editModal').replaceWith(html);
                $('#editModal').modal('show');
                $('#editModal form')[0].reset();
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert('Error occurs!');
            }
        });

        return false;

    });

    $('.icon-trash').click(function() {
        /* Act on the event */
        var id = $(this).parent().attr('todoid');
        // alert(id)
        $.ajax({
            data: {
                'id': id
            },
            url: "{% url shanchu %}",
            cache: false,
            dataType: "html",
            success: function(html, textStatus) {
                $('#todo').replaceWith(html);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert('Error occurs!');
            }
        });
        // new Ajax.Updater('todo','{% url shanchu %}',{'id' : id});
        return false;

    });

});